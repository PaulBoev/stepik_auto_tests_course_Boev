from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def sum(x, y):
    return str(int(x) + int(y))


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    z = sum(x, y)
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
