import pandas as pd

# Load your dataset
file_path = "dataset_farming/market_researcher_dataset.csv"
df = pd.read_csv(file_path)

print(df.head())