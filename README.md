# Sample MCP Python

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![FastMCP](https://img.shields.io/badge/FastMCP-2.10.6-brightgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-brightgreen)
![Docker](https://img.shields.io/badge/docker-ready-blue)

## 🚀 Overview

Sample MCP Python is a modern, container-ready MCP (Model Context Protocol) server built with [FastMCP](https://gofastmcp.com/) and FastAPI. It provides simple arithmetic tools and is designed for easy extension and cloud deployment.

## ✨ Features

- **FastMCP Server**: Implements MCP protocol for agent communication.
- **Arithmetic Tools**: Includes `add` and `subtract` as MCP tools.
- **Custom Middleware**: Logging middleware for all MCP operations.
- **FastAPI Exception Handling**: Handles session and route errors gracefully.
- **Docker Support**: Ready for containerized deployment.
- **Configurable Logging**: Debug and info logs for all operations.

## 🗂️ Project Structure

```
sample-mcp-python/
├── server.py          # Main MCP server with tools and middleware
├── test_server.py     # (Empty) Placeholder for tests
├── Dockerfile         # Container build instructions
├── pyproject.toml     # Python project metadata and dependencies
├── uv.lock            # Dependency lock file
├── .gitignore         # Git ignore rules
├── .dockerignore      # Docker ignore rules
```

## 🛠️ Usage

### Prerequisites

- Python 3.12+
- Docker (optional, for container deployment)

### Local Development

1. **Install dependencies:**
   ```sh
   uv sync
   ```

2. **Run the server:**
   ```sh
   uv run server.py
   ```

### Docker

1. **Build the image:**
   ```sh
   docker build -t sample-mcp-python .
   ```

2. **Run the container:**
   ```sh
   docker run -p 3000:3000 sample-mcp-python
   ```

## 🧩 MCP Tools

- `add(a: int, b: int) -> int`: Adds two numbers.
- `subtract(a: int, b: int) -> int`: Subtracts the second number from the first.

## ⚙️ Configuration

- **Port**: Set the `PORT` environment variable to change the server port (default: 3000).
- **Logging**: Controlled via `fastmcp.settings.log_level` and Python logging config.

## 📝 Extending

Add new MCP tools by decorating functions with `@mcp.tool()` in `server.py`.  
Custom middleware can be added for logging, authentication, etc.


## 🧪 Testing

Tests are written in `test_server.py` using [pytest](https://pytest.org/) and [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) for async support.

### Run tests

Then, run the tests:
```sh
uv run pytest
```

Example async test:
```python
import pytest
from fastmcp import Client
from server import mcp

client = Client(mcp)

@pytest.mark.asyncio
async def test_add_tool():
    async with client:
        result = await client.call_tool("add", {"a": 3, "b": 5})
        assert result == 8
```

## 📦 Dependencies

- `fastmcp==2.10.6`
- `fastapi>=0.116.1`

## 📄 License

MIT License (add your license file if needed)

---

> Made with ❤️ using FastMCP and Python.
