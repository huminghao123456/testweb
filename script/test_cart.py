# 测试添加商品到购物车
import unittest

from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.index_page import IndexProxy
from utils import DriverUtil


class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象

        cls.index_proxy = IndexProxy()  # 首页业务操作对象
        cls.goods_search_proxy = GoodsSearchProxy()  # 商品搜索业务操作对象
        cls.goods_detail_proxy = GoodsDetailProxy()  # 商品详情业务操作对象

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://www.tpshop.com/')
        # 跳转登录页
        # self.index_proxy.go_to_login()

    def test_join_goods_to_cart(self):
        """添加商品到购物车测试"""
        goods_name = '小米手机5'

        # 搜索商品
        self.index_proxy.go_to_goods_search(goods_name)
        # 跳转商品详情
        self.goods_search_proxy.go_to_goods_detail(goods_name)
        # 添加商品到购物车
        self.goods_detail_proxy.join_goods_to_cart()

        # 断言判断测试结果
        result = self.goods_detail_proxy.get_add_cart_result('添加成功')
        self.assertTrue(result)
