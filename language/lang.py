from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Language:
    def __init__(self, driver):
        self.driver = driver

    def click_on_lang(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="languages"]'))
        ).click()

    def choose_lang(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fadein"]/header/div[1]/div/div/div[2]/div/div/div[1]/div/ul/li[7]/a'))
        ).click()
        self.driver.get('https://www.phptravels.net/signup')