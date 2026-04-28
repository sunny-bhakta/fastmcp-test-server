# FastMCP demo server (Windows, no admin)

Use this project from `cmd.exe` with a local `venv`.

## Setup

```cmd
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install uv
python -m uv pip install "fastmcp[apps]"
```

## Check install

```cmd
python -m uv run --active fastmcp version
```

## Run your server file (`main.py`)

```cmd
python -m uv run --active python main.py
```

## FastMCP developer mode commands

`fastmcp dev` expects a subcommand (`inspector` or `apps`) plus a server spec.

```cmd
python -m uv run --active fastmcp dev inspector main.py
python -m uv run --active fastmcp dev apps main.py
```

If needed, you can be explicit about the server object:

```cmd
python -m uv run --active fastmcp dev inspector main.py:mcp
python -m uv run --active fastmcp dev apps main.py:mcp
```

## Why `uv run fastmcp dev main.py` failed

`main.py` was interpreted as a command argument in the wrong position.
Use `dev inspector` or `dev apps` before the file path.

## Troubleshooting: `spawn UNKNOWN` when opening Inspector

If you see this on Windows:

- `MCP Inspector is up and running at http://localhost:6274/...`
- then Node crashes with `Error: spawn UNKNOWN`

your server is usually fine; the failure is from auto-opening the browser.

### Fix 0 (recommended): Disable Inspector auto-open

```cmd
set MCP_AUTO_OPEN_ENABLED=false
python -m uv run --active fastmcp dev inspector main.py:mcp
```

Then copy the printed `http://localhost:...` URL and open it manually.

### Fix 1: Set browser executable explicitly

```cmd
set "BROWSER=C:\Program Files\Google\Chrome\Application\chrome.exe"
python -m uv run --active fastmcp dev inspector main.py:mcp
```

If you use Edge:

```cmd
set "BROWSER=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
python -m uv run --active fastmcp dev inspector main.py:mcp
```

### Fix 2: Run server directly (no Inspector auto-open)

```cmd
python -m uv run --active python main.py
```

### Fix 3: If Inspector prints a localhost URL, open it manually

Copy the printed `http://localhost:...` URL and open it in your browser.



venv\Scripts\python.exe -m uv run --active fastmcp install claude-desktop main.py:mcp 
Successfully installed 'Demo Server' in Claude Desktop