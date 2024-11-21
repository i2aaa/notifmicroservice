# Notification Microservice

## Overview
This microservice provides notifications for a mental health tracking application. It accepts a user ID via a POST request and responds with a custom notification message.

---

## Communication Contract

### 1. Requesting Data

To request data from the microservice, send a POST request to the `/notify` endpoint. The request must include a JSON payload with the following key:

- `user_id`: A unique identifier for the user (integer).

#### Example Request
Here's an example using Python's `requests` library:
```python
import requests

url = "http://127.0.0.1:5000/notify"
payload = {"user_id": 123}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())

### 2. Receiving Data 

The response from the microservice will be in JSON format. It will include the following keys:

- `user_id`: The ID of the user as provided in the request.
- `message`: A notification message.
- `timestamp`: The time when the notification was generated.

#### Example Response
Here's an example response received from the microservice:
```json
{
    "user_id": 123,
    "message": "Don’t forget to take a moment to breathe today!",
    "timestamp": "2024-11-18T12:00:00Z"
}
```

#### Parsing the Response in Python
Here's an example of how to parse the JSON response using Python:
```python
import requests

url = "http://127.0.0.1:5000/notify"
payload = {"user_id": 123}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Notification:", data["message"])
else:
    print("Error:", response.status_code)
```
---

## UML Sequence Diagram
Here is the UML sequence diagram that shows how requesting and receiving data works with the microservice.
```plaintext
+---------------------+             +---------------------+
| Requesting Program  |             | Notification        |
|                     |             | Microservice        |
+---------------------+             +---------------------+
         |                               |
         |      POST /notify (user_id)   |
         |-----------------------------> |
         |                               |
         | Validate request & generate   |
         | notification                  |
         | <-----------------------------|
         |                               |
         |    JSON Response (message,    |
         |       user_id, timestamp)     |
         | <-----------------------------|
         |                               |
```

---

## Running Microservice Locally
### 1. Install Dependencies:
```bash
pip install flask
```
[Flask Documentation](https://flask.palletsprojects.com/)

### 2. Run the microservice script:
```bash
python notifications.py
```

### 3. The microservice will be available locally at `http://127.0.0:5000`

### Additional Considerations

#### Assumptions
- The `user_id` will always be a valid integer.
- The microservice will run locally at `http://127.0.0:5000`.
- The requests must use JSON format and include the `Content-Type: application/json` header.

---

## Potential Issues
### 1. Invalid Requests:
- If the `user_id` is missing or invalid, the service will return error `400 Bad Request` with the following:
```json
{
"error": "Invalid data"
}
```

### 2. Network Connectivity:
- If you need to access the server from another device, simply modify the Flask `app.run` call as so:
```python

3. Dependencies:
- Ensure Flask is installed in your virtual environment:
```bash
pip install flask
```