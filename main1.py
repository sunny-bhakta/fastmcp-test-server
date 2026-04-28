import random
import json
from fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP(name="Demo Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.resource("resource://server-info", mime_type="application/json")
def server_info() -> str:
    """Read-only metadata about this demo MCP server."""
    return json.dumps(
        {
            "name": "Demo Server",
            "tools": ["roll_dice", "add_numbers"],
            "resources": ["resource://server-info", "resource://greeting/{name}"],
            "status": "ok",
        }
    )


@mcp.resource("resource://greeting/{name}")
def greeting_resource(name: str) -> str:
    """Return a greeting resource for a specific name."""
    return f"Hello, {name}! This came from an MCP resource."

if __name__ == "__main__":
    mcp.run()