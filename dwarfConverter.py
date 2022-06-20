import csv
import pandas as pd

df = pd.read_csv("dwarfStars(Pre).csv")
df = df.dropna()
df["Radius"] = 0.102763*df["Radius"]
df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]

df.head()
df.reset_index(drop=True,inplace=True)
df.to_csv("convertedDwarfStars.csv")