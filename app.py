from flask import Flask, render_template, request, jsonify
import requests
import logging
import os
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('whiteboard')

app = Flask(__name__, static_folder="static")

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'whiteboards.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tenor-proxy')
def tenor_proxy():
    search = request.args.get('q', '')
    api_key = request.args.get('key', '')
    limit = request.args.get('limit', 12)

    if not search or not api_key:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        response = requests.get(
            "https://api.tenor.com/v1/search",
            params={"q": search, "key": api_key, "limit": limit},
            timeout=10
        )
        if response.status_code != 200:
            return jsonify({"error": f"Tenor API error: {response.status_code}"}), response.status_code
        result = response.json()
        return jsonify(result)
    except Exception as e:
        logger.error(f"Tenor proxy error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/whiteboard', methods=['GET', 'POST'])
def user_whiteboard():
    user_id = request.args.get('userId') or request.json.get('userId')
    if not user_id:
        return jsonify({'error': 'userId required'}), 400

    # Load existing data
    if not os.path.exists(os.path.dirname(DATA_FILE)):
        os.makedirs(os.path.dirname(DATA_FILE))

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            whiteboards = json.load(f)
    else:
        whiteboards = {}

    if request.method == 'GET':
        # Return user-specific data if it exists
        return jsonify(whiteboards.get(user_id, {}))

    if request.method == 'POST':
        data = request.json
        elements = data.get('elements', [])
        # Save or update user data
        whiteboards[user_id] = {'elements': elements}
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(whiteboards, f, ensure_ascii=False, indent=2)
        return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')