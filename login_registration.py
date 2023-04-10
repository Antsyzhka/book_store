from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
#time.sleep(3)
driver.find_element_by_id("menu-item-50").click()
#time.sleep(3)
Regemail = driver.find_element_by_id("reg_email")
#Regemail.send_keys("Ivanov1@gmail.com")
Regemail.send_keys("Ivanov@gmail.com")
Password = driver.find_element_by_id("reg_password")
Password.send_keys("!Ivanov123")
#time.sleep(5)
#medium = WebDriverWait(driver, 10).until(
#EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "[aria-live='polite']"), "Medium"))
Register = WebDriverWait(driver, 20).until(
   EC.element_to_be_clickable((By.NAME, "register")))
#driver.find_element_by_css_selector("[value='Register']").click()
#medium = driver.find_element_by_css_selector("[aria-live='polite']")
#medium_get_text = medium.text
#assert medium_get_text == "Medium"
driver.find_element_by_name("register").click()
#Register.click()
#driver.quit()
