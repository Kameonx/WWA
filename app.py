from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__, static_folder="static")

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

if __name__ == '__main__':
    app.run(debug=True)