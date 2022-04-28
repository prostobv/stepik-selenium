from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Жмем на батоны
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # берем значение переменной Х и считаем значение
    x_value = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    inpt = browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(calc(x_value))

    # Снова жмем на батоны
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



