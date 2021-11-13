from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

#def calc(x,y):
  #return str(math.x+math.y)
#try: 
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_css_selector('#num1')
x = x_element.text
y_element = browser.find_element_by_css_selector('#num2')
y = y_element.text
print(x)
print(y)
z=str(int(x)+int(y))
print(z)

select = Select(browser.find_element_by_css_selector('#dropdown'))
select.select_by_value(z) 


button = browser.find_element_by_css_selector('.btn.btn-default')
button.click()

