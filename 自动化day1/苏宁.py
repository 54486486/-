from selenium import  webdriver

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("狼蛛键盘")

driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

driver.find_element_by_xpath("//*[@href='//product.suning.com/0010331177/12286087152.html']").click()

driver.switch_to.window(driver.window_handles[-1])

driver.find_element_by_xpath("//*[@id='addCart']").click()















