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
#import time

lista_ip_ird = [
    'http://10.20.39.211/advanced',             #IRD Main Red 2 SCDLC
    'http://10.20.39.212/advanced',             #IRD Main Red 5 SCDLC
    'http://10.20.39.213/advanced',             #IRD Main Red 9 SCDLC
    'http://10.20.39.216/advanced',             #IRD Main Red 4 SCDLC
    'http://10.20.39.214/advanced',             #IRD BKP Red 2 SCDLC
    'http://10.20.39.215/advanced',             #IRD BKP Red 5 SCDLC
    'http://10.20.39.217/advanced',             #IRD BKP Red 4 SCDLC
]

#service = Service(ChromeDriverManager().install())
service = Service(r'D:/Proyectos/Rep Tuxtla/Drivers/chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.maximize_window()

for i in lista_ip_ird:
    driver.get(i)
    driver.switch_to.frame("mainFrame")
    boton_input = WebDriverWait(driver, 15).until(
        ec.presence_of_element_located((By.XPATH, "//p[@class='nText'][normalize-space()='Input']"))
    )
    boton_input.click()

driver.quit()