from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TmpMail:
    def __init__(self, driver):
        self.driver = driver

    def open_window_mail(self):
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://tempmail.plus/ru/#!")

    def copy_mail(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="pre_copy"]'))
        ).click()
        self.driver.switch_to.window(self.driver.window_handles[0])

