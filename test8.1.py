import datetime
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()


# check_box = driver.find_element(By.XPATH,"//button[@aria-label='Toggle']")
# check_box.click()

action = ActionChains(driver)
double = driver.find_element(By.XPATH,"//*[@id='doubleClickBtn']")
action.double_click(double).perform()

right_click = driver.find_element(By.XPATH,"//button[@id='rightClickBtn']")
action.context_click(right_click).perform()


time.sleep(5)
driver.quit()