import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from language.lang import Language
from signup.registr import registration
from login.log_in import Login
from mail.tmp_mail import TmpMail
from hotels.hotel_search import hotels
from booking_form.booking import Booking


class Phptravels(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)
        self.driver.get("https://www.phptravels.net/signup")

    def test_case(self):
        lang = Language(self.driver)
        lang.click_on_lang()
        lang.choose_lang()
        sign = registration(self.driver)
        sign.first_name()
        sign.last_name()
        tmp = TmpMail(self.driver)
        tmp.open_window_mail()
        tmp.copy_mail()
        sign.email()
        sign.phone_number()
        sign.password()
        sign.choose()
        sign.submit_form()
        log = Login(self.driver)
        log.email()
        log.password()
        hotel = hotels(self.driver)
        hotel.click_on_hotel()
        hotel.choose_country()
        hotel.click_on_search_button()
        hotel.open_hotel_details()
        hotel.choose_hotel()
        hotel.book_hotel()
        booking = Booking(self.driver)
        booking.filling_name()
        booking.filling_email()
        booking.filling_retype_email()
        booking.submiting()
        booking.verifying_page()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
