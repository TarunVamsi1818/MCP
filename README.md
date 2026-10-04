# Example MCP Server

This project implements a minimal Model Context Protocol (MCP) server in Python using the official `mcp` SDK.

## Features

- Adds two integers
- Lists the contents of a directory
- Reads a text file from disk safely
- Runs over stdio, which is the default transport for MCP clients

## Setup

```bash
python -m pip install -e .
```

## Run

```bash
example-mcp-server
```

You can also invoke the package directly:

```bash
python -m mcp_server
```
