from textSummerizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
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