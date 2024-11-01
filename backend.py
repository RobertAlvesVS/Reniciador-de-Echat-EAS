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
    {"url": "https://laboclin.eassystems.com.br/login"},
    {"url": "https://cardioprev.eassystems.com.br/login"},
    {"url": "https://navarro.eassystems.com.br/login"},
    {"url": "https://oftalmovilas.eassystems.com.br/login"},
    {"url": "https://carvillas.eassystems.com.br/login"},
    {"url": "https://amoedo.eassystems.com.br/login"},
    {"url": "https://icb.eassystems.com.br/login"},
    {"url": "https://odccajaz.eassystems.com.br/login"},
    {"url": "https://cfisio.eassystems.com.br/login"},
    {"url": "https://hospitalsea.eassystems.com.br/login"},
    {"url": "https://hospolhosantbarbosa.eassystems.com.br/login"},
    {"url": "https://angiclin.eassystems.com.br/login"},
    {"url": "https://fazendafelicita.eassystems.com.br/login"},
    {"url": "https://guirra.eassystems.com.br/login"},
    {"url": "https://holhos.eassystems.com.br/login"},
    {"url": "https://otorhinus.eassystems.com.br/login"},
    {"url": "https://rcs.eassystems.com.br/login"},
    {"url": "https://wisetech.eassystems.com.br/login"},
    {"url": "https://agnusdei.eassystems.com.br/login"},
    {"url": "https://biomol.eassystems.com.br/login"},
    {"url": "https://maxbe.eassystems.com.br/login"},
    {"url": "https://hsaomatheuscirurgia.eassystems.com.br/login"},
    {"url": "https://clinday.eassystems.com.br/login"},
    {"url": "https://erasmo.eassystems.com.br/login"},
    {"url": "https://espacoabsolut.eassystems.com.br/login"},
    {"url": "https://otorhinusfilial.eassystems.com.br/login"},
    {"url": "https://prover.eassystems.com.br/login"},
    {"url": "https://salvador.eassystems.com.br/login"},
    {"url": "https://seta.eassystems.com.br/login"},
    {"url": "https://sst.eassystems.com.br/login"},
    {"url": "https://wfg.eassystems.com.br/login"},
    {"url": "https://dnmaster.eassystems.com.br/login"},
    {"url": "https://echat.eassystems.com.br/login"},
    {"url": "https://alianca.eassystems.com.br/login"},
    {"url": "https://echat2.eassystems.com.br/login"},
    {"url": "https://apg.eassystems.com.br/login"},
    {"url": "https://qockpit.eassystems.com.br/login"},
    {"url": "https://rodoclinica.eassystems.com.br/login"},
    {"url": "https://vocetotal.eassystems.com.br/login"},
    {"url": "https://bns.eassystems.com.br/login"},
    {"url": "https://diagnoplus.eassystems.com.br/login"},
    {"url": "https://ivaclinica.eassystems.com.br/login"},
    {"url": "https://laboclinpernambues.eassystems.com.br/login"},
    {"url": "https://cardiovascular.eassystems.com.br/login"},
    {"url": "https://silvestre.eassystems.com.br/login"},
    {"url": "https://bb.eassystems.com.br/login"},
    {"url": "https://pitapoan.eassystems.com.br/login"},
    {"url": "https://climego.eassystems.com.br/login"},
    {"url": "https://itapoanmed.eassystems.com.br/login"},
    {"url": "https://priovermelho.eassystems.com.br/login"},
    {"url": "https://clioc.eassystems.com.br/login"},
    {"url": "https://vita.eassystems.com.br/login"},
    {"url": "https://laboclingrupo.eassystems.com.br/login"},
    {"url": "https://odontosim.eassystems.com.br/login"},
    {"url": "https://klingo.eassystems.com.br/login"},
    {"url": "https://antbarbosa.eassystems.com.br/login"},
    {"url": "https://laboclincanela.eassystems.com.br/login"},
    {"url": "https://exame.eassystems.com.br/login"},
    {"url": "https://vida.eassystems.com.br/login"},
    {"url": "https://iel.eassystems.com.br/login"},
    {"url": "https://aa.eassystems.com.br/login"},
    {"url": "https://modernasany.eassystems.com.br/login"},
    {"url": "https://colp.eassystems.com.br/login"},
    {"url": "https://cmulher.eassystems.com.br/login"},
    {"url": "https://coracaodovale.eassystems.com.br/login"},
    {"url": "https://qualivida.eassystems.com.br/login"},
    {"url": "https://laboclinfeira.eassystems.com.br/login"},
    {"url": "https://medpless.eassystems.com.br/login"},
    {"url": "https://centromedicoantbarbosa.eassystems.com.br/login"},
    {"url": "https://laboclinqualidade.eassystems.com.br/login"},
    {"url": "https://laboclinareatecnica.eassystems.com.br/login"},
    {"url": "https://irba.eassystems.com.br/login"},
    {"url": "https://laboclinrh.eassystems.com.br/login"},
    {"url": "https://perfinor.eassystems.com.br/login"},
    {"url": "https://medjan.eassystems.com.br/login"},
    {"url": "https://uros.eassystems.com.br/login"},
    {"url": "https://hsaomatheus.eassystems.com.br/login"},
    {"url": "https://procardiaco.eassystems.com.br/login"},
    {"url": "https://cotefi.eassystems.com.br/login"},
    {"url": "https://nutriclin.eassystems.com.br/login"},
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
