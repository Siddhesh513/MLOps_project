from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import time

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Disable caching more aggressively


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers["Last-Modified"] = time.strftime(
        '%a, %d %b %Y %H:%M:%S GMT')
    return response

# Home page route


@app.route('/')
def index():
    return render_template('index.html')

# Form submission route - shows results page


@app.route('/predict', methods=['GET', 'POST'])
def predict_score():
    print(f"Request method: {request.method}")
    print(f"Request URL: {request.url}")

    if request.method == 'GET':
        print("Handling GET request")
        return render_template('index.html')
    else:
        print("Handling POST request")
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get(
                    'parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get(
                    'test_preparation_course'),
                reading_score=float(request.form.get('writing_score')),
                writing_score=float(request.form.get('reading_score'))
            )

            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before prediction")

            predict_pipeline = PredictPipeline()
            print("Mid prediction")
            results = predict_pipeline.predict(pred_df)
            print("After prediction")
            # Format result to 2 decimal places
            formatted_result = round(float(results[0]), 2)
            print(f"Predicted result: {formatted_result}")

            # Render results page with prediction
            return render_template('results.html', results=formatted_result)

        except Exception as e:
            print(f"Error during prediction: {e}")
            return render_template('results.html', error="An error occurred during prediction. Please check your inputs.")

# Debug route to catch any other requests


@app.route('/debug')
def debug():
    return "Debug route working!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
