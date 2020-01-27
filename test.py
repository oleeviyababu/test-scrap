from selenium import webdriver
chrome_path=r"C:\Users\User\Desktop\chromedriver_win32 (5)\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.get("https://www.python.org/")
driver.find_element_by_xpath("""//*[@id="downloads"]/a""").click()
