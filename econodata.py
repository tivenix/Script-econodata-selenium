   ##Import Bibliotecas

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import re
from bs4 import BeautifulSoup
#options = webdriver.ChromeOptions()
#options.add_argument(r"user-data-dir=C:\Users\pc casa\AppData\Local\Google\Chrome\User Data")
df = pd.read_excel("ECONODATA.xlsx",header=0)
df
CNPJ = df['CPF/CNPJ']

PATH = "C:\Program Files (x86)\chromedriver.exe" #local chromedriver.exe
driver = webdriver.Chrome(PATH) #navegador
driver.get("https://www.econodata.com.br/consulta-empresa/") #url site
driver.maximize_window()
x = 0
#barra de pesquisa
waitsearchbar = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div/input")))
waitsearchbar #esperar barra de pesquisa inicializar totalmente
searchbar = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div/input")
searchbar.click()
searchbar.send_keys(CNPJ[x])
#Pesquisar apertando ENTER
searchbar.send_keys(Keys.ENTER)

#Apertar botão de pesquisa após searchbar, contem .click
waitsearchbutton = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[5]/a"))).click()
waitsearchbutton #clicar na lupa apos pesquisa
#Espera opção pelo simples
driver.implicitly_wait(2)
waitopçao = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div[9]/div[2]")))
#Opção pelo simples
opçao = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div[9]/div[2]").text
print(CNPJ[x],opçao, "Opção pelo simples antes do loop")
driver.execute_script("window.history.go(-1)")
#lupa pesquisa
lupa = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[5]/a")))
#LOOP
x = 0
for x in range(len(CNPJ)):
    driver.get("https://www.econodata.com.br/consulta-empresa/")

    #driver.execute_script("window.history.go(-1)"),
    #searchbar.clear(),
    #driver.implicitly_wait(1)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div/input"))).click()

    driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div/input").send_keys(CNPJ[x+1], Keys.ENTER)
    driver.implicitly_wait(1)   
    #driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div[2]/form/div[1]/div/input").send_keys(Keys.ENTER)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr/td[5]/a"))).click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div[9]/div[2]")))
    opçao2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[5]/div/div[2]/div/div/div[9]/div[2]").text
    print(CNPJ[x],opçao2,"Dentro do loop")
