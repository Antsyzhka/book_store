from selenium import webdriver

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
driver.find_element_by_css_selector(".cat-item-19>a").click()
# 5
items_html = driver.find_elements_by_class_name("product_cat-html") # находим список отображаемых товаров
# проверка что в категории HTML отображается 3 товара
if len(items_html) == 3:
    print("В категории отображается 3 книги") # len здесь посчитает количество элементов, найденных при помощи find_elements
else:
    print("Ошибка. Количество книг в категории: " + str(len(items_html)))

driver.quit()