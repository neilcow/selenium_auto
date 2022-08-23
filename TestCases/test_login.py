import unittest
from selenium import webdriver
import ddt
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from TestDates import login_datas as lds
from TestDates import Global_Datas as GD


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 访问登录页面
        self.driver = webdriver.Chrome()
        self.driver.get(GD.base_url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self):
        # 步骤 1、登录页面-登录操作  用户名密码
        LoginPage(self.driver).login(*lds.success)
        # 断言 首页- 获取元素是否存在
        self.assertTrue(HomePage(self.drvier).get_element_exists())

    @ddt.data(*lds.cases)
    def test_login_failed_wrong_format(self, case):
        # 步骤 1、登陆页面 登录操作 用户名密码期望数据
        lp = LoginPage(self.driver)
        lp.login(case["user"], case["passwd"])
        # 断言
        # self.assertTrue()












