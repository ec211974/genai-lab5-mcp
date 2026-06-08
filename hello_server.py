from fastmcp import FastMCP

# se instancia el servidor
mcp = FastMCP("HelloServer")

# se define una tool (un tipo de primitiva)
@mcp.tool
def say_hello(name: str) -> str:
    """Returns a friendly greeting."""
    return f"Hello {name}!"

# corre el servidor
if __name__ == "__main__":
    mcp.run()