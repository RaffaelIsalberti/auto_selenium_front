import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")

##LOGIN
driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
driver.find_element(By.XPATH, "//input[@class='email']").send_keys('testeraffaelial@gmail.com')
driver.find_element(By.XPATH, "//input[@class='password']").send_keys('Teste123@')
driver.find_element(By.XPATH, "//button[text() ='Log in']").click()


##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE
actions = ActionChains(driver)
shop_car = driver.find_element(By.XPATH, "//span[text()= 'Shopping cart']")
actions.move_to_element(shop_car).perform()
driver.find_element(By.XPATH, "//button[@class='button-1 cart-button']").click()

#LIMPAR CARRINHO
limpar_compra = driver.find_element(By.XPATH, "//button[@class='remove-btn']")
actions.click(limpar_compra).perform()

log_out = driver.find_element(By.XPATH, "//a[text() = 'Log out']")
actions.click(log_out).perform()
time.sleep(2)
assert driver.find_element(By.XPATH, "//h2[text()= 'Welcome to our store']").is_displayed()

driver.quit()
