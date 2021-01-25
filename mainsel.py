from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time


# ASSUNTO:
Assunt = "DIREITO PENAL - Crimes contra a vida - Homicídio Simples"

# PROCEDIMENTO: (Procedimentos possíveis: Inquérito Civil - IC,
#                                         Inquérito Policial - IP,
#                                         Procedimento Investigatório Criminal - PIC,
#                                         Procedimento Preparatório Inquérito Civil - PPIC )
Proced = "Inquérito Policial - IP"

# UNIDADE:
Unid = "PROMOTORIA DE JUSTIÇA DO III TRIBUNAL DO JÚRI"



# INÍCIO DO CÓDIGO, NÃO ALTERE AS LINHAS ABAIXO
profile = FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/octet-stream')
profile.accept_untrusted_certs = True
driver = webdriver.Firefox(firefox_profile=profile)

driver.get('https://sismpconsultapublica.mpsp.mp.br/ConsultarProcedimentos/ObterProcedimentos')

driver.implicitly_wait(3)

driver.find_element_by_xpath("//select[@id='TipoProcedimento']/option[text()='" + Preced + "']").click()
driver.find_element_by_xpath("//select[@id='UA']/option[text()='" + Unid + "']").click()
btnbusca = driver.find_element_by_id('btnConsultar')
assunto = driver.find_element_by_id('AssuntoTabUni')
assunto.send_keys(Assunt)

btnbusca.click()

driver.implicitly_wait(5)

for target_list in range(218):
    driver.implicitly_wait(1)
    btnbusca = driver.find_element_by_id('btnConsultar')
    btnbusca = driver.find_elements_by_class_name('botao-paginacao')
    downloadbt = driver.find_element_by_xpath("//form[@action='/ConsultarProcedimentos/DownloadOds']//button")
    downloadbt.click()
    
    if len(btnbusca) < 4:
        btnbusca[0].click()
    else:
        btnbusca[-2].click()
    #time.sleep(1)

