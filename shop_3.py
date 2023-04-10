from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
# 1
driver.get("https://practice.automationtesting.in/")
# 2
driver.find_element_by_id("menu-item-50").click()
Regemail = driver.find_element_by_id("username")
Regemail.send_keys("Ivanov@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("!Ivanov123")
driver.find_element_by_css_selector("[value='Login']").click()
# 3
driver.find_element_by_id("menu-item-40").click()
# 4
driver.find_element_by_css_selector("[alt='Android Quick Start Guide']").click()
# 5
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
# 6
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
#7
Book_android = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='Android Quick Start Guide']")))
Book_android.click()
# 8
Book_close = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
Book_close.click()
driver.quit()