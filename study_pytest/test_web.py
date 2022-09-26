import pytest
from selenium import webdriver


# 定义fixture
@pytest.fixture()
def init():
    # 前置
    print("我是前置")
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    yield driver
    # 后置
    print("我是后置")
    driver.quit()


@pytest.fixture(scope="class")
def mycc():
    print("我是类级别的前置")
    yield
    print("我是类级别的后置")





# 只在淘宝这个方法初始化了
@pytest.mark.usefixtures("init")
def test_taobao():
    print("taobao.....")


class TestAA:

    def test_aa(self):
        print('aaaaaaaaa')

    # 测试用例
    def test_baidu(self, init):   # init = driver
        print("234333333")