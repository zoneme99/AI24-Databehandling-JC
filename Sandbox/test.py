import pandas as pd
import seaborn as sns
import context
import matplotlib.pyplot as plt
from IPython.display import display
from Exercises import data_utils as du
import numpy as np

#import plotly_express as px


titanic = sns.load_dataset("titanic")
group = titanic.groupby(["class","sex"], observed=False)[['age','fare']].mean()
group1 = titanic.groupby("class", observed=False)[['age','fare']].mean()

mask = du.type_mask(titanic)
du.uniques(mask)
print(titanic[mask['age'] == float])
print(mask.head())