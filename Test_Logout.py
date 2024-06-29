from selenium.webdriver.common.by import By
from time import sleep

class TestBurgers():
    def test_logout(self, driver):
        email = 'evgeniy_zaytsev2027@yandex.ru'
        password = '123456'
        driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(email)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@type="password"] ').send_keys(password)
        driver.find_element(By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        driver.find_element(By.XPATH, '//*[@href="/account"] ').click()



