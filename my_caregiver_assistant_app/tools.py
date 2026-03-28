import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

def get_medlineplus_mcp_toolset():
    tools = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url="http://localhost:8081/mcp"
        )
    )
    print("MCP Toolset configured for MedlinePlus NIH server.")
    return tools