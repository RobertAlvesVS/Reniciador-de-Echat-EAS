from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from dotenv import load_dotenv
import os
load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


# Lista de URLs para verificação
urls_to_check = [
    {"url": "https://url.com.br/login"},
]

nao_foi = []
# Configurações do Selenium
firefox_options = Options()
# firefox_options.add_argument("--headless")  # Executar o Firefox sem interface gráfica
gecko_driver_path = r"geckodriver.exe"

def check_site_element(url):
    with webdriver.Firefox(
        service=Service(gecko_driver_path), options=firefox_options
    ) as driver:
        driver.get(url)
        try:
            # Realiza o login
            driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            driver.find_element(
                By.XPATH, "/html/body/div/main/div[1]/form/button"
            ).click()
            time.sleep(2)

            # Navega até o menu desejado
            driver.find_element(
                By.XPATH, "/html/body/div/div[1]/div[1]/div/ul/div/li[1]/a/div[1]"
            ).click()
            time.sleep(3.5)

            driver.find_element(
                By.XPATH, "/html/body/div/div[1]/main/div[2]/div/div[2]/div/button[1]"
            ).click()
            return print(f"Reiniciado com sucesso a {url}")
        except Exception as e:
            nao_foi.append(url)
            return print(f"Algo deu Erro {url}\n Porfavor verificar")


for url in urls_to_check:
    check_site_element(url["url"])
