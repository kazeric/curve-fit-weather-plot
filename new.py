import pandas as pd

df = pd.read_csv()

df = df.drop('Region', axis=1)

df.to_csv('city_temp_new.csv', index=False)