from PageLocators.login_page_locs import LoginPageLocs as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Common.basepage import BasePage


class LoginPage(BasePage):

    # 登录，元素操作，
    def login(self, username, passwd):
        # 显性等待
        self.input_text(loc.user_input, username, "登录页面_输入用户名")
        self.input_text(loc.passwd_input, passwd, "登录页面_输入密码")
        self.click_element(loc.login_button, "点击登录按钮")

    # 获取登录区域的提示信息
    def get_msg_from_login_form(self):
        self.wait_ele_visible(loc.msg_from_login_form, "登录页面_等待登录表单的错误提示元素")












