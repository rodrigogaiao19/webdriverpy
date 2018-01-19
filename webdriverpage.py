from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint


driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title

news_itens = driver.find_elements_by_css_selector('.blog-widget .menu li')

for item in news_itens:
    pprint(item.find_element_by_css_selector("a").text)
