import os
import urllib.request as request
import zipfile
from textSummerizer.logging import logger
from textSummerizer.utils.common import get_size
from textSummerizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
            localdir = os.path.dirname(self.config.local_data_file)
            os.makedirs(localdir,exist_ok=True)
            if not os.path.exists(self.config.local_data_file):
                filename,headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename = self.config.local_data_file
                )
                logger.info(f"{filename} download with following info: \n{headers}")
            else:
                logger.info(f"file already exists of size{get_size(Path(self.config.local_data_file))}")
        
    def extract_zip_file(self):
            ''''zip_file_path:str
                Extract zip file into the data directory
                Function returns None'''
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            if not zipfile.is_zipfile(self.config.local_data_file):
                raise Exception("Downloaded file is not a valid zip file.")

            with zipfile.ZipFile(self.config.local_data_file,"r") as zip:
                    zip.extractall(unzip_path)