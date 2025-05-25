from textSummerizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from textSummerizer.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from textSummerizer.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
from textSummerizer.pipeline.stage_4_model_trainer import ModelTrainingPipeline
from textSummerizer.logging import logger

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} ...... Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} ...... Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{STAGE_NAME} ...... Completed")
except Exception as e:
    logger.exception(e)
    raise e

'''STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"{STAGE_NAME} ...... Completed")
except Exception as e:
    logger.exception(e)
    raise e''''