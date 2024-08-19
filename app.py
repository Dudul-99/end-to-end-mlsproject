from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.train_pipeline import CustomData, PredictPipeline
from src.logger import logger  # Importez votre logger ici



application = Flask(__name__)
app = application

## Route for a home page
@app.route('/')
def index():
    logger.info('Accessed home page')
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    logger.info('Received a request to /predictdata')
    if request.method == 'GET':
        logger.info('GET request to /predictdata - rendering home.html')
        return render_template('home.html')
    else:
        logger.info('POST request to /predictdata - processing data')
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('writing_score')),
                writing_score=float(request.form.get('reading_score'))
            )
            pred_df = data.get_data_as_data_frame()
            logger.info(f'Input data frame: {pred_df}')
            
            logger.info('Initializing prediction pipeline')
            predict_pipeline = PredictPipeline()
            
            logger.info('Making prediction')
            results = predict_pipeline.predict(pred_df)
            
            logger.info(f'Prediction completed. Result: {results[0]}')
            return render_template('home.html', results=results[0])
        except Exception as e:
            logger.error(f'An error occurred during prediction: {str(e)}')
            return render_template('home.html', error="An error occurred during prediction.")

'''
This is the port 
http://localhost:5001/predictdata
, debug=True
'''
if __name__ == "__main__":
    logger.info('Flask app is starting')
    app.run(host="0.0.0.0", port=5001)
