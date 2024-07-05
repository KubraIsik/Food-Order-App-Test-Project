from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.restaurant_page import RestaurantMenuPage

class orderCheckoutPage(RestaurantMenuPage):
    def __init__(self,driver):
        super().__init__(driver)
        
        self.title_checkout_cart_element = "//*[@id=\"cart\"]/div[2]/div/h3"
        self.price_checkout_cart_element = "//*[@id=\"cart\"]/div[2]/div/div[3]/div[3]/span"
        self.quantity_item_checkout_cart_element = "//*[@id=\"cart\"]/div[2]/div/div[2]/div/div/span[1]"
        self.name_item_checkout_cart_element = "//*[@id=\"cart\"]/div[2]/div/div[2]/div/div/div/span"

    # Checkout Cart TITLE Element
    def get_order_checkout_cart_title_element(self):
        try:    
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.title_checkout_cart_element))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHECKOUT CART TITLE ELEMENT {self.title_checkout_cart_element} could not be found within the specified timeout.")
    
    # Checkout Cart TOTAL PRICE Element
    def get_order_checkout_cart_total_price_element(self):
        try:    
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.price_checkout_cart_element))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHECKOUT CART TOTAL PRICE ELEMENT {self.price_checkout_cart_element} could not be found within the specified timeout.")
        
    # CHECKOUT CART ITEM QUANTITY
    def get_order_checkout_cart_item_quantity_element(self):
        try:    
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.quantity_item_checkout_cart_element))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHECKOUT CART ITEM QUANTITY ELEMENT {self.quantity_item_checkout_cart_element} could not be found within the specified timeout.")
        
    # CHECKOUT CART ITEM NAME
    def get_order_checkout_cart_item_name_element(self):
        try:    
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.name_item_checkout_cart_element))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHECKOUT CART ITEM QUANTITY ELEMENT {self.name_item_checkout_cart_element} could not be found within the specified timeout.")
        

