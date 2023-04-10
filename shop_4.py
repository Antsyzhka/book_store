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
driver.find_element_by_id("menu-item-40").click()
# 3
driver.execute_script("window.scrollBy(0, 700);")
driver.find_element_by_css_selector(".product_tag-mastering .button ").click()
Basket = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "added_to_cart"), "View Basket"))
# 4
#Item = driver.find_element_by_css_selector("[title='View your shopping cart']")
Item = driver.find_element_by_class_name("cartcontents")
Item_text = Item.text
#print(Item_text)
assert Item_text == "1 Item"

price = driver.find_element_by_class_name("amount")
price_text = price.text
#print(price_text)
assert price_text == "₹350.00"
# 5
driver.find_element_by_id("wpmenucartli").click()
# 6
Subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,
        "[data-title='Subtotal'] .amount"), "₹350.00"))
#print(Subtotal)
# 7
Total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,
        ".order-total .amount"), "₹357.00"))
#print(Total)
driver.quit()