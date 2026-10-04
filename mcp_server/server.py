from __future__ import annotations

from pathlib import Path
from typing import Any

from mcp.server.mcpserver import MCPServer

server = MCPServer(
    name="example-mcp-server",
    title="Example MCP Server",
    description="A small MCP server for basic arithmetic and filesystem operations.",
    instructions=(
        "Use the available tools to add numbers, inspect directories, and read text files. "
        "Keep file access focused on the requested path and avoid reading outside the intended workspace."
    ),
    version="0.1.0",
)


@server.tool()
def add_numbers(a: int, b: int) -> dict[str, int]:
    """Add two integers and return the result as a JSON object."""
    return {"sum": a + b}


@server.tool()
def list_directory(path: str = ".") -> dict[str, Any]:
    """List files and folders inside a directory."""
    target = Path(path).expanduser()
    if not target.exists():
        raise ValueError(f"Path does not exist: {path}")
    if not target.is_dir():
        raise ValueError(f"Path is not a directory: {path}")

    entries = sorted(item.name for item in target.iterdir())
    return {"path": str(target.resolve()), "entries": entries}


@server.tool()
def read_file(path: str) -> dict[str, Any]:
    """Read a text file and return its contents."""
    target = Path(path).expanduser()
    if not target.exists():
        raise ValueError(f"File does not exist: {path}")
    if not target.is_file():
        raise ValueError(f"Path is not a file: {path}")

    try:
        content = target.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"File is not UTF-8 text: {path}") from exc

    return {"path": str(target.resolve()), "content": content}


def main() -> None:
    """Run the MCP server over stdio."""
    server.run(transport="stdio")


if __name__ == "__main__":
    main()
