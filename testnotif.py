import requests


def test_notification_service():
    # URL for the microservice
    url = "http://127.0.0.1:5000/notify"

    # Data to send in the request
    payload = {'user_id': 123}

    # Make a POST request
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        # Display the data received
        print("Notification received:")
        print(response.json())
    else:
        print("Error:", response.status_code, response.text)


if __name__ == '__main__':
    test_notification_service()
