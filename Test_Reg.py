import email
from telnetlib import EC
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants
from time import sleep

class TestBurgers():
    def test_registration(self, driver):
        name = 'Evgeniy1'
        email = 'evgeniy_zaytsev333029yandex.ru'
        password = '123456'
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/a[1]/p[1]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//a[@class="Auth_link__1fOlj"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]').send_keys(name)
        driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@type="password"] ').send_keys(password)
        sleep(10)
        driver.find_element(By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"] ').click()
        driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(email)
        driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//a[@href="/account"]').click()
        sleep(2)
        print(email)
        print(name)
        print(password)


    def test_correct_password(self, driver):
        email = 'evgeniy_zaytsev2024yandex.ru'
        password = '123456'
        sleep(2)
        driver.find_element(By.XPATH, '//*[@type="text"]' ).send_keys(email)
        driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
        driver.find_element(By.XPATH,'//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        
    def test_uncorrect_password(self, driver):
        email = 'evgeniy_zaytsev2024yandex.ru'
        password = '12'
        sleep(5)
        driver.find_element(By.XPATH, '//*[@type="text"]').send_keys(email)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(password)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]').click()
        sleep(2)
        assert isinstance(driver.find_element(By.XPATH, '//p[@class="input__error text_type_main-default"]').text, object)
        driver.find_element(By.XPATH, '//p[@class="input__error text_type_main-default"]').text


