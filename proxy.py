# from fastmcp import FastMCP

# # Create a proxy to your remote FastMCP Cloud server
# # FastMCP Cloud uses Streamable HTTP (default), so just use the /mcp URL
# mcp = FastMCP.as_proxy(
#     "https://expense-tracker-remote-mcp.fastmcp.app/mcp",  # Standard FastMCP Cloud URL
#     name="Expense-Tracker-Remote-MCP"
# )

# if __name__ == "__main__":
#     # This runs via STDIO, which Claude Desktop can connect to
#     mcp.run()

from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "https://expense-tracker-remote-mcp.fastmcp.app/mcp",
    name="Expense-Tracker-Remote-MCP",
    headers={
        "Authorization": "Bearer vinayak123"
    }
)

if __name__ == "__main__":
    mcp.run()