from pydantic_ai import Agent
import os
import httpx
import json
from typing import List, Dict, Any, Optional

# Brave API configuration
# Set the API key directly in the code for testing
# In production, you would use environment variables
BRAVE_API_KEY = "BSAoH1ER3IiBODiGc5TSr7VgJzbw657"
BRAVE_SEARCH_URL = "https://api.search.brave.com/res/v1/web/search"

class BraveSearchAgent:
    """Agent that can search the internet using the Brave Search API."""
    
    def __init__(self):
        self.name = "brave_search_agent"
        
        if not BRAVE_API_KEY:
            raise ValueError("BRAVE_API_KEY is not set")
    
    async def search(self, query: str, count: int = 5) -> List[Dict[str, Any]]:
        """
        Search the internet using the Brave Search API.
        
        Args:
            query: The search query
            count: Number of results to return (default: 5)
            
        Returns:
            List of search results
        """
        headers = {
            "Accept": "application/json",
            "X-Subscription-Token": BRAVE_API_KEY
        }
        
        params = {
            "q": query,
            "count": count
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                BRAVE_SEARCH_URL,
                headers=headers,
                params=params
            )
            
            if response.status_code != 200:
                raise Exception(f"Brave Search API returned status code {response.status_code}: {response.text}")
            
            data = response.json()
            return data.get("web", {}).get("results", [])

    async def run(self, query: str) -> Dict[str, Any]:
        """
        Run the agent with a search query.
        
        Args:
            query: The search query
            
        Returns:
            Dictionary with search results
        """
        results = await self.search(query)
        
        formatted_results = []
        for result in results:
            formatted_results.append({
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "description": result.get("description", "")
            })
        
        return {
            "query": query,
            "results": formatted_results
        }

# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def main():
        agent = BraveSearchAgent()
        results = await agent.run("artificial intelligence latest developments")
        print(json.dumps(results, indent=2))
    
    asyncio.run(main())
