import email
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants
from time import sleep


class TestBurgers():
    def test_ls_account(self, driver):
        email = 'evgeniy_zaytsev2027@yandex.ru'
        password = '123456'
        sleep(2)
        driver.find_element(By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@href="/account"]').click()
        sleep(2)
