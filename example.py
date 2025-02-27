import asyncio
import os
from dotenv import load_dotenv
from agent import BraveSearchAgent
import json

# Load environment variables from .env file
load_dotenv()

async def main():
    # Create the agent
    agent = BraveSearchAgent()
    
    # Get search query from user
    query = input("Enter your search query: ")
    
    # Run the agent
    results = await agent.run(query)
    
    # Print the results
    print("\nSearch Results:")
    print(json.dumps(results, indent=2))
    
    # Print in a more readable format
    print("\nFormatted Results:")
    for i, result in enumerate(results["results"], 1):
        print(f"\n{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   {result['description']}")

if __name__ == "__main__":
    asyncio.run(main())
