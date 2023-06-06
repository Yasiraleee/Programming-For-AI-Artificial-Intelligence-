import pandas as pd
data = {'Name': ['', 'Ali', 'Ahmed', 'Nida', ''],'Field': ['C', 'E', 'E', 'C', 'C'], 'Age': [None, None, None, None, None], 'Marks': [-90, 60, -10, 70, 75]}
f = pd.DataFrame(data)
f = f.dropna(axis=1)
f.replace('', '---', inplace=True)
f['Field'].replace(['C', 'E'], [0, 1], inplace=True)
t = (60+70+75)/3
for x in f.index:
    if f.loc[x,'Marks']<0:
        f.loc[x, 'Marks'] = t


print(f)