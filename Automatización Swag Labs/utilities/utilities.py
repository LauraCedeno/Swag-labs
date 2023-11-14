import time
from selenium.webdriver.common.by import By
def browser_open(self):
    self.driver.get("https://www.saucedemo.com/")
def login(self, username, password):
    self.driver.find_element(by=By.XPATH, value="//input[@id='user-name']").send_keys(username)
    time.sleep(3)
    self.driver.find_element(by=By.XPATH, value="//input[@id='password']").send_keys(password)
    time.sleep(3)
    self.driver.find_element(by=By.XPATH, value="//input[@id='login-button']").click()
