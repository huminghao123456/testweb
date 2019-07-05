# 商品搜索页面
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class GoodsSearchPage(BasePage):
    """搜索商品-对象库层"""

    def __init__(self):
        super().__init__()

        # self.goods = (By.XPATH, '//div[@class="shop_name2"]/a[contains(text(),"小米手机5")]')  # 目标商品
        self.goods = (By.XPATH, '//div[@class="shop_name2"]/a[contains(text(),"{}")]')  # 目标商品

    def find_goods(self, kw):
        """定位搜索到的商品方法"""
        location = (self.goods[0], self.goods[1].format(kw))
        return self.find_element(location)


class GoodsSearchHandle(BaseHandle):
    """搜索商品-操作层"""

    def __init__(self):
        self.goods_search_page = GoodsSearchPage()

    def click_goods(self, kw):
        """点击搜索到的商品方法"""
        self.goods_search_page.find_goods(kw).click()


class GoodsSearchProxy(object):
    """搜索商品-业务层"""

    def __init__(self):
        self.goods_search_handle = GoodsSearchHandle()

    def go_to_goods_detail(self, kw):
        """跳转商品详情页方法"""
        self.goods_search_handle.click_goods(kw)
