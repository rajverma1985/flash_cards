import pandas as pd

df = pd.read_csv("data/german_en.csv")
list_words = df.to_dict(orient="records")
