import button as button
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def fun(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    z = fun(x)

    browser.find_element(By.ID, "answer").send_keys(z)
    browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element(By.CSS_SELECTOR, ".btn").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
