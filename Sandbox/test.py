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

pal = sns.color_palette(("#00d9ff","#0bdbf7","#16ddee","#21dfe6","#2ce1de","#37e3d5","#42e5cd","#4de7c5","#58e9bc","#63ebb4","#6fedac","#7aefa4","#85f19b","#90f393","#9bf58b","#a6f782","#b1f97a","#bcfb72","#c7fd69","#d2ff61"))

sns.histplot(data=group1, x="age", hue="age",  palette=pal, alpha=0.7)
plt.show()

