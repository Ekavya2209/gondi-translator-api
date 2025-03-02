from flask import Flask, request, jsonify  # Flask के ज़रूरी मॉड्यूल इंपोर्ट करें
import os

app = Flask(__name__)

# Sample Gondi translation data (Replace with real data or a model)
gondi_translations = {
    "hello": "नमस्ते",
    "how are you": "तुम कुसल हुस",
    "good morning": "सुप्रभात",
    "thank you": "धन्यवाद"
}

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        text = data.get("text", "").lower()

        # Check if translation is available
        translation = gondi_translations.get(text, "Translation not found")

        return jsonify({"input": text, "translation": translation})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render का पोर्ट इस्तेमाल करें
    app.run(host="0.0.0.0", port=port)
