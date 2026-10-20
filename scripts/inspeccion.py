# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total
import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
ventas["ticket"] = ventas["ventas"]/ventas["clientes"]
print(ventas.head())

print("Sucursal con mayo venta: ",
      ventas.loc[ventas["ventas"].idxmax(), "sucursal"])
print("Sucursal con menor venta: ", ventas.loc[ventas["ventas"].idxmin(), "sucursal"])
ventas_por_region = ventas.groupby("region")["ventas"].sum()
ventas_por_region.head()
print( ventas_por_region.idxmax())