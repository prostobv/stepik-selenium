from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    # element.send_keys(file_path)

    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.abspath(__file__))
    print(file_path)

    firstname = browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('SerJ')
    lastname = browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('BB')
    email = browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('test@mail.ru')

    # отправляем file
    browser.find_element(By.XPATH, '//input[@name="file"]').send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



