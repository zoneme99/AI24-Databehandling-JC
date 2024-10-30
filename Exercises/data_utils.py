import pandas as pd
import matplotlib.pyplot as plt

def plt_nans(df):
    nan_counts = df.isna().sum()
    nan_counts = nan_counts[nan_counts > 0]  # Keep only columns with NaNs
    nan_counts.plot(kind='bar', title='Number of NaNs per Column', color=plt.cm.tab20(range(len(nan_counts))))

def type_mask(df):
	mask = pd.DataFrame()
	for col in df.columns:
		mask[col] = df[col].apply(lambda x: type(x))
	return mask

def uniques(df):
	for col in df.columns:
		print(f"{col} : {df[col].unique()}")