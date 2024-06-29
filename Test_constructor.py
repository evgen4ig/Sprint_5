from selenium.webdriver.common.by import By
from time import sleep

class TestBurgers():
    def test_constructor(self, driver):
        email = 'evgeniy_zaytsev2027@yandex.ru'
        password = '123456'

        driver.find_element(By.XPATH,  '//div[@class="AppHeader_header__logo__2D0X2"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@href="/account"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@href="/"]').click()
        sleep(2)

