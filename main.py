# Oasis Task 2
# Arif Shaikh

# Using pandas profiling to get an overview of dataset

import pandas as pd
from pandas_profiling import ProfileReport
csv_path = r"C:\Users\arif shaikh\Downloads\oasis\task2\Unemployment_Rate_upto_11_2020.csv"

df = pd.read_csv(csv_path)
print(df)


profile = ProfileReport(df)
# profile = ProfileReport(df, minimal=True)
profile.to_file(output_file='unemploy1.html')