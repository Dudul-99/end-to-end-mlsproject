import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logger
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

def run_pipeline():
    try:
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()
        
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
        
        modeltrainer = ModelTrainer()
        result = modeltrainer.initiate_model_trainer(train_arr, test_arr)
        print(result)
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")