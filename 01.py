import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


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
driver.find_element(By.XPATH, '')
# driver.implicitly_wait()
loc = ("xpath", '')
WebDriverWait(driver, 15, 0.5).until(expected_conditions.visibility_of_element_located(loc))
driver.window_handles
# driver.quit()

from selenium.webdriver.common.action_chains import ActionChains

# 1、找到鼠标要操作的元素
loc = (By.XPATH, '//')
ele = driver.find_element(*loc)

# 2、实例化ActionChains类
ac = ActionChains(driver)
# 3、调用鼠标行为
ac.move_to_element(ele).click(ele)
# 4、调用perform()来执行鼠标动作
ac.perform()

# 关闭会话
time.sleep(7)
driver.quit()

from selenium.webdriver.support.select import Select

# 初始化，找select 对象
loc = (By.XPATH, '')
select_element = driver.find_element(loc)
s = Select(select_element)
# 根据下标，value属性、文本内容来选择值
s.select_by_index(6)
time.sleep(3)
s.select_by_value('doc')
time.sleep(3)
s.select_by_visible_text('文件')

# js函数，元素对象.scrollIntoView()
loc = (By.XPATH, '')
a = driver.find_element(*loc)
driver.execute_script('arguments[0].scrollIntoView();', a)
# 滚动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 滚动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")