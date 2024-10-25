import pandas as pd

def print_cols_unique(df, blacklist=[]):
    for col in df.columns:
        if col not in blacklist:
            print(col, df[col].unique())