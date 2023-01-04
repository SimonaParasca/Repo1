import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

class CheckBoxTest(TestCase):
    CHECKBOXLINK = (By.LINK_TEXT, "checkboxes")
    HEADERCSS = (By.CSS_SELECTOR, "h3")
    FIRSTCHECKBOXXPATH = (By.XPATH)
    def setUp(self):
        self.firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.firefox.maximize_window()
        self.firefox.get("https://the-internet.herokuapp.com/checkboxes")
        self.firefox.find_element(*self.CHECKBOXLINK).click()
        self.firefox.implicitly_wait(5)
        # sleep(3)

    def tearDown(self):
        self.firefox.quit()
    def testCheckUrl(self):
        actual = self.firefox.current_url
        expected = "https://the-internet.herokuapp.com/checkboxes"
        self.assertEqual(expected, actual, "url incorect")

    @unittest.skip
    def testCheckHeader(self):
        actual = self.firefox.find_element(*self.HEADERCSS).text
        # actual = header.test
        expected = "Checkboxes"
        self.assertEqual(expected, actual,"header gresit")

    @unittest.skip
    def testCheckBoxSelected(self):
        pass

    @unittest.skip
    def testCheckBoxUnselected(self):
        pass

    def testSelectCheckBox1(self):
        box = self.firefox.find_element(*self.FIRSTCHECKBOXXPATH)
        box.click()
        self.assertTrue(box.is_selected(), "box unchecked")