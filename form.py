from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path='D:\dev\chromedriver.exe'
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://sso.teachable.com/secure/37913/identity/login/password')

email=driver.find_element_by_name('email')
email.send_keys('example name')

password=driver.find_element_by_name('password')
password.send_keys('password')

email.send_keys(Keys.ENTER)