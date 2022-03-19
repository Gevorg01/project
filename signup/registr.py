from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from string import digits,ascii_letters
from random import *


class registration:
    def __init__(self, driver):
        self.driver = driver

    def first_name(self):
        with open("names.txt", "r") as f:
            name = list(map(str, f.read().split()))
            name = "".join(choice(name))

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="first_name"]'))
        ).send_keys(name)

    def last_name(self):
        with open("surname.txt", "r") as f:
            surname = list(map(str, f.read().split()))
            surname = "".join(choice(surname))

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="last_name"]'))
        ).send_keys(surname.capitalize())

    def phone_number(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="phone"]'))
        ).send_keys('16465106465')

    def email(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]'))
        ).send_keys(Keys.CONTROL,'V')

    def password(self):
        s = ascii_letters+digits
        password = "".join(choice(s) for p in range(1,15))

        with open("user_info.txt", "w") as f:
            f.write(f'{password}\n')

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))
        ).send_keys(password)

    def choose(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//select[@id="account_type"]/option[text()="Customer"]'))
        ).click()

    def submit_form(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        ).click()