from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
options = webdriver.ChromeOptions()
 #options .add_argument("--disable-notifications")

 #Fix Error about metrics.cc 
options.add_experimental_option('excludeSwitches', ['enable-logging'])



driver = webdriver.Chrome('./chromedriver.exe',options=options)

driver.get("http://www.google.com")

#google search frome
ele = driver.find_element_by_class_name("gLFyf.gsfi")

#next page
#driver.forward()
#previous PAGE
#driver.back()

#Transfer String
ele.send_keys("Selenium Python")

#ele.clear()
#clear searched history
#ele.clear()

#google search button
button = driver.find_element_by_class_name("gNO89b")

button.submit()








driver.quit()


