import button as button
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def fun(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface").click()

    # confirm = browser.switch_to.alert
    # confirm.accept()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    z = fun(x)

    browser.find_element(By.ID, "answer").send_keys(z)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
