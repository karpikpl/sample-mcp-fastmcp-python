import asyncio
import pytest
from fastmcp import Client
from server import mcp

client = Client(mcp)

@pytest.mark.asyncio
async def test_add_tool():
    async with client:
        result = await client.call_tool("add", {"a": 3, "b": 5})
        assert result.data == 8, f"Expected 8, got {result.data}"

@pytest.mark.asyncio
async def test_subtract_tool():
    async with client:
        result = await client.call_tool("subtract", {"a": 5, "b": 3})
        assert result.data == 2, f"Expected 2, got {result.data}"