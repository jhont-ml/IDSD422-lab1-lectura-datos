import pandas as pd
ventas = pd.read_excel("ventas.xlsx", sheet_name="ventas")
print(ventas.head())
print(ventas.shape)
print(ventas.dtypes)