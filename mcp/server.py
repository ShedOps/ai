from mcp.server.fastmcp import FastMCP

# Create a MCP server
mcp = FastMCP("Weather Service")

# Tool implementation
@mcp.tool()
def get_weather(location: str) -> str:
    """Get the weather for a given location"""
    return f"The weather in {location} is sunny."

# Resource implementation
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource"""
    return f"Weather data for {location}: Sunny, 72F"

# Prompt implementation
@mcp.prompt()
def weather_prompt(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""

# Run the server
if __name__ == "__main__":
    mcp.run()