from flask import Flask, jsonify, request
import api_main as main  # import your refactored main script
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/receive-url', methods=['POST'])
def receive_url():
    try:
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({"error": "No URL provided"}), 400
        
        # Call your refactored main function that processes a URL
        results = main.process_url(url)
    except Exception as e:
        logger.exception("Failed to process URL.")  # This will log the full exception traceback
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"status": "success", "data": results}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
