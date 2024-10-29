import pandas as pd
import seaborn as sns
from IPython.display import display
import plotly_express as px


titanic = sns.load_dataset("titanic")
group = titanic.groupby(["class","sex"])[['age','fare']].mean()
group1 = titanic.groupby("class")[['age','fare']].mean()
display(group)
display(group1)
display(titanic.head())
