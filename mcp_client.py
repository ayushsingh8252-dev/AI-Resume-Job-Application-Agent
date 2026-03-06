from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

async def main()
    client = MultiServerMCPClient(
        {
            "mcp_server":{
                "command" : "python",
                "args" : ["mcp_server.py"],
                "transport" : "stdio",
            },
        }
    )