from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
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

system_meters_list = [
    'Power Ctrl Ref',
    'APC Reference',
    'APC Output',
    'Foldback Level',
    'Fordward Sample'
    ]

drive_chain_list = [
    'Module RF Out',
    'Module Input',
    'Input Voltage',
    'Total Current'
    ]

system_cooling_list = [
    'Coolant Temp',
    'Flow Rate',
    'Inlet Press',
    'Oulet Press',
    'Air Temp-Front'
    ]
#
#    POWER AMPS:
#        #####   PWR OUT%    VOLTS   AMPS    TEMP°C
#          PA1
#          PA2
#          PA3
#          PA4
#          PA5
#          PA6

grupos = [
    ('System meters', system_meters_tx16, system_meters_tx17,['Canal 16', 'Canal 17']),
    ('Drive Chain', drive_chain_tx_16, drive_chain_tx_17, ['Canal 16', 'Canal 17']),
    ('System Cooling', system_cooling_tx16, system_cooling_tx17, ['Canal 16', 'Canal 17'])

]