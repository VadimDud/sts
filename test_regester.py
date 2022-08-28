# import selectors
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://sandbox.synctoskill.com/')
driver.maximize_window()
# driver.get_screenshot_as_file("1.png")
driver.find_elements(By.XPATH, '//a[@class="nav-link text-dark"]')[1].click()
driver.find_element(By.NAME, 'FullName').send_keys('User User')
driver.find_element(By.NAME, 'Email').send_keys('user99@test.com')
driver.find_element(By.NAME, 'Password').send_keys('123()aA:')
driver.find_element(By.NAME, 'PasswordConfirmation').send_keys('123()aA:')
driver.find_element(By.NAME, 'Phone').send_keys('7(111)111-11-11')
driver.find_element(By.NAME, 'Address').send_keys('Dom, 1')
driver.find_elements(By.XPATH, '//input[@value="Sign Up"]')[0].click()

time.sleep(6)
driver.close()
