from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://demo.nopcommerce.com/")

##LOGIN
driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
##User e senha
driver.find_element(By.XPATH, "//input[@class='email']").send_keys('testeraffaelial@gmail.com')
driver.find_element(By.XPATH, "//input[@class='password']").send_keys('Teste123@')
driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.quit()
