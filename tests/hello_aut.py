import unittest
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By


class AutTest(unittest.TestCase):

    def setUp(self):

        # Browser default
        browser = "firefox"

        # Browser dikirim dari GitHub Actions
        if len(sys.argv) > 2:
            browser = sys.argv[2]

        # Pilih browser
        if browser == "firefox":
            options = webdriver.FirefoxOptions()

        elif browser == "chrome":
            options = webdriver.ChromeOptions()

        elif browser == "edge":
            options = webdriver.EdgeOptions()

        else:
            raise Exception(f"Browser '{browser}' tidak didukung.")

        # Ignore SSL
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")

        # Selenium Hub
        server = "http://localhost:4444"

        self.browser = webdriver.Remote(
            command_executor=server,
            options=options
        )

        self.addCleanup(self.browser.quit)

    def test_homepage(self):

        # URL default
        url = "http://localhost"

        # URL dikirim dari workflow
        if len(sys.argv) > 1:
            url = sys.argv[1]

        self.browser.get(url)

        # Screenshot
        self.browser.save_screenshot("homepage.png")

        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, "p")

        self.assertIn(expected_result, actual_result.text)


if __name__ == "__main__":
    unittest.main(
        argv=["first-arg-is-ignored"],
        verbosity=2,
        warnings="ignore"
    )