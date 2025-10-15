from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet

system_meters_tx16 = ['3.510 V', '3.509 V', '3.385 V', '0.267 V', '3.502 V']
system_meters_tx17 = ['3.512 V', '3.508 V', '3.380 V', '0.257 V', '3.509 V']
drive_chain_tx_16 = ['113.2%', '100.9%', '49.5V', '19.6A']
drive_chain_tx_17 = ['115.0%', '95.5%', '47.1V', '17.9A']
system_cooling_tx16 = ['25.9 C', '16.4', '19.2', '16.6', '25.9 C']
system_cooling_tx17 = ['25.6 C', '15.3', '16.9', '14.4', '25.3 C']
power_amps_tx16 = ['PA 1:', '101.4 %', '49.6 V', '23.2 A', '43.8 C',
                   'PA 2:', '100.4 %', '49.5 V', '21.6 A', '42.2 C',
                   'PA 3:', '99.2 %', '49.2 V', '21.4 A', '40.8 C',
                   'PA 4:', '102.8 %', '49.2 V', '21.3 A', '39.2 C',
                   'PA 5:', '99.5 %', '49.4 V', '21.4 A', '41.9 C',
                   'PA 6:', '97.2 %', '49.6 V', '21.6 A', '38.3 C']
power_amps_tx17 = ['PA 1:', '99.3 %', '47.5 V', '23.9 A', '40.4 C',
                   'PA 2:', '100.6 %', '47.6 V', '20.7 A', '38.2 C',
                   'PA 3:', '99.1 %', '47.6 V', '20.5 A', '34.6 C',
                   'PA 4:', '100.4 %', '47.6 V', '20.6 A', '38.6 C',
                   'PA 5:', '99.8 %', '47.4 V', '19.4 A', '37.3 C',
                   'PA 6:', '104.7 %', '47.4 V', '20.4 A', '38.2 C']

power_amps_tx16PA = []
power_amps_tx16_power = []
power_amps_tx16V = []
power_amps_tx16A = []
power_amps_tx16C = []
tx16PowerAmpsList = [power_amps_tx16PA,power_amps_tx16_power,power_amps_tx16V,power_amps_tx16A,power_amps_tx16C]

for cont, lista in enumerate(tx16PowerAmpsList):
    for idx, valor in enumerate(power_amps_tx16):
        if (idx - cont) % 5 == 0:
            lista.append(valor)
    cont +=1
    print(lista)

power_amps_tx17PA = []
power_amps_tx17_power = []
power_amps_tx17V = []
power_amps_tx17A = []
power_amps_tx17C = []
tx17PowerAmpsList = [power_amps_tx17PA,power_amps_tx17_power,power_amps_tx17V,power_amps_tx17A,power_amps_tx17C]

for cont, lista in enumerate(tx17PowerAmpsList):
    for idx, valor in enumerate(power_amps_tx17):
        if (idx - cont) % 5 == 0:
            lista.append(valor)
    cont +=1
    print(lista)

system_meters_list = [
    'Power Ctrl Ref',
    'APC Reference',
    'APC Output',
    'Foldback Level',
    'Fordward Sample']

drive_chain_list = [
    'Module RF Out',
    'Module Input',
    'Input Voltage',
    'Total Current']

system_cooling_list = [
    'Coolant Temp',
    'Flow Rate',
    'Inlet Press',
    'Oulet Press',
    'Air Temp-Front']
#
#    POWER AMPS:
#        #####   PWR OUT%    VOLTS   AMPS    TEMP°C
#          PA1
#          PA2
#          PA3
#          PA4
#          PA5
#          PA6

grupos1 = [
    (system_meters_list, system_meters_tx16, system_meters_tx17,['System meters','Canal 16', 'Canal 17']),
    (drive_chain_list, drive_chain_tx_16, drive_chain_tx_17, ['Drive chain','Canal 16', 'Canal 17']),
    (system_cooling_list, system_cooling_tx16, system_cooling_tx17, ['System cooling','Canal 16', 'Canal 17']),
    ]

grupos2 = [
    (power_amps_tx16PA, power_amps_tx16_power, power_amps_tx16V, power_amps_tx16A, power_amps_tx16C,['','PWR OUT%','VOLTS','AMPS','TEMP °C']),
    (power_amps_tx17PA, power_amps_tx17_power, power_amps_tx17V, power_amps_tx17A, power_amps_tx17C,['','PWR OUT%','VOLTS','AMPS','TEMP °C'])
]

#Creacion de PDF
pdf = SimpleDocTemplate('reporte_mediciones.pdf', pagesize=letter)
estilos = getSampleStyleSheet()
contenido = []

# Estilo de tabla
estilo_tabla = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
])

for lista1, lista2, lista3, headers in grupos1:
    #crear tabla
    data = [headers]
    for i in range(len(lista1)):
        data.append([lista1[i], lista2[i], lista3[i]])

    tabla = Table(data)
    tabla.setStyle(estilo_tabla)

    #Agregar tabla y espacio
    contenido.append(tabla)
    contenido.append(Spacer(1,15))

for lista1, lista2, lista3, lista4, lista5, headers in grupos2:
    #crear tabla
    data = [headers]
    for i in range(len(lista1)):
        data.append([lista1[i], lista2[i], lista3[i], lista4[i], lista5[i]])

    tabla = Table(data)
    tabla.setStyle(estilo_tabla)

    #agregar tabla y espacio
    contenido.append(tabla)
    contenido.append(Spacer(1, 15))

#Generar PDF
pdf.build(contenido)
print("PDF generado correctamente: reporte_mediciones.pdf")