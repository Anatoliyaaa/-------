from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "ESB is running!", 200

@app.route('/seb', methods=['GET'])
def seb():
    return "This is the /seb route"

# Эмуляция ESB (Enterprise Service Bus)
@app.route('/esb', methods=['POST'])
def esb():
    data = request.json
    service = data.get("service")
    payload = data.get("payload", {})

    service_urls = {
        "order": "http://localhost:5001/order",
        "payment": "http://localhost:5002/payment",
        "notification": "http://localhost:5003/notification"
    }

    if service in service_urls:
        if service not in service_urls:
            return {"error": f"Service '{service}' not found"}, 400
        response = requests.post(service_urls[service], json=payload)
        #response = requests.get("http://localhost:5001/"+service)
        return response.json(), response.status_code
    else:
        return jsonify({"error": "Unknown service"}), 400

if __name__ == "__main__":
    app.run(port=5000, debug=True)
