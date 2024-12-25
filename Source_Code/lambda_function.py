import json
import boto3
import joblib
import numpy as np
from datetime import datetime
from io import BytesIO

# Initialize the S3 client
s3_client = boto3.client('s3')

# S3 bucket and folder details
BUCKET_NAME = 'projectkafkabucket'
MODEL_PATH = 'models/xgboost_model.joblib'
PREDICTIONS_FOLDER = 'predicted_data/'
BATCH_SIZE = 10

buffer = []

def load_model_from_s3():
    try:
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=MODEL_PATH)
        model_data = response['Body'].read()
        model = joblib.load(BytesIO(model_data))
        print("Model loaded successfully from S3.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e

def apply_model(model, batch):
    predictions = []
    for record in batch:
        features = record.get('features')
        if features:
            features_array = np.array(features).reshape(1, -1)  # Reshape for XGBoost
            prediction = model.predict(features_array)[0]  # Get the first prediction
            record['prediction'] = float(prediction)  # Add prediction to the record
            predictions.append(record)
    return predictions

def lambda_handler(event, context):
    global buffer
    try:
        model = load_model_from_s3()
        
        for record in event['Records']:
            payload = json.loads(record['kinesis']['data'])
            buffer.append(payload)
            
            if len(buffer) >= BATCH_SIZE:
                processed_data = apply_model(model, buffer)
                
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                file_name = f"{PREDICTIONS_FOLDER}predictions_{timestamp}.json"
                
                s3_client.put_object(
                    Bucket=BUCKET_NAME,
                    Key=file_name,
                    Body=json.dumps(processed_data, indent=2)
                )
                
                buffer = []
        
        return {
            'statusCode': 200,
            'body': json.dumps('Processed records successfully with predictions!')
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing records: {str(e)}")
        }

