from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class hotels:
    def __init__(self, driver):
        self.driver = driver

    def click_on_hotel(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a'))
        ).click()

    def choose_country(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="selection"]//descendant::span'))
        ).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fadein"]/span/span/span[1]/input'))
        ).send_keys('Yerevan', Keys.ENTER)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//li[@class="select2-results__option select2-results__option--highlighted"]'))
        ).click()

    def click_on_search_button(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="submit"]'))
        ).click()

    def open_hotel_details(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cascade hotel"]/div/div[2]/div/div[2]/div/a'))
        ).click()

    def choose_hotel(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="SearchBoxContainer"]/div/div/div[4]/div'))
        ).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="contentContainer"]/div[3]/ol/li[2]/div/a/div/div[3]/div/div[3]/button/div/div/div/span'))
        ).click()

    def book_hotel(self):
        self.driver.switch_to.window(self.driver.window_handles[3])
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body'))
        ).send_keys(Keys.ARROW_DOWN)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="ChildRoom-Ch8IlIa5CBACIAIo5PhAMAQ4AkABSgcxRDFOXzFOUJgFEgIIARoGEAIoBDAB"]/div/div[5]/div[1]/div/div[1]/button'))
        ).click()
