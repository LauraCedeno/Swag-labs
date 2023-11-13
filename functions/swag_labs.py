from utilities import utilities
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Swag_labs:
    def __init__(self):
        serv = Service(ChromeDriverManager().install())
        opt = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=serv, options=opt)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def login(self, user, pwd):
        utilities.browser_open(self)
        utilities.login(self, username=user, password=pwd)
        time.sleep(3)

    def add_to_card(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)

    def shopping_cart_page(self):
        self.driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']").click()
        time.sleep(3)

    def remove_product(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='remove-sauce-labs-backpack']").click()
        time.sleep(3)

    def checkout(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='checkout']").click()
        time.sleep(3)

    def shipment_information(self, first_name, last_name, postal_code):
        self.driver.find_element(by=By.XPATH, value="//input[@id='continue']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//input[@id='first-name']").send_keys(first_name)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//input[@id='last-name']").send_keys(last_name)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//input[@id='postal-code']").send_keys(postal_code)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//input[@id='continue']").click()
        time.sleep(3)

    def finalize_purchase(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='finish']").click()
        time.sleep(3)

    def back_to_products(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='back-to-products']").click()
        time.sleep(3)

    def product_detail(self):
        self.driver.find_element(by=By.XPATH, value="(//div[@class='inventory_item_name '])[1]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(3)

    def reset_app_state(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//a[contains(@id,'reset_sidebar_link')]").click()
        time.sleep(3)

    def about(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//a[@id='about_sidebar_link']").click()
        time.sleep(3)

    def logout(self):
        self.driver.find_element(by=By.XPATH, value="//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//a[@id='logout_sidebar_link']").click()
        time.sleep(3)

    def close(self):
        self.driver.close()