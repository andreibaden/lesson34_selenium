import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SimpleGoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def testSearchSelenium(self):
        expected_title = "selenium"

        self.driver.get("https://www.google.com")
        question_input = self.driver.find_element(By.NAME, "q")
        question_input.send_keys("selenium")
        question_input.send_keys(Keys.ENTER)

        actual_title = self.driver.title

        self.assertIn(expected_title, actual_title)


if __name__ == "__main__":
    unittest.main()
