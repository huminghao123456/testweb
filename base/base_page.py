# page 基类
from utils import DriverUtil


class BasePage(object):
    """page基类"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()

    def find_element(self, location):
        """
        元素定位方法(利用拆包获取元组属性值)
        :param location: 元素对象定位方法类型和属性值
        :return: 元素对象
        """
        return self.driver.find_element(*location)


class BaseHandle(object):
    """handle 基类"""

    def input_text(self, element, text):
        """
        输入框元素清空方法和输入方法封装
        :param element: 元素对象
        :param text: 输入的文本信息
        """
        element.clear()
        element.send_keys(text)
