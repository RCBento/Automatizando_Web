### IMPORTAÇÕES PARA LER O ARQUIVO EXCEL ###
import pandas as pd

import time

### IMPORTAÇÕES PARA AUTOMATIZAR A WEB ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url_forms = "https://forms.gle/7xkcLCPEf9TcthVr9"
info_arquivo = 'info.xlsx'
df = pd.read_excel(info_arquivo)

for index,row in df.iterrows():
    print("Index: " + str(index) + " | E o nome do Fulano é: " + row["Nome Completo"])
    chrome = webdriver.Chrome(executable_path='chromedriver.exe')
    chrome.get(url_forms)
    
    time.sleep(2)

    elemento_nome = chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    elemento_telefone = chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    elemento_nota = chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[' + str(row["Nota"]) +']/div[2]/div/div/div[3]/div')

    elemento_nome.send_keys(row["Nome Completo"])
    elemento_telefone.send_keys(row["Telefone"])
    elemento_nota.click()
    chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

    time.sleep(1)

    chrome.quit
