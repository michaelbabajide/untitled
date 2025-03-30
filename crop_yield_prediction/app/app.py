import pandas as pd
import pickle
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
app.logger.info("Application starting up")

# Load model and preprocessing pipeline
MODEL_PATH = '/workspaces/untitled/crop_yield_prediction/app/model/best_crop_yield_model.pkl'
PIPELINE_PATH = '/workspaces/untitled/crop_yield_prediction/app/model/crop_yield_preprocessing_pipeline.pkl'

# Load model and pipeline using pickle instead of joblib
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

with open(PIPELINE_PATH, 'rb') as pipeline_file:
    pipeline = pickle.load(pipeline_file)

@app.route('/predict', methods=['POST'])
def predict_crop_yield():
    try:
        # Get input data from request
        input_data = request.json
        
        # Create DataFrame from input
        df = pd.DataFrame([input_data])
        
        # Preprocess the data
        processed_data = pipeline.transform(df)
        
        # Make prediction
        prediction = model.predict(processed_data)
        
        # Return prediction
        return jsonify({
            'predicted_yield': float(prediction[0]),
            'units': 'tons per hectare'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696, debug=True)