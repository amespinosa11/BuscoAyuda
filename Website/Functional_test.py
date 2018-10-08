from unittest import TestCase
from selenium import webdriver


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn("Busco Ayuda", self.browser.title)