from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os
import logging

app = Flask(__name__)

# Set the basic configuration for the logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])  # Ensures logging to console

app.logger.setLevel(logging.INFO)
app.logger.info("Logging is set up.")

# Base Path from environment variable or default
base_path = os.getenv('BASE_PATH', './')

import os
print("Current Working Directory:", os.getcwd())

# Load the models
model_01 = joblib.load(os.path.join(base_path, 'Model 01 Pipeline.pkl'))
model_02 = joblib.load(os.path.join(base_path, 'Model 02 Pipeline.pkl'))
target_encoder = joblib.load(os.path.join(base_path, 'Model 02 Dependencies', 'Target Encoder.pkl'))

def preprocess_data(items):
    """
    This function preprocesses the data before making predictions.
    
    Parameters:
    - items: A list of dictionaries representing the food items with their corresponding features.
    
    Returns:
    - df: A DataFrame containing the preprocessed data.
    - original_food_names: A list of the original food names before preprocessing.
    """
    # Convert the items into a DataFrame
    df = pd.DataFrame(items)
    
    # Check if the 'Food' column exists in the DataFrame
    if 'Food' in df.columns:
        # Replace any missing values in the 'Food' column with the string 'Unknown'
        df['Food'] = df['Food'].fillna('Unknown')
        
        # Convert the values in the 'Food' column to strings
        df['Food'] = df['Food'].astype(str)
        
        # Store the original food names before preprocessing
        original_food_names = df['Food'].tolist()
        
        # Use the target encoder to transform the 'Food' column
        df['Food'] = target_encoder.transform(df[['Food']])
        
    else:
        # If the 'Food' column does not exist, return an empty DataFrame and an empty list
        df = pd.DataFrame()
        original_food_names = []
    
    # Return the preprocessed DataFrame and the original food names
    return df, original_food_names

@app.route('/predict_model_01', methods=['POST'])
def predict_model_01():
    try:
        # Get the JSON data from the request
        data = request.json
        # Convert the data into a DataFrame
        df = pd.DataFrame([data])
        # Make a prediction using the model
        prediction = model_01.predict(df)
        # Map the predicted values to their corresponding labels
        # The prediction returned by the model is a 1D array of shape (1, 3),
        # where the first dimension (1) represents the batch size and the
        # second dimension (3) represents the number of classes.
        # We convert the array into a list and select the first element of
        # the array to get the predicted values for the three classes.
        labeled_prediction = {
            "carbs%": float(prediction[0][0]),
            "fats%": float(prediction[0][1]),
            "proteins%": float(prediction[0][2])
        }
        # Return the prediction as JSON response
        return jsonify({'prediction': labeled_prediction})
    except Exception as e:
        # Log any errors that occur during the processing of the request
        logging.error(f"Error in predict_model_01: {e}")
        # Return an error message if there is an error
        return jsonify({"error": "Error processing request"}), 500

@app.route('/predict_model_02', methods=['POST'])
def predict_model_02():
    """
    This function handles the '/predict_model_02' route and predicts food items
    using the model_02. It expects a JSON payload with multiple categories and
    their corresponding food items. The function preprocesses the data, makes
    predictions using the model_02, and returns the results as a JSON response.
    """
    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)
        
        # Initialize an empty dictionary to store the results
        results = {}
        
        # Iterate over each category and its corresponding food items
        for category, items in data.items():
            
            # Preprocess the data and get the transformed data and original food names
            df, original_food_names = preprocess_data(items)
            
            # Make predictions using the model_02 and store them in a variable
            predictions = model_02.predict(df)
            
            # Store the predictions and original food names in the results dictionary
            results[category] = {
                "predictions": predictions.tolist(), # Convert predictions to a list
                "food_names": original_food_names # Store the original food names
            }
        
        # Return the results as a JSON response
        return jsonify(results)
    
    except Exception as e:
        # Log any errors that occur during the processing of the request
        logging.error(f"Error in predict_model_02: {e}")
        
        # Return an error message if there is an error
        return jsonify({"error": "Error processing request"}), 500

if __name__ == '__main__':
    port = os.getenv('PORT', 5000)
    app.run(debug = False, host='0.0.0.0', port=port)


