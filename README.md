# Brave Search Agent

This agent uses the Brave Search API to search the internet and return results in a user-friendly format.

## Overview

The Brave Search Agent is a tool that allows you to search the internet using the Brave Search API. It provides both a command-line interface and a web interface built with Streamlit.

## Setup Instructions

### For Novice Users

1. **Prerequisites**:
   - Make sure you have Python installed on your computer (Python 3.8 or higher recommended)
   - Make sure you have Git installed to clone the repository

2. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/archon.git
   cd archon
   ```

3. **Set Up the Virtual Environment**:
   ```
   # Create and activate a virtual environment
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install Dependencies**:
   ```
   cd agent1
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```
   streamlit run streamlit_app.py
   ```
   
   Or use the auto-shutdown version that will terminate when you close your browser:
   ```
   python auto_shutdown_app.py
   ```

6. **Access the Web Interface**:
   - Open your web browser and go to the URL shown in the terminal (typically http://localhost:8501)
   - Enter your search query in the text box
   - Adjust the number of results using the slider
   - Click the "Search" button to see the results
   - When using auto_shutdown_app.py, the server will automatically shut down when you close the browser tab

### For Developers

1. **Environment Setup**:
   ```
   git clone https://github.com/your-username/archon.git
   cd archon
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   
   cd agent1
   pip install -r requirements.txt
   ```

2. **API Key Configuration**:
   - The API key is currently hardcoded in the `agent.py` file for simplicity
   - For production use, you should modify the code to use environment variables:
     - Create a `.env` file in the agent1 directory
     - Add your Brave API key: `BRAVE_API_KEY=your_brave_api_key_here`
     - Update the `agent.py` file to load the key from environment variables:
       ```python
       from dotenv import load_dotenv
       load_dotenv()
       BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")
       ```

3. **Running the Application**:
   ```
   cd agent1
   streamlit run streamlit_app.py
   ```
   
   For automatic shutdown when the browser is closed:
   ```
   cd agent1
   python auto_shutdown_app.py
   ```

4. **Development and Testing**:
   - Use `example.py` to test the agent functionality in a script
   - Use `test_env.py` to test if environment variables are loaded correctly
   - Use `test_brave_api.py` to test the Brave API key functionality

## Usage Examples

### Command Line Usage

```python
from agent import BraveSearchAgent
import asyncio

async def main():
    agent = BraveSearchAgent()
    results = await agent.search("your search query here", count=10)
    print(results)

asyncio.run(main())
```

### Streamlit Web Interface

Run the Streamlit app to use a web interface for the search agent:

```bash
streamlit run streamlit_app.py
```

This will start a local web server and open the application in your browser. You can enter your search queries in the web interface and see the results displayed in a user-friendly format.

## Troubleshooting

### Common Issues and Solutions

1. **API Key Error**:
   - If you see an error about the API key not being set, make sure the API key is correctly set in the `agent.py` file
   - For production, ensure your `.env` file is in the correct location and contains the valid API key

2. **Package Not Found Errors**:
   - Make sure you've activated the virtual environment
   - Run `pip install -r requirements.txt` to install all required packages

3. **Streamlit Not Starting**:
   - Make sure you're in the correct directory (`agent1`)
   - Make sure Streamlit is installed: `pip install streamlit`

4. **Multiple Streamlit Instances**:
   - If you have multiple Streamlit instances running (on ports 8501, 8502, etc.), you can stop them using:
     ```
     # Find all Streamlit processes
     netstat -ano | findstr :850
     
     # Kill the processes (replace PID with the actual process IDs)
     taskkill /F /PID <PID1> /PID <PID2> /PID <PID3>
     ```
   - Alternatively, you can restart your computer to stop all running instances

## Extending the Agent

### Ideas for Improvement

1. **Add More Search Options**:
   - Implement filters for search results (e.g., by date, region, language)
   - Add options to search for images, news, or videos

2. **Enhance the User Interface**:
   - Add more visualization options for search results
   - Implement a history feature to save past searches

3. **Integrate with Other APIs**:
   - Combine with other search APIs for more comprehensive results
   - Add functionality to compare results from different search engines

4. **Implement Authentication**:
   - Add user authentication to save preferences and search history
   - Implement rate limiting to prevent API abuse

## API Reference

### BraveSearchAgent

- `search(query: str, count: int = 5)`: Search the internet using the Brave Search API
  - `query`: The search query string
  - `count`: Number of results to return (default: 5)
  - Returns: List of search results as dictionaries

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Brave Search API](https://brave.com/search/api/) for providing the search functionality
- [Streamlit](https://streamlit.io/) for the web interface framework
