import pandas as pd
import os

class DataLoader:
    def __init__(self, base_path='dataset_farming'):
        self.base_path = base_path

    def load_farmer_data(self):
        """
        Load and preprocess the farmer advisor dataset.
        """
        path = os.path.join(self.base_path, 'farmer_advisor_dataset.csv')
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} does not exist.")

        df = pd.read_csv(path)
        df.dropna(inplace=True)
        df.columns = df.columns.str.strip().str.lower()
        return df

    def load_market_data(self):
        """
        Load and preprocess the market researcher dataset.
        """
        path = os.path.join(self.base_path, 'market_researcher_dataset.csv')
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} does not exist.")

        df = pd.read_csv(path)
        df.dropna(inplace=True)
        df.columns = df.columns.str.strip().str.lower()
        return df
