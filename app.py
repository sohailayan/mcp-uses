import os
#i/o operation when waiting for user input or sending data over network
import asyncio 
#allows python script to read environment variables from .env file
from dotenv import load_dotenv
#groq is a large language model provider
from langchain_groq import ChatGroq
#MCPClient: Connects to a browser automation MCP server.
#MCPAgent: Handles AI interactions with built-in memory and connects with the MCP client.
from mcp_use import MCPAgent, MCPClient

async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory."""
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Config file path - update if needed , available mcp browser server that we can use
    config_file = "browser_mcp.json"

    print("Initializing chat...")

    # Create MCPClient from config file
    #browser automation server
    client = MCPClient.from_config_file(config_file)

    llm = ChatGroq(model="qwen-qwq-32b")

    # Create agent with memory enabled
    agent = MCPAgent(
        llm=llm,
        client=client,
        memory_enabled=True,
        #reasoning steps
        max_steps=15,
    )

    print("\n==== Interactive MCP Chat ====")
    print("Type 'exit' or 'quit' to end the chat.")
    print("Type 'clear' to clear the memory.")
    print("================================\n")

    try:
        while True:
            # Get user input
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat...")
                break
            elif user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared")
                continue

            # Get response from agent
            print("Assistant: ", end="", flush=True)

            try:
                #Calls the run() method of the agent to process the input and generate a response
                response = await agent.run(user_input)
                print(response)
                
            except Exception as e:
                print(f"\nError: {e}")

    finally:
        # Clean up
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
