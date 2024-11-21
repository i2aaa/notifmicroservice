# Notification Microservice

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    if not data or 'user_id' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    # Generate a notification
    notification = {
        'user_id': data['user_id'],
        'message': 'Don’t forget to take a moment to breathe today!',
        'timestamp': '2024-11-18T12:00:00Z'
    }
    return jsonify(notification), 200


if __name__ == '__main__':
    app.run(port=5000)
