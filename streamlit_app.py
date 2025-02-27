import streamlit as st
import asyncio
import os
import json
from agent import BraveSearchAgent

# Set page title and configuration
st.set_page_config(
    page_title="Brave Search Agent",
    page_icon="🔍",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .result-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        border-left: 5px solid #ff7f50;
    }
    .result-title {
        color: #1e88e5;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .result-url {
        color: #4caf50;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .result-description {
        color: #424242;
        font-size: 16px;
    }
    .search-header {
        background-color: #ff7f50;
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="search-header"><h1>🔍 Brave Search Agent</h1><p>Search the internet using the Brave Search API</p></div>', unsafe_allow_html=True)

# Create a form for the search query
with st.form(key="search_form"):
    query = st.text_input("Enter your search query:", placeholder="Type your search query here...")
    num_results = st.slider("Number of results:", min_value=1, max_value=20, value=5)
    submit_button = st.form_submit_button(label="Search")

# Function to run the search asynchronously
async def run_search(query, count):
    try:
        agent = BraveSearchAgent()
        results = await agent.search(query, count)
        return results
    except Exception as e:
        st.error(f"Error during search: {str(e)}")
        return []

# Handle search when the form is submitted
if submit_button and query:
    with st.spinner("Searching..."):
        try:
            # Run the async function in a synchronous context
            results = asyncio.run(run_search(query, num_results))
            
            # Display the results
            if results:
                st.success(f"Found {len(results)} results for '{query}'")
                
                for i, result in enumerate(results, 1):
                    title = result.get("title", "No title")
                    url = result.get("url", "#")
                    description = result.get("description", "No description available")
                    
                    # Create a card for each result
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-title">{i}. {title}</div>
                        <div class="result-url"><a href="{url}" target="_blank">{url}</a></div>
                        <div class="result-description">{description}</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No results found. Try a different query.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please check your API key and try again.")

# Add information about the API
with st.expander("About Brave Search API"):
    st.markdown("""
    This application uses the [Brave Search API](https://brave.com/search/api/) to search the internet.
    
    The Brave Search API provides:
    - Privacy-respecting search results
    - No tracking or profiling
    - Independent search index
    
    To use this application, you need a Brave Search API key. You can get one from the [Brave Search API website](https://brave.com/search/api/).
    """)

# Add footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Brave Search API")
