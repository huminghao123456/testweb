# 订单提交测试(不能单独执行)
import time
import unittest

import utils
from page.cart_page import CartProxy
from page.index_page import IndexProxy
from page.my_order_list_page import MyOrderListProxy
from page.my_order_page import MyOrderProxy
from page.order_pay_page import OrderPayProxy
from utils import DriverUtil


class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象

        cls.index_proxy = IndexProxy()  # 首页业务操作对象
        cls.cart_proxy = CartProxy()  # 购物车业务操作对象
        cls.my_order_proxy = MyOrderProxy()  # 订单提交操作对象
        cls.my_order_list_proxy = MyOrderListProxy()  # 我的订单业务执行对象
        cls.order_pay_proxy = OrderPayProxy()  # 订单支付业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('http://www.tpshop.com/')

    def tearDown(self) -> None:
        time.sleep(3)

    def test01_submit_order(self):
        """提交订单测试"""

        # 点击我的购物车
        self.index_proxy.go_to_cart()
        # 去结算
        self.cart_proxy.go_to_check_order()
        # 设置睡眠,等待订单地址加载
        time.sleep(3)
        # 提交订单
        self.my_order_proxy.submit_order()
        # 断言判断测试结果
        result = utils.exist_text('订单提交成功，请您尽快付款')
        self.assertTrue(result)

    def test02_order_pay(self):
        """订单支付测试"""

        # 进入我的订单页面
        self.index_proxy.go_to_my_order_list()
        # 切换我的订单页面窗口
        utils.switch_to_new_window()

        # 点击待支付,进行支付
        self.my_order_list_proxy.go_to_order_pay()

        # 切换支付结果确认窗口
        utils.switch_to_new_window()

        # 选择支付方式,确认支付
        self.order_pay_proxy.pay()

        # 断言判定测试结果
        result = utils.exist_text('订单提交成功，我们将在第一时间给你发货')
        self.assertTrue(result)
