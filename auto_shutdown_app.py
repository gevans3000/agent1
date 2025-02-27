import subprocess
import sys
import time
import webbrowser
import os
import signal
import threading
import socket
import psutil

def find_free_port():
    """Find a free port on the system."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def check_connection(port):
    """Check if there are active connections to the Streamlit app."""
    connections = 0
    for conn in psutil.net_connections():
        if conn.laddr.port == port and conn.status == 'ESTABLISHED':
            connections += 1
    
    # Streamlit creates multiple connections, but when browser is closed,
    # the number drops significantly
    return connections > 2

def monitor_connections(process, port, check_interval=5):
    """Monitor connections and terminate the process when no connections are detected."""
    print(f"Monitoring connections on port {port}...")
    
    # Give some time for initial connections to be established
    time.sleep(10)
    
    last_active = time.time()
    while True:
        if check_connection(port):
            last_active = time.time()
        elif time.time() - last_active > 10:  # No connections for 10 seconds
            print("No active connections detected. Shutting down...")
            try:
                # On Windows
                os.kill(process.pid, signal.CTRL_C_EVENT)
            except:
                try:
                    process.terminate()
                except:
                    pass
            break
        
        time.sleep(check_interval)

def main():
    # Find a free port
    port = find_free_port()
    
    # Start Streamlit on the free port
    streamlit_cmd = [
        sys.executable, "-m", "streamlit", "run", 
        "streamlit_app.py", 
        "--server.port", str(port),
        "--server.headless", "true"
    ]
    
    print(f"Starting Streamlit app on port {port}...")
    process = subprocess.Popen(streamlit_cmd)
    
    # Give Streamlit time to start
    time.sleep(2)
    
    # Open the browser
    url = f"http://localhost:{port}"
    print(f"Opening browser at {url}")
    webbrowser.open(url)
    
    # Start monitoring thread
    monitor_thread = threading.Thread(
        target=monitor_connections, 
        args=(process, port),
        daemon=True
    )
    monitor_thread.start()
    
    try:
        # Wait for the process to complete
        process.wait()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Shutting down...")
        process.terminate()
    
    print("Streamlit app has been shut down.")

if __name__ == "__main__":
    main()
