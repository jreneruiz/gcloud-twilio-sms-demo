from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


client = Client("ACCOUNT_SID", "AUTH_TOKEN")
app = Flask(__name__)


@app.route('/messages', methods=['POST'])
def post_messages():
    to = request.json['to']
    message = request.json['message']
    try:
        client.messages.create(to=to, from_="TW_NUMBER", body=message)
    except TwilioRestException as e:
        return e
    return jsonify([{"response": "ok"}])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
