from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking:
    def __init__(self, driver):
        self.driver = driver

    def filling_name(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="firstName_lastName"]'))
        ).send_keys('a a')

    def filling_email(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="email"]'))
        ).send_keys('edmwcu@mailto.plus')

    def filling_retype_email(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="retypeEmail"]'))
        ).send_keys('edmwcu@mailto.plus')

    def submiting(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="SiteContent"]/div/div[1]/div[6]/div/button'))
        ).click()

    def verifying_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body'))
        ).click()
        self.driver.get_screenshot_as_file("screenshot/screen.png")
