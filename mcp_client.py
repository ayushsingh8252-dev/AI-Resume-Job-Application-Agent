from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

async def main():
    client = MultiServerMCPClient(
        {
            "mcp_server":{
                "command" : "python",
                "args" : ["mcp_server.py"],
                "transport" : "stdio",
            },
        }
    )

import os
tools = await.client.get_tools()
