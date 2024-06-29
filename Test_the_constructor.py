import email
from telnetlib import EC
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants
from time import sleep

class TestBurgers():
    def test_constructor(self, driver):
        driver.find_element(By.XPATH, '//*[@fill="none"]').click()
        sleep(2)
        driver.find_element(By.XPATH, '//span[text()="Соусы"]').click()
        sleep(5)
        driver.find_element(By.XPATH, '//span[text()="Начинки"]').click()
        sleep(5)
        driver.find_element(By.XPATH, '//span[text()="Булки"]').click()
        sleep(5)
