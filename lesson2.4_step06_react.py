from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Варианты ожидания свойств элементов для expected_conditions
# -----------------------------------------------------------
#    title_is
#    title_contains
#    presence_of_element_located
#    visibility_of_element_located
#    visibility_of
#    presence_of_all_elements_located
#    text_to_be_present_in_element
#    text_to_be_present_in_element_value
#    frame_to_be_available_and_switch_to_it
#    invisibility_of_element_located
#    element_to_be_clickable
#    staleness_of
#    element_to_be_selected
#    element_located_to_be_selected
#    element_selection_state_to_be
#    element_located_selection_state_to_be
#    alert_is_present

#   Дополнительная информация - https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
#    button = WebDriverWait(browser, 5).until_not(
#            EC.element_to_be_clickable((By.ID, "verify"))
#        )


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не будет равна 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price", "100"))
    )

    # Снова жмем на батоны
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()


    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



