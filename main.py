from selenium import webdriver

chrome_driver_path = 'D:\dev\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# ////////////////////// amazon automation /////////////////////////////

# driver.get(
#     'https://www.amazon.com/Acer-SB220Q-Ultra-Thin-Frame-Monitor/dp/B07CVL2D2S/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w'
#     '=nl9qH&content-id=amzn1.sym.1bcf206d-941a-4dd9-9560-bdaa3c824953&pf_rd_p=1bcf206d-941a-4dd9-9560-bdaa3c824953'
#     '&pf_rd_r=52C61MR539RN9FBAQ58Z&pd_rd_wg=tbGbX&pd_rd_r=e31d7546-025e-4715-a6c9-1961d64b0729&pd_rd_i=B07CVL2D2S')
# price = driver.find_element_by_class_name('a-price-whole')
# driver.find_element_by_name().tag_name()   <==================== really useful for  forms
# driver.find_element_by_name().get_attribute("placeholder")
# driver.find_element_by_name().
# print(price.text)
# logo = driver.find_element_by_id('nav-logo-sprites')
# print(logo.size)
# css = driver.find_element_by_class_name('.nav-logo-sprites a')
# print(css.text)

# some_non_unique_thing= driver.find_element_by_xpath('//*[@id="navFooter"]/div[4]/table/tbody/tr[7]/td[9]/a/span')
# print(some_non_unique_thing.text)
#
# driver.find_elements_by_id()
# driver.close()
# driver.quit()

# ///////////////// python.org automation //////////////////
# driver.get('https://www.python.org/')
# # events = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
# event_time = driver.find_elements_by_css_selector('.event-widget time')
# event_name = driver.find_elements_by_css_selector('.event-widget li a')
#
# events_dic = {event_time[i].text: event_name[i].text for i in range(len(event_time))}
# print(events_dic)
#
# driver.quit()


