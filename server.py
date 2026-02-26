import random 
from fastmcp import FastMCP

mcp = FastMCP(name = "Demo Server")

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

#to run a server 
if __name__ == "__main__":
    mcp.run()