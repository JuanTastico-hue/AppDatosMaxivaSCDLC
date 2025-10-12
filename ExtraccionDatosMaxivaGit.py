#       ___  ___  ___  ________  ________   _________  ________  ________  _________  ___  ________  ________
#      |\  \|\  \|\  \|\   __  \|\   ___  \|\___   ___\\   __  \|\   ____\|\___   ___\\  \|\   ____\|\   __  \
#      \ \  \ \  \\\  \ \  \|\  \ \  \\ \  \|___ \  \_\ \  \|\  \ \  \___|\|___ \  \_\ \  \ \  \___|\ \  \|\  \
#    __ \ \  \ \  \\\  \ \   __  \ \  \\ \  \   \ \  \ \ \   __  \ \_____  \   \ \  \ \ \  \ \  \    \ \  \\\  \
#   |\  \\_\  \ \  \\\  \ \  \ \  \ \  \\ \  \   \ \  \ \ \  \ \  \|____|\  \   \ \  \ \ \  \ \  \____\ \  \\\  \
#   \ \________\ \_______\ \__\ \__\ \__\\ \__\   \ \__\ \ \__\ \__\____\_\  \   \ \__\ \ \__\ \_______\ \_______\
#    \|________|\|_______|\|__|\|__|\|__| \|__|    \|__|  \|__|\|__|\_________\   \|__|  \|__|\|_______|\|_______|
#                                                                  \|_________|

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

def obtener_texto(by, selector, timeout=10):
    etiqueta = WebDriverWait(driver, timeout).until(ec.visibility_of_element_located((by, selector)))
    return etiqueta.text

def obtener_textos(by, selector, timeout=50):
    clases = WebDriverWait(driver, timeout).until(ec.presence_of_all_elements_located((by, selector)))
    return [elemento.text for elemento in clases]

def system_meters():
    #Listoooooo
    boton_system = driver.find_element(By.XPATH, "//a[@id='menuBtn5']")
    boton_system.click()
    time.sleep(4)
    boton_meters = driver.find_element(By.XPATH, "//a[@id='menuBtn2']")
    boton_meters.click()

    system_meters_datos= []
    '''
        datos guardados:
            Power Ctrl Ref
            APC Reference
            APC Output
            Foldback Level
            Fordward Sample
    '''

    ids = ['fax_sysmeter_pwrctrlref',
           'fax_sysmeter_apcref',
           'xt_sysmeter_apcoutput',
           'fax_sysmeter_foldback',
           'fax_sysmeter_fwdsmp']

    system_meters_datos.extend([obtener_texto(By.ID, id_) for id_ in ids])

    print(system_meters_datos)

    boton_home = driver.find_element(By.XPATH, "//div[@id='sysmetersPage']//a[@class='home_link']")
    boton_home.click()

def drive_chain():
    #Listoooooo
    exitador = 'B'
    boton_drive_chain = driver.find_element(By.XPATH, "//a[@id='menuBtn1']")
    boton_drive_chain.click()
    time.sleep(4)
    boton_drive_summary = driver.find_element(By.XPATH, "//a[@id='menuBtn1']")
    boton_drive_summary.click()

    drive_chain_datos = []

    '''
    --->Colocar botón en el cual se pueda elegir el exitador activo
        datos guardados:
            Module RF Out
            Module Input
            Input Voltage
            Total Current
    '''
    #ExcitadorA
    ids=[]
    if exitador == 'A':
        ids = ['xt_dca_mod_rf_out',
               'xt_dca_mod_dr',
               'xt_dca_inp_volt',
               'xt_dca_tot_curr']

    #ExcitadorB
    elif exitador == 'B':
        ids = ['xt_dcb_mod_rf_out',
                 'xt_dcb_mod_dr',
                 'xt_dcb_inp_volt',
                 'xt_dcb_tot_curr']

    drive_chain_datos.extend([obtener_texto(By.ID, id_) for id_ in ids])

    print(drive_chain_datos)

    boton_home = driver.find_element(By.XPATH, "//div[@id='dcsumPage']//a[@class='home_link']")
    boton_home.click()

def system_cooling():
    #Listoooooo
    boton_cooling = driver.find_element(By.ID, "fax_home_cooling")
    boton_cooling.click()

    cooling_datos = []

    ids = ['xt_pbcooling_itempc',
           'xt_pbcooling_flow1',
           'xt_pbcooling_inpress1',
           'xt_pbcooling_outpress1',
           'xt_pbcooling_ftempc']

    cooling_datos.extend([obtener_texto(By.ID, id_) for id_ in ids])

    print(cooling_datos)

    boton_home = driver.find_element(By.XPATH, "//div[@id='coolingPage']//a[@class='home_link']")
    boton_home.click()

