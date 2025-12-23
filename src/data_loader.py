import pandas as pd

class DataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()
        req_cols = {'Name', 'Genres', 'sypnopsis'}
        missing_cols = req_cols - set(df.columns)
        if missing_cols:
            raise ValueError("Missing Required Columns in the CSV file.")
        df['Info'] = (
            "Title:" + df['Name'] + "Overview" + df['sypnopsis'] + "Genres:" + df['Genres']
        )

        df[['Info']].to_csv(self.processed_csv, encoding='utf-8', index=False)
        return self.processed_csv