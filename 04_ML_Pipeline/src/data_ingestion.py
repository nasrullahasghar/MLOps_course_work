import os
import logging
import pandas as pd
from sklearn.model_selection import train_test_split

# Ensure the 'logs' directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logger = logging.getLogger("data_ingestion")
logger.setLevel(logging.DEBUG) 

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

log_file_path = os.path.join(log_dir, "data_ingestion.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_data(data_url: str) -> pd.DataFrame:
    """Load the Data from CSV file"""
    try:
        df = pd.read_csv(data_url) 
        logger.debug("Data loaded successfully from %s", data_url)
        return df
    except pd.errors.ParserError as e:
        logger.error("Failed to parse the CSV file: %s", e)
        raise
    except Exception as e:
        logger.error("Unexpected error occurred while loading the data: %s", e)
        raise

def data_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    """Clean, rename, and deduplicate data"""
    try:
        df = df.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], errors='ignore')
        df = df.rename(columns={"v1": "target", "v2": "text"})
        df = df.drop_duplicates(keep='first')
        logger.debug("Data Preprocessing completed")
        return df
    except KeyError as e:
        logger.error("Missing expected column in the dataframe: %s", e)
        raise
    except Exception as e:
        logger.error("Unexpected error occurred during preprocessing: %s", e)
        raise

def save_data(train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str) -> None:
    """Save the train and test dataset"""
    try:
        raw_data_path = os.path.join(data_path, "raw")
        os.makedirs(raw_data_path, exist_ok=True)
        
        train_data.to_csv(os.path.join(raw_data_path, "train.csv"), index=False)
        test_data.to_csv(os.path.join(raw_data_path, "test.csv"), index=False)
        logger.debug("Train and Test data saved to %s", raw_data_path)
    except Exception as e:
        logger.error("Unexpected error occurred while saving the data: %s", e)
        raise

def main():
    try:
        test_size = 0.2
        data_path = "https://raw.githubusercontent.com/vikashishere/Datasets/main/spam.csv"
        df = load_data(data_url=data_path)
        final_df = data_preprocessing(df)
        train_data, test_data = train_test_split(final_df, test_size=test_size, random_state=42)
        save_data(train_data, test_data, data_path="./data")
    except Exception as e:
        logger.error("Failed to complete the data ingestion step: %s", e)

if __name__ == "__main__":
    main()
