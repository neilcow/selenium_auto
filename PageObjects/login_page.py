from PageLocators.login_page_locs import LoginPageLocs as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver: WebDriver):
        # 初始化drvier
        self.driver = driver

    # 登录，元素操作，
    def login(self, username, passwd):
        # 显性等待
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        self.driver.find_element(*loc.user_input).send_keys(username)
        self.driver.find_element(*loc.passwd_input).send_keys(passwd)
        self.driver.find_element(*loc.login_button).click()














