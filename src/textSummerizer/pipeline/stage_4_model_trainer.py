from textSummerizer.config.configuration import ConfigurationManger
from textSummerizer.components.model_trainer import ModelTrainer
from textSummerizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass 
    
    def main(self):
        config = ConfigurationManger()
        model_trainer_config =config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(model_trainer_config)
        model_trainer_config.train()