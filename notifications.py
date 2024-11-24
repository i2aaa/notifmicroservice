# Notification Microservice

from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)


@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    if not data in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    # Extract 'user_id' pameter
    if 'user_id' not in data:
        return jsonify({'error': 'No user_id in request'}), 400
    else:
        user_id = data['custom_id']

    # Extract 'custom_message' parameter
    if 'custom_message' not in data:
        return jsonify({'error': 'No custom message in request'}), 400
    else:
        custom_message = data['custom_message']

    # Extract 'time' parameter
    if 'time' not in data:
        return jsonify({'error': 'No time in request'}), 400
    else: 
        time = data['time']
        try:
            parsed_time = datetime.fromisoformat(time.replace('Z', '+00:00'))
            if parsed_time < datetime.now(timezone.utc):
                return jsonify({'error': 'Invalid time: Time must be in the future'}), 400
        except ValueError:
            return jsonify({'error': 'Invalid time format. Use ISO 8601 (e.g., 2024-11-18T12:00:00Z)'}), 400

    # Generate a notification
    notification = {
        'user_id': user_id,
        'message': custom_message,
        'timestamp': time
    }
    
    return jsonify(notification), 200


if __name__ == '__main__':
    app.run(port=5000)
