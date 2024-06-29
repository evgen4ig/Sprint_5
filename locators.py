from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.XPATH, '//*[@type="text"]')
    # Ввод Email
    PASSWORD = (By.XPATH, '//*[@type="password"]')
    # Ввод пароля
    AUTH_BUTTON = (By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    # Кнопка "Войти"

