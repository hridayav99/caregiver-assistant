import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioServerParameters

def get_medlineplus_mcp_toolset():
    server_path = os.path.join(os.path.dirname(__file__), "..", "mcp_server", "medlineplus_server.py")
    tools = MCPToolset(
            connection_params=StdioServerParameters(
                command="python3",  # use python3 instead of python
                args=[os.path.abspath(server_path)],
                env={
                    **os.environ,  # pass all environment variables
                }
            )
        )
    print("MCP Toolset configured for MedlinePlus NIH server.")
    return tools