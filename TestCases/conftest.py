import pytest
from selenium import webdriver
from TestDates import Global_Datas as GD
from PageObjects.login_page import LoginPage
import logging


@pytest.fixture
def init_driver():
    # 前置：打开浏览器，访问系统网址
    # 后置： 退出浏览器
    logging.info("**** conftest.py 共享的init_driver前置")
    driver = webdriver.Chrome()
    driver.get(GD.base_url)
    driver.maximize_window()
    yield
    driver.quit()
    logging.info("**** conftest.py 共享的init_driver后置")


@pytest.fixture
def init_login(init_driver):
    LoginPage(init_driver).login(GD.user, GD.passwd)
    yield init_driver

