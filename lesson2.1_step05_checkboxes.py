from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # берем значение переменной Х
    x_value = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    print(x_value)

    # вывод атрибутов radio-button
    people_radio = browser.find_element(By.XPATH, '//input[@id="peopleRule"]')
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    inpt = browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(calc(x_value))
    check1 = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    radio1 = browser.find_element(By.XPATH, '//input[@id="robotsRule"]').click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()