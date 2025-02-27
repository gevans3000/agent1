import os
import requests
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Get the Brave API key
brave_api_key = os.getenv("BRAVE_API_KEY")

# Check if the Brave API key is set
if not brave_api_key:
    print("❌ The Brave API key is not set in the .env file!")
    exit(1)

print(f"Using Brave API key: {brave_api_key[:5]}...{brave_api_key[-4:]}")

# Brave Search API URL
url = "https://api.search.brave.com/res/v1/web/search"

# Headers with the API key
headers = {
    "Accept": "application/json",
    "X-Subscription-Token": brave_api_key
}

# Parameters for the search query
params = {
    "q": "test query",  # Simple test query
    "count": 1          # Just get one result to verify it works
}

print("\nSending request to Brave Search API...")
try:
    # Make the request
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("✅ API request successful! (Status code: 200)")
        
        # Parse the response
        data = response.json()
        
        # Check if we got search results
        if "web" in data and "results" in data["web"] and len(data["web"]["results"]) > 0:
            print("✅ Received search results!")
            
            # Display the first result
            first_result = data["web"]["results"][0]
            print("\nFirst search result:")
            print(f"Title: {first_result.get('title', 'N/A')}")
            print(f"URL: {first_result.get('url', 'N/A')}")
            print(f"Description: {first_result.get('description', 'N/A')[:100]}...")
        else:
            print("❌ No search results found in the response.")
            print("Response data:", json.dumps(data, indent=2))
    else:
        print(f"❌ API request failed with status code: {response.status_code}")
        print("Response:", response.text)
        
        # Common error codes and their meanings
        if response.status_code == 401:
            print("This usually means your API key is invalid or has expired.")
        elif response.status_code == 429:
            print("You've exceeded your rate limit or quota.")
        
except Exception as e:
    print(f"❌ An error occurred: {str(e)}")

print("\nTest completed.")
