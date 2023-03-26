from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path='D:\dev\chromedriver.exe'
driver=webdriver.Chrome(executable_path=chrome_driver_path)

# //////////////////// wiki automation ////////////////////
driver.get('https://en.wikipedia.org/wiki/Main_Page')

articles_number=driver.find_element_by_css_selector('#articlecount > a:nth-child(1)')
print(articles_number.text)

# how to click on something
# articles_number.click()
# source= driver.find_element_by_link_text('View source')
# source.click()
search=driver.find_element_by_name('search')
search.send_keys('python')
search.send_keys(Keys.ENTER)
# driver.quit()
