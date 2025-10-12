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