from flask import Flask, render_template, request, jsonify, session
import requests
import json
import os
from datetime import datetime
import threading

app = Flask(__name__, static_folder="static")
app.secret_key = os.urandom(24)  # For session management

# In-memory storage for whiteboards (in production, use a database)
# Structure: {session_id: {data: [...], last_updated: timestamp}}
whiteboards = {}
whiteboard_lock = threading.Lock()  # Thread safety for data access

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tenor-proxy')
def tenor_proxy():
    """Proxy for Tenor API to avoid CORS issues"""
    search = request.args.get('q', '')
    api_key = request.args.get('key', '')
    limit = request.args.get('limit', 12)
    
    if not search or not api_key:
        return jsonify({"error": "Missing parameters"}), 400
    
    try:
        # Print request parameters for debugging
        print(f"Tenor request: q={search}, key={api_key}, limit={limit}")
        
        response = requests.get(
            "https://api.tenor.com/v1/search",
            params={
                "q": search,
                "key": api_key,
                "limit": limit
            },
            timeout=10
        )
        
        # Check for error response
        if response.status_code != 200:
            print(f"Tenor API error: Status {response.status_code}")
            return jsonify({"error": f"Tenor API error: {response.status_code}"}), response.status_code
        
        # Try to parse response as JSON to ensure it's valid
        result = response.json()
        
        # Debug: Print the structure of the response
        print("API response structure:", json.dumps(result, indent=2)[:500] + "...")
        
        # Check for expected data structure
        if 'results' not in result:
            print("Warning: 'results' not in API response")
            
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return jsonify({"error": f"Request error: {str(e)}"}), 500
    except json.JSONDecodeError as e:
        print(f"Invalid JSON response: {str(e)}")
        return jsonify({"error": "Invalid response from Tenor API"}), 500
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/whiteboard/<session_id>', methods=['GET', 'POST'])
def whiteboard_data(session_id):
    """API endpoint to get or update whiteboard data"""
    # Normalize session ID
    session_id = f"whiteboard_{session_id}" if not session_id.startswith("whiteboard_") else session_id
    
    if request.method == 'GET':
        # Return current whiteboard data
        with whiteboard_lock:
            data = whiteboards.get(session_id, {}).get('data', [])
            return jsonify({"data": data})
    
    elif request.method == 'POST':
        try:
            # Update whiteboard with new data
            new_data = request.json.get('data', [])
            
            with whiteboard_lock:
                whiteboards[session_id] = {
                    'data': new_data,
                    'last_updated': datetime.now()
                }
            
            return jsonify({"status": "success", "message": "Whiteboard updated"})
        
        except Exception as e:
            print(f"Error saving whiteboard data: {str(e)}")
            return jsonify({"error": str(e)}), 500

@app.route('/api/whiteboard/<session_id>/poll', methods=['GET'])
def whiteboard_poll(session_id):
    """Polling endpoint for checking if whiteboard has updates"""
    # Normalize session ID
    session_id = f"whiteboard_{session_id}" if not session_id.startswith("whiteboard_") else session_id
    
    # Get client's last update timestamp
    client_timestamp = request.args.get('last_updated', '0')
    try:
        client_timestamp = float(client_timestamp)
    except ValueError:
        client_timestamp = 0
    
    with whiteboard_lock:
        whiteboard = whiteboards.get(session_id, {})
        
        if not whiteboard:
            return jsonify({"has_updates": False})
        
        # Convert server timestamp to float for comparison
        server_timestamp = whiteboard.get('last_updated', datetime.now())
        server_timestamp_float = server_timestamp.timestamp()
        
        # Check if server has newer data
        has_updates = server_timestamp_float > client_timestamp
        
        return jsonify({
            "has_updates": has_updates,
            "server_timestamp": server_timestamp_float
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Allow external connections