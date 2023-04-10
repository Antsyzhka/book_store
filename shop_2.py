from selenium import webdriver
from selenium.webdriver.support.select import Select

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
select = driver.find_element_by_css_selector("[value='menu_order']")
select_checked = select.get_attribute("selected")
if select_checked is not None:
    print("В селекторе выбрано значение: 'Default sorting'")
else:
    print("В селекторе выбрано не 'Default sorting'")
# 5
select_1 = driver.find_element_by_class_name("orderby")
select_high = Select(select_1)
select_high.select_by_value("price-desc")
# 6-7
select_2 = driver.find_element_by_css_selector("[value='price-desc']")
select_2_checked = select_2.get_attribute("selected")
if select_2_checked is not None:
    print("В селекторе выбрано значение: 'Sort by price: high to low'")
else:
    print("В селекторе выбрано не 'Sort by price: high to low'")

driver.quit()
