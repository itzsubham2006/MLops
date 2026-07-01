import logging
from sklearn.model_selection import train_test_split
import os
import pandas as pd


log_dir = 'logs'

os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'data_ingestion.log')

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load(data_url: str) -> pd.DataFrame:
    """Load data from csv files"""
    
    try: 
        df = pd.read_csv(data_url)
        logger.debug('Data is loaded from %s', data_url)
        return df
    
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the csv file: %s', e)
        raise
    
    except Exception as e:
        logger.error('Unexpected error occured from file : %s', e)
        raise
    
    
    
def preprocess_data(df : pd.DataFrame) -> pd.DataFrame:
    
    """Data preprocessing"""
    
    try:
        
        df.rename(columns={'v2': 'text', 'v1': 'target'}, inplace=True)
        logger.debug('Data preprocessing in process..')
        return df
    
    except KeyError as e:
        
        logger.error('Missing column in the dataframe : %s', e)
        raise
        
    except Exception as e:
        
        logger.error('Unexpected error occurred..!')
        raise
    
    
    
def save_data(train_data : pd.DataFrame, test_data : pd.DataFrame, data_path : str) -> None:
    
    """Saving the train data and test data"""
    
    try:
        raw_data_path = os.path.join(data_path, 'raw')
        
        os.makedirs(raw_data_path, exist_ok=True)
        
        train_file_path = os.path.join(raw_data_path, "train.csv")
        test_file_path = os.path.join(raw_data_path, "test.csv")

        train_data.to_csv(train_file_path, index=False)
        test_data.to_csv(test_file_path, index=False)
        
        logger.debug('Train and test data saved successfully to %s', raw_data_path)
        
    except Exception as e:
        logger.error('Unexpected error while saving the data : %s', e)
        raise
        
        
def main():
    
    try:
        test_size = 0.2
        data_path = 'https://raw.githubusercontent.com/vikashishere/Datasets/refs/heads/main/spam.csv'
        df = load(data_url=data_path)
        final_df = preprocess_data(df)
        train_data, test_data = train_test_split(final_df, test_size=test_size, random_state=2)
        save_data(train_data, test_data, data_path='./data')
        
    except Exception as e:
        
        logger.error('Failed to complete the ingestion process : %s', e)
        print(f'Error {e}')
        
if __name__ == '__main__':
    main()