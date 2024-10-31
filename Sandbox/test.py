import pandas as pd
import seaborn as sns
import context
import matplotlib.pyplot as plt
from IPython.display import display
from Exercises import data_utils as du

#import plotly_express as px


titanic = sns.load_dataset("titanic")
group = titanic.groupby(["class","sex"])[['age','fare']].mean()
group1 = titanic.groupby("class")[['age','fare']].mean()

alpha, pal = du.sns_theme(len(group1['age'].unique()))

sns.histplot(data=group1, x="age", hue="age", palette=pal, alpha=alpha)
plt.show()

