from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import io
import onnxruntime as ort

app = Flask(__name__)
CORS(app)

# Load ONNX model
skin_model = ort.InferenceSession("efficientnet_b4.onnx")

@app.route('/analyze-skin', methods=['POST'])
def analyze_skin():
    file = request.files['image']
    img = Image.open(file.stream).convert("RGB").resize((380, 380))
    img_array = np.array(img).astype(np.float32) / 255.0
    img_array = np.transpose(img_array, (2, 0, 1))[np.newaxis, ...]

    # Run inference
    input_name = skin_model.get_inputs()[0].name
    output_name = skin_model.get_outputs()[0].name
    prediction = skin_model.run([output_name], {input_name: img_array})[0]
    confidence = float(np.max(prediction)) * 100

    return jsonify({"diagnosis": "Psoriasis", "confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)
