from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# id
element = driver.find_element(By.ID, 'kw')
element.send_keys('测试')

# # class_name
# driver.find_element(By.CLASS_NAME, 's_ipt')
# driver.find_elements(By.CLASS_NAME, 's_ipt')
# # name
# driver.find_element(By.NAME, 'wd')
# driver.find_elements(By.NAME, 'wd')
#
# # tag
# driver.find_element(By.TAG_NAME, 'input')
# driver.find_elements(By.TAG_NAME, 'input')

# link_text
driver.find_element(By.LINK_TEXT, '地图')
driver.find_elements(By.LINK_TEXT, '地图')

# partial_link_text
driver.find_element(By.PARTIAL_LINK_TEXT, 'hao')

# driver.quit()

