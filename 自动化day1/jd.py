from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get("https://www.jd.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("亚索")

driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()

time.sleep(5)

driver.find_element_by_partial_link_text("电脑桌摆件办公桌摆件创意摆件桌面小摆件创意亚索武士蜡笔小新公仔汽车摆件车").click()

time.sleep(5)

driver.switch_to.window(driver.window_handles[-1])

driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()





