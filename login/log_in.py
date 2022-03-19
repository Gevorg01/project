from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    def __init__(self, driver):
        self.driver = driver

    def email(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]'))
        ).send_keys(Keys.CONTROL, 'V')

    def password(self):
        with open("user_info.txt", "r") as f:
            read_pass = f.read()
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]'))
            ).send_keys(read_pass)

    def submit(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@class="btn btn-default btn-lg btn-block effect ladda-button waves-effect"]'))
        ).click()
