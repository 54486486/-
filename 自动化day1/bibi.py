from  selenium import webdriver

import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.bilibili.com/")

driver.find_element_by_xpath("//*[@class='nav-search-keyword']").send_keys("周姐语录")

driver.find_element_by_xpath("//*[@class='nav-search-btn']").click()

driver.switch_to.window(driver.window_handles[-1])

driver.find_element_by_xpath("//*[@title='【周淑怡】周姐的土味社会语录']").click()

driver.switch_to.window(driver.window_handles[-1])

time.sleep(8)

driver.find_element_by_xpath("//*[@class='like']")































