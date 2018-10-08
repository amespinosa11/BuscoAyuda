from selenium import webdriver
import unittest

class FunctionalTest(unittest.TestCase):
    def setUp(self):
    	self.browser = webdriver.Chrome("C:\\Selenium\\chromedriver.exe")
    	self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)



if __name__ == '__main__':
    unittest.main()