from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #  link = "http://suninjuly.github.io/selects1.html"
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")

    # берем значение переменной Х
    x_value = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    print(x_value)

    inpt = browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(calc(x_value))
    check1 = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    radio1 = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')

    browser.execute_script("return arguments[0].scrollIntoView(true);", radio1)
    radio1.click()

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#
#    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    # browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


