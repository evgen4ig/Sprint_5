import email
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants
from time import sleep


class TestBurgers():
    def test_login_using_the_Log_in_to_account(self, driver):
        email = 'evgeniy_zaytsev2027@yandex.ru'
        password = '123456'
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]/p[1]').click()
        sleep(2)  # Ожидание 2 секунды после первого клика

        driver.find_element(By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]').click()
        sleep(2)  # Ожидание 2 секунды после второго клика

        driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/section[2]/div[1]/button[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(email)
        sleep(2)  # Ожидание 2 секунды после ввода электронной почты для входа

        driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)

        driver.find_element(By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        sleep(2)  # Ожидание 2 секунды после нажатия кнопки входа




    def test_login_personal_account_button(self, driver):
        email = 'evgeniy_zaytsev2026@yandex.ru'
        password = '123456'
        driver.find_element(By.XPATH, '//*[@fill="none" ]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@href="/account"]').click()
        driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(email)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
        sleep(2)
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        sleep(5)


    def test_login_button_registracion(self,driver):
        email = 'evgeniy_zaytsev2026@yandex.ru'
        password = '123456'
        driver.find_element(By.XPATH, '//a[@href="/register"] ').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@class="Auth_link__1fOlj"] ').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
        sleep(2)
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        sleep(2)


    def test_login_password_recovery_from(self, driver):
        email = 'evgeniy_zaytsev2026@yandex.ru'
        password = '123456'
        driver.find_element(By.XPATH, '//*[@href="/forgot-password"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(email)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
        sleep(2)
        driver.find_element(By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        sleep(2)


