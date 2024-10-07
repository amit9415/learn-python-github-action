import pandas as pd
df = pd.read_csv("day.csv")
df.to_parquet("day.parquet")