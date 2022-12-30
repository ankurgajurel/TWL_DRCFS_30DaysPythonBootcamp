from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []


@app.route('/receive', methods=['GET'])
def receive():
    return jsonify({"messages": messages})


@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    messages.append(message)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=9999)
