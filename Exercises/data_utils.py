import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plt_nans(df):
	nan_counts = df.isna().sum()
	nan_counts = nan_counts[nan_counts > 0]
	sns.barplot(x=nan_counts.index, y=nan_counts.values, hue=nan_counts.index, palette=sns.color_palette("blend:#00D9FF,#D2FF61", n_colors=len(nan_counts.index)), alpha=0.7)
	plt.show()

def type_mask(df):
	mask = pd.DataFrame()
	for col in df.columns:
		mask[col] = df[col].apply(lambda x: type(x))
	return mask

def uniques(df):
	for col in df.columns:
		print(f"{col} : {df[col].unique()}")

def sns_theme(hue_length):
	'''
	returns my personal palette and alpha
	hue_length is the number of unique values in defined hue argument for seaborn (integer)
	'''
	alpha = 0.7
	return alpha, sns.color_palette("blend:#00D9FF,#D2FF61", n_colors=hue_length)