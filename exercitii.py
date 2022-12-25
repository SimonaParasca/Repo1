from unittest import TestCase
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test(TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        # self.chrome.get('https://www.phptravels.net/')
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        # expected = 'https://phptravels.net/'
        expected = 'https://the-internet.herokuapp.com/'
        self.assertEqual(expected, actual, 'URL incorect')

    # def testSearchByCity(self):
    #     self.chrome.implicitly_wait(2)
    #     search = self.chrome.find_element(By.ID, 'select2-hotels_city-container')
    #     search.click()
    #     self.chrome.find_element(By.CLASS_NAME, 'select2-search__field').send_keys('Bucharest')
    #     self.chrome.implicitly_wait(3)
    #     expectedValue = 'Bucharest,Romania'
    #     result = self.chrome.find_element(By.CLASS_NAME, 'select2-results__option select2-results__option--highlighted')
    #     actual = result.text
    #     self.assertEqual(expectedValue, actual, 'Rezultat incorect')

    def testAddRemoveLinkTxt_URL(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/add_remove_elements/'
        self.assertEqual(expected, actual, 'url incorect')

    def testHeader(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        result = self.chrome.find_element(By.CSS_SELECTOR, 'h3')
        expected = 'Add/Remove Elements'
        actual = result.text
        self.assertEqual(expected, actual, 'text incorect')

    def testButton(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        result = self.chrome.find_element(By.ID, 'elements')
        expected = 'Delete'
        actual = result.text
        self.assertEqual(expected, actual, 'text incorect')

    def testPressAddElement(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        actual = self.chrome.find_elements(By.CSS_SELECTOR, 'button.added-manually')
        expected = 3
        self.assertEqual(expected, len(actual), 'inccorect')