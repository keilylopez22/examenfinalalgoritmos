import sys
import os
import openpyxl

libro = openpyxl.load_workbook("datos2.xlsx")
hoja = libro["listado"]

hoja['A1'].value = "codigo"
hoja['B1'].value = "marca"
hoja['C1'].value = "modelo"
hoja['D1'].value = "precio"
hoja['E1'].value = "kilometraje"
hoja['F1'].value = "cantidad fotos"

libro.save("datos2.xlsx")