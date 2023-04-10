from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
# 1
driver.get("https://practice.automationtesting.in/")
# 2
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 700);")
# 3
driver.find_element_by_css_selector(".product_tag-mastering .button ").click()
Basket = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "added_to_cart"), "View Basket"))
# 4
driver.find_element_by_id("wpmenucartli").click()
# 5
Proceed = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
Proceed.click()
# 6
PlaceOrder = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "place_order")))

FirstName = driver.find_element_by_id("billing_first_name")
FirstName.send_keys("Ivan")

LastName = driver.find_element_by_id("billing_last_name")
LastName.send_keys("Ivanov")

Email = driver.find_element_by_id("billing_email")
Email.send_keys("Ivanov@gmail.com")

Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("12345678")

driver.find_element_by_id("s2id_billing_country").click()
CountrySearch = driver.find_element_by_id("s2id_autogen1_search")
CountrySearch.send_keys("Jersey")
driver.find_element_by_class_name("select2-match").click()

Email = driver.find_element_by_id("billing_address_1")
Email.send_keys("Rte Orange")

Unit = driver.find_element_by_id("billing_address_2")
Unit.send_keys("12")

City = driver.find_element_by_id("billing_city")
City.send_keys("Saint-Brelade")

State = driver.find_element_by_id("billing_state")
State.send_keys("Jersey")

ZIP = driver.find_element_by_id("billing_postcode")
ZIP.send_keys("JE3")
# 7
driver.execute_script("window.scrollBy(0, 700);")
time.sleep(3)
driver.find_element_by_id("payment_method_cheque").click()
# 8
driver.find_element_by_id("place_order").click()
# 9
Thank = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),
                                     "Thank you. Your order has been received."))
print(Thank)
# 10
Method = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))
print(Method)
