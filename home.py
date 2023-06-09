from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector("[alt='Selenium Ruby']").click()
driver.find_element_by_class_name("reviews_tab").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_class_name("star-5").click()
Comment = driver.find_element_by_id("comment")
Comment.send_keys("Nice book!")
Name = driver.find_element_by_id("author")
Name.send_keys("Kate")
Email = driver.find_element_by_id("email")
Email.send_keys("Ivanov@gmail.com")
driver.find_element_by_class_name("submit").click()
driver.quit()