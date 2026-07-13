import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class GoogleTestCase(unittest.TestCase):

    def setUp(self):

        options = Options()

        self.browser = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=options
        )

        self.addCleanup(self.browser.quit)

    def test_page(self):

        self.browser.get("https://example.com")

        element = self.browser.find_element(By.TAG_NAME, "p")

        print(element.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)