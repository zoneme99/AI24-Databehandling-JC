import pandas as pd

df = pd.DataFrame({'A':["hej", "på", "dig", "ok",'no'], 'B':[6, 7, 8, 9, 10], 'C':[11, 12, 13, 14, 15]})
df1 = pd.DataFrame({'A':["hej", "på", "dig", "ok",'no'], 'B':[11, 12, 13, 14, 15], 'C':[11, 12, 13, 14, 15]})

new = pd.concat([df,df1])
result = new.groupby('A').apply(lambda x: (x['B'] - x['B']) / (x['B'] + x['B']))
#TODO Above function doesnt work, I want the duplicate of B to make operation with first B
print(result)
