import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Brave API key
brave_api_key = os.getenv("BRAVE_API_KEY")

# Print the Brave API key
print(f"BRAVE_API_KEY: {brave_api_key}")

# Check if the Brave API key is set
if brave_api_key:
    print("✅ The Brave API key is set correctly!")
else:
    print("❌ The Brave API key is not set!")
