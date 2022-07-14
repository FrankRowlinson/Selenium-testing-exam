from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_USERNAME = (By.ID, "#id_login-username")
    LOGIN_PASSWORD = (By.ID, "#id_login-password")

    REGISTER_USERNAME = (By.ID, "#id_registration-email")
    REGISTER_PASSWORD = (By.ID, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT = (By.ID, "#id_registration-password2")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    # should check with .endswith(), cause text contains jibberish
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main h1")
    ADDED_PRODUCT_TITLE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")