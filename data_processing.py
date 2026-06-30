import os
import pandas as pd

DATA_DIR = "./data"

dfs = []

for file in os.listdir(DATA_DIR):
    dfs.append(pd.read_csv(os.path.join(DATA_DIR,file)))
    
df = pd.concat(dfs)

print(f"After concat: \n {df.info()}")

df = df[df['product'] == 'pink morsel']

df["price"] = df["price"].replace(r"[$]", "", regex = True).astype(float)


df["sales"] = df["price"] * df["quantity"]

df = df.loc[:, ["sales", "date", "product"]]

df.to_csv("formatted_data.csv", index = False)