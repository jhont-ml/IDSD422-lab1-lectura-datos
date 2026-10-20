# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total
library(readr)
ventas = read_csv("data/ventas.csv")
head(ventas)

str(ventas)
ventas$ticket = ventas$ventas / ventas$clientes
print(paste("Sucursal con mayo venta: ", ventas$sucursal[which.max(ventas$ventas)]))
print(paste("Sucursal con menor venta: ", ventas$sucursal[which.min(ventas$ventas)]))

ventas_por_region = aggregate(ventas ~ region, data = as.data.frame(ventas), FUN = sum)
head(ventas_por_region)

print(paste( ventas_por_region$region[which.max(ventas_por_region$ventas)]))