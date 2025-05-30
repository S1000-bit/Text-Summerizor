from textSummerizer.config.configuration import ConfigurationManger
from textSummerizer.components.data_transformation import DataTransformation
from textSummerizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        config =ConfigurationManger()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()