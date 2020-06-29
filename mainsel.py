from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import time


profile = FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/octet-stream')
driver = webdriver.Firefox(firefox_profile=profile)


driver.get('https://sismpconsultapublica.mpsp.mp.br/ConsultarProcedimentos/ObterProcedimentos')

driver.implicitly_wait(3)


driver.find_element_by_xpath("//select[@id='UA']/option[text()='PROMOTORIA DE JUSTIÇA DO I TRIBUNAL DO JÚRI']").click()
btnbusca = driver.find_element_by_id('btnConsultar')
btnbusca.click()


driver.implicitly_wait(5)

for target_list in range(100):
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

