
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import logging


class BasePage:

    def __init__(self, driver: WebDriver):
        # 初始化drvier
        self.driver = driver

    def wait_ele_visible(self, loc, img_name, timeout=20, poll_fre=0.5):
        logging.info("等待 {} 元素可见。".format(loc))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            # 失败截图- 写入日志
            self.save_page_shot(img_name)
            logging.exception("等待元素可见失败：")
            raise

    # 查找元素
    def get_element(self, loc, img_name):
        logging.info("在{} 查找元素： {}。".format(img_name, loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_page_shot(img_name)
            logging.exception("查找元素失败")
            raise
        else:
            return ele

    # 点击元素
    def click_element(self, loc, img_name, timeout=20, poll_fre=0.5):
        logging.info("在{} 点击{} 元素.".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        try:
            ele.click()
        except:
            self.save_page_shot(img_name)
            logging.exception("点击元素失败")
            raise

    # 元素的输入操作
    def input_text(self, loc, value, img_name, timeout=20, poll_fre=0.5):
        logging.info("在{} 往元素{} 输入文本值：{}.".format(img_name, loc, value))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        try:
            ele.send_keys(value)
        except:
            self.save_page_shot(img_name)
            logging.exception("元素输入文本失败")
            raise

    # 获取元素属性
    def get_ele_attribute(self, loc, attr_name, img_name, timeout=20, poll_fre=0.5):
        logging.info("在{} 获取元素{} 的属性值".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        try:
            value = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_name)
            logging.exception("获取元素的属性失败")
            raise
        else:
            logging.info("属性值为：{}".format(value))
            return value

    # 获取元素的文本值
    def get_ele_text(self, loc, img_name, timeout=20, poll_fre=0.5):
        logging.info("在{} 获取元素{}的文本内容".format(img_name, loc))
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.get_element(loc, img_name)
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            logging.exception("获取元素的文本失败")
            raise
        else:
            logging.info("文本值为：{}".format(text))
            return text

    def save_page_shot(self, img_name):
        # 将图片存储到outputs的的screenshot目录下
        # 命名规范： 页面名称_页面行为_时间.png
        # 文件完整名称 = Outputs的screenshots
        file_name = "{}_{}.png".format(img_name, "当前时间")
        self.driver.save_screenshot("图片存储图片" + file_name)
        logging.info("页面图片保存在: {}".format("图片存储图片" + file_name))
