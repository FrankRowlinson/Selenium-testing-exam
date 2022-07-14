from pages.product_page import ProductPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
urls = [f"{link}?promo=offer{i}" \
    if i != 7 else pytest.param(f"{link}?promo=offer{i}", marks=pytest.mark.xfail) \
         for i in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_equal_product_price_and_basket_total()
    page.should_be_correct_added_product()