#       ___  ___  ___  ________  ________   _________  ________  ________  _________  ___  ________  ________
#      |\  \|\  \|\  \|\   __  \|\   ___  \|\___   ___\\   __  \|\   ____\|\___   ___\\  \|\   ____\|\   __  \
#      \ \  \ \  \\\  \ \  \|\  \ \  \\ \  \|___ \  \_\ \  \|\  \ \  \___|\|___ \  \_\ \  \ \  \___|\ \  \|\  \
#    __ \ \  \ \  \\\  \ \   __  \ \  \\ \  \   \ \  \ \ \   __  \ \_____  \   \ \  \ \ \  \ \  \    \ \  \\\  \
#   |\  \\_\  \ \  \\\  \ \  \ \  \ \  \\ \  \   \ \  \ \ \  \ \  \|____|\  \   \ \  \ \ \  \ \  \____\ \  \\\  \
#   \ \________\ \_______\ \__\ \__\ \__\\ \__\   \ \__\ \ \__\ \__\____\_\  \   \ \__\ \ \__\ \_______\ \_______\
#    \|________|\|_______|\|__|\|__|\|__| \|__|    \|__|  \|__|\|__|\_________\   \|__|  \|__|\|_______|\|_______|
#                                                                  \|_________|

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

lista_ip_ird = [
    'http://10.20.39.211/advanced',  # IRD Main Red 2 SCDLC
    'http://10.20.39.212/advanced',  # IRD Main Red 5 SCDLC
    'http://10.20.39.213/advanced',  # IRD Main Red 9 SCDLC
    'http://10.20.39.216/advanced',  # IRD Main Red 4 SCDLC
    'http://10.20.39.214/advanced',  # IRD BKP Red 2 SCDLC
    'http://10.20.39.215/advanced',  # IRD BKP Red 5 SCDLC
    'http://10.20.39.217/advanced',  # IRD BKP Red 4 SCDLC
]

#service = Service(ChromeDriverManager().install())
service = Service(r'D:/Proyectos/Rep Tuxtla/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

for i, url in enumerate(lista_ip_ird, start=1):
    print(f"\n➡️ Accediendo a {url} ({i}/{len(lista_ip_ird)})...")
    try:
        driver.get(url)

        # Esperar frame principal y cambiar
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.NAME, "mainFrame")))

        # Desactivar temporalmente el frame que tapa (resultFrame)
        driver.execute_script("document.getElementsByName('resultFrame')[0].style.pointerEvents='none';")

        # Esperar botón Input
        boton_input = wait.until(
            ec.element_to_be_clickable((By.XPATH, "//p[@class='nText'][normalize-space()='Input']"))
        )

        # Asegurar visibilidad
        driver.execute_script("arguments[0].scrollIntoView(true);", boton_input)
        time.sleep(0.5)
        boton_input.click()

        # Esperar y hacer clic en SAT Input
        boton_satellite_input = wait.until(
            ec.element_to_be_clickable((By.XPATH, "//table[@id='SAT Input']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", boton_satellite_input)
        time.sleep(0.3)
        boton_satellite_input.click()

        print(f"✅ Acceso exitoso a {url}")

    except TimeoutException:
        print(f"⚠️ Timeout o IP inaccesible en {url}")
    except NoSuchElementException:
        print(f"❌ Elemento no encontrado en {url}")
    except Exception as e:
        print(f"🚨 Error inesperado en {url}: {e}")
    finally:
        driver.switch_to.default_content()
        time.sleep(2)