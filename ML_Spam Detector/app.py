from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and vectorizer
classifier = joblib.load('spam_classifier.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Ensure the request content type is application/json
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    json_input = request.get_json()

    # Ensure 'message' key is in JSON
    if 'message' not in json_input:
        return jsonify({"error": "JSON must include a 'message' key"}), 400

    message = json_input['message']

    # Check if the message is empty
    if not message.strip():
        return jsonify({"error": "Message cannot be empty"}), 400

    # Process the message with the ML model
    message_vect = vectorizer.transform([message])
    prediction = classifier.predict(message_vect)

    return jsonify({'prediction': 'spam' if prediction[0] == 1 else 'not spam'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all public IPs
