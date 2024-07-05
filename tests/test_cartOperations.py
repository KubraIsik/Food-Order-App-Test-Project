import pytest, time
from selenium import webdriver
from db_utils import *
from pages.restaurant_page import RestaurantMenuPage
from data.get_data import get_restaurant_paths # get restaurant_paths
from helpers import simulate_random_user_interactions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.orderCheckout_page import orderCheckoutPage

class TestCartOperations:
    #@pytest.mark.usefixtures("chrome_driver_init")
    def setup_method(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # Set a realistic User-Agent
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.page = orderCheckoutPage(self.driver)
        self.restaurant_paths = get_restaurant_paths() # bring restaurant paths id pairs e.g. restaurant_path for restaurant_id 1: f"restaurant/pc6b/burger-yiyelim-pc6b"
        # Set window size
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        
    def teardown_method(self):
        self.driver.quit()
    
    def test_add_to_cart(self):#, restaurant_id):
        # STEP 1: Open restaurant page
        restaurant_path = self.restaurant_paths[1] # bring restaurant path of restaurant_id 1
        self.page.open(restaurant_path)
        # apply random user interactions on the website
        simulate_random_user_interactions(self.driver)
        
        # STEP 2: Choose address
        self.choose_address()
        # STEP 3: Click first add to cart button
        self.add_item_to_cart1() # adding first item on the menu
        # STEP 4: Click second add to cart button
        self.add_item_to_cart2()
        # STEP 5: View item name text added to cart 
        first_menu_item_element = self.page.get_menu_item_name_elements(1) # bring first element located at the begining of the menu
        first_menu_item_text = first_menu_item_element.text
        # STEP 6: View item's name and quantity displayed on the cart
        displayed_cart_item, displayed_quantity_cart_item =self.view_cart()
        # EXPECTED RESULT: ITEM name displayed on the menu should match item name on the cart 
        assert  displayed_cart_item == first_menu_item_text, f"Menu Item {first_menu_item_text} not in the cart"
        # CHeCK quantity cart item after first add should be displayed as 1
        assert displayed_quantity_cart_item == "1" , f"Added first time but quantity of cart item {displayed_quantity_cart_item} "
        time.sleep(2)
    
    def test_increase_quantity_cart_item(self):
        # STEP 1: Open restaurant page
        restaurant_path = self.restaurant_paths[1] # bring restaurant path of restaurant_id 1
        self.page.open(restaurant_path)
        # apply random user interactions on the website
        simulate_random_user_interactions(self.driver)
        # STEP 2: Choose address
        self.choose_address()
        # STEP 3: Click first add to cart button
        self.add_item_to_cart1() # adding first item on the menu
        # STEP 4: Click second add to cart button
        self.add_item_to_cart2()
        # STEP 5: View item quantity text added to cart
        displayed_cart_item, displayed_quantity_cart_item =self.view_cart()
        # STEP 6 : Increase quantity of cart Item
        self.increase_cart_item_quantity()
        expected_quantity_cart_item = int(displayed_quantity_cart_item) + 1
        displayed_cart_item, updated_displayed_quantity_cart_item =self.view_cart()

        assert str(updated_displayed_quantity_cart_item) == str(expected_quantity_cart_item) , f"Quantity of cart item could not increased: {displayed_quantity_cart_item} "
        time.sleep(2)

    def test_decrease_quantity_cart_item(self):    
        # STEP 1: Open restaurant page
        restaurant_path = self.restaurant_paths[1] # bring restaurant path of restaurant_id "1"
        self.page.open(restaurant_path)
        # apply random user interactions on the website
        simulate_random_user_interactions(self.driver)
        # STEP 2: Choose address
        self.choose_address()
        # STEP 3: Click first add to cart button
        self.add_item_to_cart1() # adding first item on the menu
        # STEP 4: Click second add to cart button
        self.add_item_to_cart2()
        # STEP 5 : Increase quantity of cart Item
        self.increase_cart_item_quantity()
        # STEP 6: View item quantity text added to cart
        displayed_cart_item, displayed_quantity_cart_item =self.view_cart()
        # STEP 7: Decrease quantity of cart Item
        self.decrease_cart_item_quantity()
        expected_quantity_cart_item = int(displayed_quantity_cart_item) - 1
        displayed_cart_item, displayed_quantity_cart_item =self.view_cart() 

        assert str(displayed_quantity_cart_item) == str(expected_quantity_cart_item) , f"Quantity of cart item could not decreased: {displayed_quantity_cart_item} "
        time.sleep(2)

    def test_empty_cart(self):
        # STEP 1: Open restaurant page
        restaurant_path = self.restaurant_paths[1] # bring restaurant path of restaurant_id "1"
        self.page.open(restaurant_path)
        # apply random user interactions on the website
        simulate_random_user_interactions(self.driver)
        # STEP 2: Choose address
        self.choose_address()
        # STEP 3: Click first add to cart button
        self.add_item_to_cart1() # adding first item on the menu
        # STEP 4: Click second add to cart button
        self.add_item_to_cart2()
        # STEP 5: Click Trash button to remove item from cart 
        self.remove_item_from_cart()
        # EXPECTED RESULT: Empty cart message: "Sepetiniz şu an boş görünüyor."
        displayed_empty_cart = self.empty_cart()
        assert displayed_empty_cart == "Sepetiniz şu an boş görünüyor." , \
                    f"Cart is not empty or empty text could not found "
        time.sleep(2)
    
    def test_checkout_cart(self):
        # STEP 1: Open restaurant page
        restaurant_path = self.restaurant_paths[1] # bring restaurant path of restaurant_id "1"
        self.page.open(restaurant_path)
        # apply random user interactions on the website
        simulate_random_user_interactions(self.driver)
        # STEP 2: Choose address
        self.choose_address()
        # STEP 3: Click first add to cart button
        self.add_item_to_cart1() # adding first item on the menu
        # STEP 4: Click second add to cart button
        self.add_item_to_cart2()
        # STEP 5 : Increase quantity of cart Item
        self.increase_cart_item_quantity()
        # STEP 6 : View display cart item name and quantity of cart item
        displayed_cart_item_name, displayed_cart_item_quantity = self.view_cart()
        displayed_total_price_cart = self.view_total_price_cart() # displayed total price on the previous cart page 
        # STEP 7 : Click checkout cart button
        self.checkout_cart_button()
        # EXPECTED RESULT : Order Checkout Page open by checking CART TITLE
        displayed_order_checkout_cart_title = self.order_checkout_cart_title()
        assert displayed_order_checkout_cart_title == "Siparişiniz ", "Order Checkout page could not opened."

        # EXPECTED RESULT : Order Checkout CART TOTAL PRICE equals on previous page on the Cart 
        displayed_order_checkout_cart_total_price = self.order_checkout_cart_total_price()
        assert displayed_order_checkout_cart_total_price == displayed_total_price_cart, \
                "Displayed TOTAL PRICE on the cart and the cart on the checkout page is not equal"
        # EXPECTED RESULT : Order Checkout CART ITEM NAME equals on previous page on the Cart
        displayed_order_checkout_cart_name = self.order_checkout_cart_name()
        assert displayed_order_checkout_cart_name == displayed_cart_item_name, \
                "Displayed CART ITEM NAME on the cart and the cart on the checkout page is not equal"
        # EXPECTED RESULT : Order Checkout CART ITEM QUANTITY equals on previous page on the Cart
        displayed_order_checkout_cart_quantity = self.order_checkout_cart_quantity()
        assert displayed_order_checkout_cart_quantity == displayed_cart_item_quantity, \
                "Displayed CART ITEM QUANTITY on the cart and the cart on the checkout page is not equal"

    # CHOOSE ADDRESS
    def choose_address(self):
        choose_address_element = self.page.get_choose_address_button_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", choose_address_element)
        choose_address_element.click()
        time.sleep(2)

        choose_address_input_element = self.page.get_choose_address_input_element()
        choose_address_input_element.click()
        time.sleep(2)
        choose_address_input_element.send_keys("Akşemsettin, Fevzi Paşa Cd., 133, 34080 Fatih İstanbul")
        time.sleep(2)

        use_address_button_element = self.page.get_use_address_button_element()
        use_address_button_element.click()
        time.sleep(2)

    def add_item_to_cart1(self):
        # First add to cart button
        add_to_cart_button_element = self.page.get_add_to_cart_button_elements()
        self.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button_element)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", add_to_cart_button_element)
        time.sleep(2)

    def add_item_to_cart2(self):    
        # Second add to cart button 
        second_add_to_cart_button_element = self.page.get_second_add_to_cart_button_elements()
        self.driver.execute_script("arguments[0].scrollIntoView();", second_add_to_cart_button_element)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", second_add_to_cart_button_element)
        time.sleep(2)

    def view_cart(self):
        # cart item name element
        cart_item_element = self.page. get_cart_item_elements()
        self.driver.execute_script("arguments[0].scrollIntoView();", cart_item_element)
        time.sleep(2)
        # cart item quantity element
        quantity_cart_item_element = self.page.get_quantity_cart_item_elements()
        # displayed cart item name text & displayed cart item quantity text
        return cart_item_element.text, quantity_cart_item_element.text
    
    def view_total_price_cart(self):
        # cart total price element
        cart_total_price_element = self.page. get_total_price_cart_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", cart_total_price_element)
        return cart_total_price_element.text
    
    def increase_cart_item_quantity(self):
        # increase quantity of cart item
        increase_quantity_cart_item_button_element = self.page.get_increase_quantity_cart_item_button_elements()
        self.driver.execute_script("arguments[0].scrollIntoView();", increase_quantity_cart_item_button_element)
        self.driver.execute_script("arguments[0].click();", increase_quantity_cart_item_button_element)
        time.sleep(2)

    def decrease_cart_item_quantity(self):
        # decrease quantity of cart item
        decrease_quantity_cart_item_button_element = self.page.get_decrease_quantity_cart_item_button_elements()
        self.driver.execute_script("arguments[0].scrollIntoView();", decrease_quantity_cart_item_button_element)
        self.driver.execute_script("arguments[0].click();", decrease_quantity_cart_item_button_element)
        time.sleep(2)

    def remove_item_from_cart(self):
        # TRASH cart button
        trash_cart_button_element = self.page.get_trash_cart_button_elements()
        self.driver.execute_script("arguments[0].scrollIntoView();", trash_cart_button_element)
        self.driver.execute_script("arguments[0].click();", trash_cart_button_element)
        time.sleep(2)

    def empty_cart(self):
        # EMPTY CART ELEMENT text
        empty_cart_element = self.page.get_empty_cart_elements()
        self.driver.execute_script("arguments[0].scrollIntoView();", empty_cart_element)
        displayed_empty_cart = empty_cart_element.text
        time.sleep(2)
        return displayed_empty_cart

    # CHECKOUT CART BUTTON
    def checkout_cart_button(self):
        checkout_cart_button_element = self.page.get_checkout_cart_button_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", checkout_cart_button_element)
        self.driver.execute_script("arguments[0].click();", checkout_cart_button_element)

    # ORDER CHECKOUT CART TITLE
    def order_checkout_cart_title(self):
        order_checkout_cart_title_element = self.page.get_order_checkout_cart_title_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", order_checkout_cart_title_element)
        return order_checkout_cart_title_element.text
    
    # ORDER CHECKOUT CART TOTAL PRICE
    def order_checkout_cart_total_price(self):
        order_checkout_cart_total_price_element = self.page.get_order_checkout_cart_total_price_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", order_checkout_cart_total_price_element)
        return order_checkout_cart_total_price_element.text
    
    # ORDER CHECKOUT CART NAME
    def order_checkout_cart_name(self):
        order_checkout_cart_name_element = self.page.get_order_checkout_cart_item_name_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", order_checkout_cart_name_element)
        return order_checkout_cart_name_element.text

    # ORDER CHECKOUT CART QUANTITY
    def order_checkout_cart_quantity(self):
        order_checkout_cart_quantity_element = self.page.get_order_checkout_cart_quantity_element()
        self.driver.execute_script("arguments[0].scrollIntoView();", order_checkout_cart_quantity_element)
        return order_checkout_cart_quantity_element.text

    

    