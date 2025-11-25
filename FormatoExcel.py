import win32com.client as win32
import openpyxl

excel_file = "plantilla.xlsx"
salida_excel = "reporte.xlsx"
salida_pdf = "reporte.pdf"

# 1. Cargar plantilla y poner datos
wb = openpyxl.load_workbook(excel_file)
ws = wb.active

# Tus datos recolectados con Selenium
datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Carlos", 28, "CDMX"],
    ["Ana", 30, "Monterrey"]
]

# Insertarlos en la plantilla
fila_inicio = 5  # donde comienza tu tabla
col_inicio = 1
for i, fila in enumerate(datos):
    for j, valor in enumerate(fila):
        ws.cell(row=fila_inicio + i, column=col_inicio + j, value=valor)

wb.save(salida_excel)

# 2. Convertir ese Excel a PDF usando Excel real
excel = win32.Dispatch('Excel.Application')
excel.Visible = False

wb = excel.Workbooks.Open(salida_excel)
wb.ExportAsFixedFormat(0, salida_pdf)
wb.Close()
excel.Quit()

print("PDF generado:", salida_pdf)