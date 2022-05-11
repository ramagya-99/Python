import pandas as pd
import numpy as np
file_loc = "C:/Users/ramag/Downloads/EWR_SQL.xlsx"
df = pd.read_excel(file_loc,sheet_name='Sheet1', usecols="C")
print(df)