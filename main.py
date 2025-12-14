from fastmcp import FastMCP
import random 
import json


mcp = FastMCP("Simple-Calculator-Server")

@mcp.tool
def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b

@mcp.tool   
def random_number(min_value=1, max_value=100):
    """
    Generate a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)

@mcp.tool
def server_info():
    """
    Return server information as a JSON string.
    """
    info = {
        "server_name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A server that performs simple arithmetic operations and generates random numbers.",
        "tools": ["add", "random_number", "server_info"],
        "author": "Software Engineer"
    }
    return json.dumps(info, indent=2)



if __name__ == "__main__":
    mcp.run(transport='http', host='0.0.0.0', port=8000)
