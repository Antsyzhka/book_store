from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
Regemail = driver.find_element_by_id("username")
Regemail.send_keys("Ivanov@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("!Ivanov123")
driver.find_element_by_css_selector("[value='Login']").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
Book_html = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[itemprop='name']"), "HTML5 Forms"))
#print(Book_html)
driver.quit()