from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('chromedriver.exe')

url = ('https://www.netflix.com/ar/title/80192098') 
browser.get(url)

Temp_button = browser.find_element_by_name('season-selector')

Temp_button.send_Keys(Keys.DOWN) #presiona la tecla de abajo


'''
----------------------------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
user = ""
pwd = ""
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")

assert "Facebook" in driver.title                    #verifica que el titulo de la pagina sea facebook

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.close()

----------------------------------------------------------------------------------------------------

https://selenium-python.readthedocs.io/getting-started.html#simple-usage

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

'''