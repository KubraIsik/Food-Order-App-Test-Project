import pytest, time
from selenium import webdriver
from db_utils import *
from pages.restaurant_page import RestaurantMenuPage
from data.get_data import get_restaurant_paths, get_search_items
from helpers import simulate_random_user_interactions, format_word
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRestaurantMenu:
    #@pytest.mark.usefixtures("chrome_driver_init")
    def setup_method(self):

        chrome_options = webdriver.ChromeOptions()
        # to avoid being blocked by website during automation runs
        #chrome_options.add_argument("--incognito")
        #chrome_options.add_argument("--headless")  # Run browser in headless mode
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("--disable-dev-shm-usage")
        #chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # Set a realistic User-Agent
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        self.page = RestaurantMenuPage(self.driver)
        #self.page.open("restaurant/pc6b/burger-yiyelim-pc6b") # burger yiyelim
        self.restaurant_paths = get_restaurant_paths() # bring restaurant paths e.g. restaurant_path: f"restaurant/pc6b/burger-yiyelim-pc6b" 
        # Set window size
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        
    def teardown_method(self):
        self.driver.quit()

    # check categories for each restaurant by restaurant_id s retrieved from db and navigate each restaurant page by parametrize
    @pytest.mark.parametrize("restaurant_id,",fetch_restaurant_ids(get_db_connection().cursor()))
    def test_displayed_categories_match(self, restaurant_id):
        # Navigate restaurant page and open
        self.page.open(self.restaurant_paths[restaurant_id]) # bring restaurant path from restaurant_id : restaurant_path pairs
        # e.g. restaurant_path for restaurant_id 1: f"restaurant/pc6b/burger-yiyelim-pc6b" 
        simulate_random_user_interactions(self.driver)

        expected_categories = fetch_categories_for_restaurant(get_db_connection().cursor(), restaurant_id) #restaurant_id)
        #displayed_categories = [element.text for element in self.page.get_category_elements()]
        num_categories_restaurant = fetch_count_categories_for_restaurant(get_db_connection().cursor(), restaurant_id)# restaurant_id)
           
        for i in range(num_categories_restaurant): # 0 - 9, category var restaurant_id 1 için 
            category_element = self.page.get_category_elements(i) # pass index as argument for locator to navigate all categories
            self.driver.execute_script("arguments[0].scrollIntoView();", category_element)       
            
            expected_category = expected_categories[i] 
            displayed_category = category_element.text 
            
            assert displayed_category == expected_category, \
                f"Categories for restaurant {self.restaurant_id} do not match . Expected: {expected_category}, Displayed: {displayed_category}"
      

    @pytest.mark.parametrize("restaurant_id,",fetch_restaurant_ids(get_db_connection().cursor()))
    def test_displayed_menu_items_match(self, restaurant_id):
        # Navigate restaurant page and open
        self.page.open(self.restaurant_paths[restaurant_id]) # bring restaurant path from restaurant_id : restaurant_path pairs
        # e.g. restaurant_path for restaurant_id 1: f"restaurant/pc6b/burger-yiyelim-pc6b" 
        simulate_random_user_interactions(self.driver)
        
        # Retrieve Menu Items NAMES and PRICES From DB
        expected_menu_name_price = fetch_menu_items_for_restaurant(get_db_connection().cursor(), restaurant_id)
        # Bring number of items in the menu for related category_id 
        num_menu_items = fetch_count_menu_items_for_restaurant(get_db_connection().cursor(), restaurant_id)
        for i in range(1,num_menu_items): # 1 - number of menu items in selected category
            menu_item_name_element = self.page.get_menu_item_name_elements(i) # pass index as argument for locator to navigate all categories
            menu_item_price_element = self.page.get_menu_item_price_elements(i)

            # Scroll to the menu item element
            self.driver.execute_script("arguments[0].scrollIntoView();", menu_item_name_element)

            displayed_menu_item_name = menu_item_name_element.text
            displayed_menu_item_price = menu_item_price_element.text

            expected_menu_item_name = expected_menu_name_price[i-1][0]
            expected_menu_item_price = expected_menu_name_price[i-1][1]

            assert displayed_menu_item_name == expected_menu_item_name, \
                f"Displayed menu item name: {displayed_menu_item_name}, Expected menu item name:{expected_menu_item_name}"
            
            assert displayed_menu_item_price == expected_menu_item_price, \
                f"Displayed menu item name: {displayed_menu_item_price}, Expected menu item name:{expected_menu_item_price}"

    # CHECK SUCCESSFUL SEARCH RESULT MATCH  
    #@pytest.mark.skip()
    @pytest.mark.parametrize("restaurant_id,",fetch_restaurant_ids(get_db_connection().cursor()))
    def test_succesfull_search(self, restaurant_id):
        # Navigate restaurant page and open
        self.page.open(self.restaurant_paths[restaurant_id]) # bring restaurant path from restaurant_id : restaurant_path pairs
        # e.g. restaurant_path for restaurant_id 1: f"restaurant/pc6b/burger-yiyelim-pc6b" 
        simulate_random_user_interactions(self.driver)
        
        search_input_element = self.page.get_search_input_element()
        # not_found_search_items
        search_items = get_search_items("found_search_items")
        
        for expected_word in search_items:
            search_input_element.send_keys(expected_word)
            self.driver.execute_script("arguments[0].scrollIntoView();", search_input_element)
            time.sleep(5)

            menu_item_element = self.page.get_search_item_elements()
            # Scroll to the menu item element
            self.driver.execute_script("arguments[0].scrollIntoView();", menu_item_element)
            displayed_menu_item = menu_item_element.text
            assert displayed_menu_item == format_word(expected_word),\
                         f"Search word {expected_word} and displayed item text does not match {menu_item_element}"
            search_input_element.clear()
        
    # CHECK UNSUCCESSFUL SEARCH RESULT      
    @pytest.mark.parametrize("restaurant_id,",fetch_restaurant_ids(get_db_connection().cursor()))
    def test_unsuccesfull_search(self, restaurant_id):
        # Navigate restaurant page and open
        self.page.open(self.restaurant_paths[restaurant_id]) # bring restaurant path from restaurant_id : restaurant_path pairs
        # e.g. restaurant_path for restaurant_id 1: f"restaurant/pc6b/burger-yiyelim-pc6b" 
        simulate_random_user_interactions(self.driver)
        
        search_input_element = self.page.get_search_input_element()
        search_items = get_search_items("not_found_search_items")
        
        for expected_word in search_items:
            search_input_element.send_keys(expected_word)
            self.driver.execute_script("arguments[0].scrollIntoView();", search_input_element)
            time.sleep(5)
        
            menu_item_element = self.page.get_unsuccesful_search_element()
            displayed_menu_item = menu_item_element.text
            assert displayed_menu_item == "Sonuç bulunamadı", \
                     f" {expected_word} Sonuç Bulunamadı yazısı görüntülenemiyor."
            # Clear the input field
            search_input_element.clear()


        
        
       



        
        
        

        
