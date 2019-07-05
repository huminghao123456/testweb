# 订单支付页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderPayPage(BasePage):
    """订单支付-对象库层"""

    def __init__(self):
        super().__init__()

        self.cod = (By.CSS_SELECTOR, '[value="pay_code=cod"]')  # 货到付款复选框
        self.confirm_pay = (By.LINK_TEXT, '确认支付方式')  # 支付方式确认

    def find_cod(self):
        """定位货到付款方法"""
        return self.find_element(self.cod)

    def find_confirm_pay(self):
        """定位确认付款方法"""
        return self.find_element(self.confirm_pay)


class OrderPayHandle(BaseHandle):
    """订单支付-操作层"""

    def __init__(self):
        self.order_pay_page = OrderPayPage()

    def click_cod(self):
        """点击货到付款方法"""
        self.order_pay_page.find_cod().click()

    def click_confirm_pay(self):
        """点击确认付款方法"""
        self.order_pay_page.find_confirm_pay().click()


class OrderPayProxy(object):
    """订单支付-业务层"""

    def __init__(self):
        self.order_pay_handle = OrderPayHandle()

    def pay(self):
        """订单支付方法"""
        # 选择付款方式
        self.order_pay_handle.click_cod()
        # 确认支付
        self.order_pay_handle.click_confirm_pay()
