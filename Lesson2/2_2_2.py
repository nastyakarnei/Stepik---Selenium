from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_element=browser.find_element_by_css_selector("#input_value").text
#x = x_element.text
y = calc(x_element)
browser.execute_script("window.scrollBy(0, 110);")
input1 = browser.find_element_by_css_selector('#answer').send_keys(y)
#input1.send_keys(y)
input2 = browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
#input2.click()
input3 = browser.find_element_by_css_selector('#robotsRule').click()
#input3.click()
#button = browser.find_element_by_tag_name("button")
button.click()