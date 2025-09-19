The USB-C for AI applications...

Working through the examples found over at huggingface.
Ref: Official Python SDK - https://github.com/modelcontextprotocol/python-sdk

## Gradio MCP Server Example

### Steps

1. Use our existing python virtual environment

```python -m venv venv```

2. Activate the virtual environment

```source venv/bin/activate```

3. Install Gradio with the MCP extra

```pip install "gradio[mcp]"```

4. Fire up the MCP server via Gradio

```python ./server.py```

5. Add 'client.json' content to your MCP Hosts in Cursor (Cursor -> Settings -> Cursor Settings -> MCP Add) as we need to use an LLM application that supports using tools via MCP servers

6. In "New Chat" in Cursor, type the following prompt, which should result in the LLM choosing
the available MCP server and 'letter_counter' tool

```count the number of letters in the word 'hello'```

7. Tools and schema available via

http://127.0.0.1:7860/gradio_api/mcp/schema