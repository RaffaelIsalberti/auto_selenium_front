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

##User e senha
driver.find_element(By.XPATH, "//input[@class='email']").send_keys('testeraffaelial@gmail.com')
driver.find_element(By.XPATH, "//input[@class='password']").send_keys('Teste123@')
driver.find_element(By.XPATH, "//button[text() ='Log in']").click()

#ACTION EM VARIAVEL
actions = ActionChains(driver)
##FUNÇÃO MOUSE HOVER - MOUSE FLUTUANTE

mouse_tracker = driver.find_element(By.XPATH, "//a[text() ='Computers ']")
actions.move_to_element(mouse_tracker).perform()

desk_tracker = driver.find_element(By.XPATH, "//a[text() ='Desktops ']")
actions.move_to_element(desk_tracker).perform()

note_tracker = driver.find_element(By.XPATH, "//a[text() ='Notebooks ']")
actions.move_to_element(note_tracker).perform()

##NAVEGAÇÃO LOJA NOTEBOOK

driver.find_element(By.XPATH, "//a[text() ='Notebooks ']").click()
driver.find_element(By.ID, 'attribute-option-7').click()
time.sleep(2)
produto1 = driver.find_element(By.XPATH, "//h2/a[text() = 'Asus N551JK-XO076H Laptop']")
wait.until(EC.element_to_be_clickable(produto1))
actions.click(produto1).perform()

##FUNÇÃO DOUBLE CLICK MOUSE e SCROLL
#limpar campo para preenchimento

camp_valor = driver.find_element(By.ID, "product_enteredQuantity_5")
actions.scroll_to_element(camp_valor).perform()
actions.double_click(camp_valor).perform()
camp_valor.send_keys(Keys.DELETE)

##ADICIONAR FUNÇÃO WAIT
camp_valor.send_keys('2')
driver.find_element(By.ID, "add-to-cart-button-5").click()


##CARRINHO
assert driver.find_element(By.XPATH, "//p[text()= 'The product has been added to your ']").is_displayed()
driver.find_element(By.XPATH, "//span[@class='close']").click()

##MOUSE HOPER CARRINHO
shop_cart = driver.find_element(By.XPATH, "//span[text()= 'Shopping cart']")
actions.scroll_to_element(shop_cart).perform()
actions.move_to_element(shop_cart).perform()
driver.find_element(By.XPATH, "//button[@class='button-1 cart-button']").click()



driver.quit()
