The USB-C for AI applications...

Working through the examples found over at huggingface.
Ref: Official Python SDK - https://github.com/modelcontextprotocol/python-sdk

## Tiny Agents Client
### MCP Client that connects directly to an MCP Server, using a CLI environment

### Steps

1. Use the existing python virtual environment

```python -m venv venv```

2. Activate the virtual environment

```source venv/bin/activate```

3. Install npx

```npm install -g npx```

4. Install the hugging face package with MCP support (for MCP servers and clients)

```pip install "huggingface_hub[mcp]>=0.33.2"```

5. Update our Node package

```npm install @huggingface/tiny-agents```

6. TESTING ONLY: Next export your Hugging Face Hub access token (you need a HF account for this and an access token)

```export HF_TOKEN=hf_123456789```

7. Now we can connect to the HF MCP server, using the sample json provided (we are using the @playwright/mcp MCP server here)
it can control a browser with Playwright

```npx tiny-agents run ./agent.json```

8. Open Google Chrome incognito window and accept / reject cookies, then make sure Google Chrome is completely closed / terminated

9. Enter the following prompt, as an example (taken from the HuggingFace MCP course)

```do a Web Search for HF inference providers on Brave Search and open the first result and then give me the list of the inference providers supported on Hugging Face```

10. TROUBLESHOOTING (note: 401 usually means authentication issues)

```npx @modelcontextprotocol/inspector -- npx @playwright/mcp@latest --headless```

...and...

```DEBUG=@huginface/* npx tiny-agents run ./agent.json```
