from selenium import webdriver
import math
# from selenium.webdriver.chrome.options import Options
import time 

link = "http://suninjuly.github.io/find_link_text"

try:
#    option = webdriver.ChromeOptions()
#    option.add_argument('--headless')
#    option.add_argument('--no-sandbox')
#    option.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')

    browser = webdriver.Chrome()

    browser.get(link)

    text_link = str(math.ceil(math.pow(math.pi, math.e)*10000)) # 224592

    link = browser.find_element_by_link_text(text_link)
    link.click()

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Sj")

    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")

    input_city = browser.find_element_by_css_selector(".form-control.city")
    input_city.send_keys("M")

    input4 = browser.find_element_by_id("country")
    input4.send_keys("Gukia")

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


#    input1 = browser.find_element_by_tag_name("input")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element_by_name("last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element_by_class_name("city")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element_by_id("country")
#    input4.send_keys("Russia")
#    button = browser.find_element_by_css_selector(".btn.btn-default")
#    button.click()


finally:
    time.sleep(5)
#    browser.quit()
