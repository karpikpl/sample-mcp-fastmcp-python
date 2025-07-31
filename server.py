import asyncio
import logging
import os
import fastmcp

from fastmcp import FastMCP 

# Add FastAPI exception handler for HTTP 409 Conflict
from fastmcp.server.middleware import Middleware, MiddlewareContext

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

if __name__ == "__main__":
    port = os.getenv('PORT', 3000)
    logger.info(f"🚀 MCP server starting on host 0.0.0.0, port {port}")
    logger.debug(f"[startup] Environment variables: {dict(os.environ)}")
    try:
        asyncio.run(
            mcp.run_async(
                transport="streamable-http",
                host="0.0.0.0",
                port=port,
            )
        )
        logger.info("✅ MCP server started successfully.")
    except Exception as e:
        logger.error(f"❌ MCP server failed to start: {e}", exc_info=True)