from textSummerizer.entity import DataTransformationConfig
from textSummerizer.logging import logger
import os
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk


class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        
    
    def convert_examples_to_features(self,example_batch):
        input_embeddings = self.tokenizer(example_batch['dialogue'],max_length=1024,truncation=True)
        with self.tokenizer.as_target_tokenizer():
            target_embeddings = self.tokenizer(example_batch['summary'],max_length=128,truncation=True)
        return{
            'input_ids': input_embeddings['input_ids'],
            'attention_mask': input_embeddings['attention_mask'],
            'labels': target_embeddings['input_ids']
        }
        
    def convert(self):
        data_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = data_samsum.map(self.convert_examples_to_features,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))