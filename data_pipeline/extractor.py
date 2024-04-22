import os
from typing import List

import pandas as pd # type: ignore

def _get_all_files_from_dir(dir_path: str) -> List[str]:
    return [
                os.path.join(dir_path, file)
                for file in os.listdir(dir_path)
                if os.path.isfile(os.path.join(dir_path, file))
            ]

def _get_df_from_multiple_files(files: List[str]) -> List[pd.DataFrame]:
    return [pd.read_csv(file, low_memory=False) for file in files]

def get_all_data(*, leagues:List[str])-> pd.DataFrame:
    """Read all csv files from the raw directory and return a single DataFrame

    Returns:
        pd.DataFrame: A single DataFrame containing all the data from the csv files
    """
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    raw_csv_dir = os.path.join(curr_dir, 'raw')
    files = _get_all_files_from_dir(raw_csv_dir)

    df = pd.concat(_get_df_from_multiple_files(files), ignore_index=True)
    if leagues:
        df = df[df['league'].str.lower().isin([league.lower() for league in leagues])]
    return df
