from selenium import webdriver

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
#Проверка Logout
Logout = driver.find_element_by_link_text("Logout")
Logout_get_text = Logout.text
assert Logout_get_text == "Logout"
#print(Logout_get_text)

driver.quit()
