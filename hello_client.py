import asyncio
from fastmcp import Client

async def main():
    # se define el client y se llama la tool
    client = Client("hello_server.py")
    async with client:
        result = await client.call_tool("say_hello", {"name": "Elias"})
        print(result)
        
        
asyncio.run(main())