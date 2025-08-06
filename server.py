import asyncio
import logging
import os
import fastmcp

from fastmcp import FastMCP

from starlette.requests import Request
from starlette.responses import JSONResponse

# Add FastAPI exception handler for HTTP 409 Conflict
from fastmcp.server.middleware import Middleware, MiddlewareContext
import httpx

from weather_models import WeatherData, dict_to_weather_data


class LoggingMiddleware(Middleware):
    """Middleware that logs all MCP operations."""

    async def on_message(self, context: MiddlewareContext, call_next):
        """Called for all MCP messages."""
        print(f"Processing {context.method} from {context.source}")

        result = await call_next(context)

        print(f"Completed {context.method}")
        return result


logger = fastmcp.utilities.logging.get_logger("mcp_server")
logger.setLevel(logging.DEBUG)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.DEBUG)

run_stateless = os.getenv("STATELESS", "true").lower() in ("true", "1", "yes")

mcp = FastMCP("MCP Server")
mcp.add_middleware(LoggingMiddleware())
print(fastmcp.settings.log_level)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    logger.info(f"[add] Tool called with a={a}, b={b}")
    result = a + b
    logger.debug(f"[add] Computed result: {result}")
    return result


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Use this to subtract two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference of the two numbers.
    """
    logger.info(f"[subtract] Tool called with a={a}, b={b}")
    result = a - b
    logger.debug(f"[subtract] Computed result: {result}")
    return result


@mcp.tool()
async def get_weather(location: str) -> WeatherData:
    """Use this to get the weather for a given location.
    Args:
        location: The location to get the weather for. e.g., "London", "New York".
    Returns:
        A dictionary containing the weather data.
    """
    # Make request to wttr.in
    wttrUrl = f"https://wttr.in/{location}?format=j1"
    logger.info(f"[get_weather] Fetching weather for {location} from {wttrUrl}")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(wttrUrl)
            weather_data = response.json()
        logger.debug(f"[get_weather] Received weather data: {weather_data}")
        return dict_to_weather_data(weather_data)
    except httpx.HTTPStatusError as e:
        logger.error(
            f"[get_weather] HTTP error occurred: {e.response.status_code} - {e.response.text}"
        )
        raise fastmcp.exceptions.MCPError(
            f"Failed to fetch weather data: {e.response.status_code} - {e.response.text}"
        )


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request):
    return JSONResponse({"status": "healthy"})


if __name__ == "__main__":
    port = os.getenv("PORT", 3000)
    logger.info(f"🚀 MCP server starting on host 0.0.0.0, port {port}")
    logger.debug(f"[startup] Environment variables: {dict(os.environ)}")
    try:
        asyncio.run(
            mcp.run_async(
                transport="streamable-http",
                host="0.0.0.0",
                port=port,
                stateless_http=run_stateless,
            )
        )
        logger.info("✅ MCP server started successfully.")
    except Exception as e:
        logger.error(f"❌ MCP server failed to start: {e}", exc_info=True)
