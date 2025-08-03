import os
import sys
import pandas as pd
import numpy as np
import dill
from sklearn.metrics import r2_score

from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save an object to a file using pickle.
    """
    import pickle
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train)  # Train the model
            y_train_pred = model.predict(X_train)  # Predict on training data

            y_test_pred = model.predict(X_test)  # Predict on test data
            train_model_score = r2_score(y_train, y_train_pred)  # Calculate R2
            test_model_score = r2_score(y_test, y_test_pred)  # Calculate R2

            # Store the score
            report[list(models.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
