from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
#driver.implicitly_wait(5)
# 1
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
# 2
driver.find_element_by_id("menu-item-40").click()
time.sleep(3)
# 3
driver.execute_script("window.scrollBy(0, 700);")
driver.find_element_by_css_selector(".product_tag-mastering .button ").click()
time.sleep(3)
# 4
driver.find_element_by_id("wpmenucartli").click()
time.sleep(3)
# 5
driver.find_element_by_css_selector(".product-remove .remove").click()
time.sleep(3)
# 6
driver.find_element_by_link_text("Undo?").click()
time.sleep(3)
# 7
Quantity = driver.find_element_by_css_selector(".quantity>[type='number']")
Quantity.clear()
Quantity.send_keys(3)
time.sleep(3)
# 8
driver.find_element_by_name("update_cart").click()
time.sleep(3)
# 9
Quantity1 = driver.find_element_by_css_selector(".quantity>[type='number']")
Quantity1_value = Quantity1.get_attribute("value")
#print(Quantity1_value)
assert Quantity1_value == "3"
time.sleep(3)
# 10
driver.find_element_by_name("apply_coupon").click()
time.sleep(3)
# 11
ApplyCoupon = driver.find_element_by_class_name("woocommerce-error")
ApplyCoupon_text = ApplyCoupon.text
#print(ApplyCoupon_text)
assert ApplyCoupon_text == "Please enter a coupon code."
time.sleep(3)
driver.quit()
