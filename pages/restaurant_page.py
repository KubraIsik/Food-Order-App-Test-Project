from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RestaurantMenuPage:
    def __init__(self, driver):
        self.driver = driver 
        self.base_url = "https://www.yemeksepeti.com" # base url 
        self.CATEGORY_BUTTON_XPATH_TEMPLATE = "//li[@id='tabs__tab-{index}']/button"

        # for "Popüler" category
        self.MENU_ITEM_NAME_XPATH_TEMPLATE = "//*[@id=\"menu__category-id-0\"]/ul/li[{index}]/div[2]/div/h3/span" # start from 1
        self.MENU_ITEM_PRICE_XPATH_TEMPLATE = "//*[@id=\"menu__category-id-0\"]/ul/li[{index}]/div[2]/div/div/p" # start from 1

        # for another category: Kutu & Kova Menüler
        #self.MENU_ITEM_NAME_XPATH_TEMPLATE = "//*[@id=\"menu__category-id-3037386\"]/ul/li[{index}]/div[2]/div/h3/span" # start from 1
        #self.MENU_ITEM_PRICE_XPATH_TEMPLATE = "//*[@id=\"menu__category-id-3037386\"]/ul/li[{index}]/div[2]/div/div/p" # start from 1
        
        # name
        #//*[@id="menu__category-id-3037386"]/ul/li[1]/div[2]/div/h3/span
        # price
        # //*[@id="menu__category-id-3037386"]/ul/li[1]/div[2]/div/div/p
        
    def open(self, path =""):
        full_url = f"{self.base_url}/{path}"
        self.driver.get(full_url)

    # Address Choose Bar Element
    def get_choose_address_button_element(self):
        #address_element = "//*[@id=\"location-search-button\"]/span/span/span/div/span[2]/text()"
        address_element = "//*[@id=\"location-search-button\"]/span/span/span/div/span[2]/span"
        try:    
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, address_element))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHOOSE ADDRESS ELEMENT {address_element} could not be found within the specified timeout.")
    
    def get_choose_address_input_element(self):
        #address_element = "//*[@id=\"location-search-button\"]/span/span/span/div/span[2]/text()"
        address_input_element = "//*[@id=\"delivery-information-postal-index\"]"

        try:    
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, address_input_element))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHOOSE ADDRESS INPUT ELEMENT {address_input_element} could not be found within the specified timeout.")
    
    def get_use_address_button_element(self):
        address_use_element = "/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/button"
        try:    
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, address_use_element))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHOOSE ADDRESS USE BUTTON ELEMENT {address_use_element} could not be found within the specified timeout.")
    
    
    def get_category_elements(self, index): # index, 0 - num_of_category
        category_xpath = self.CATEGORY_BUTTON_XPATH_TEMPLATE.format(index=index)
        try:     # TRY EKLENDİ
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, category_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CATEGORY {category_xpath} could not be found within the specified timeout.")


    def get_search_input_element(self):
        search_input_xpath = "//input[@id=\'search-input\']"
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, search_input_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in SEARCH INPUT {search_input_xpath} could not be found within the specified timeout.")

    # ITEM ELEMENTS APPEARS AFTER SEARCH
    def get_search_item_elements(self):
        # after search gelenler böyle ilerliyor
        # item_xpath =  "//*[@id=\"menu__category-id--1\"]/ul/li[1]/button" # name, price, sepete ekle
        item_xpath = "//*[@id=\"menu__category-id--1\"]/ul/li[1]/div[2]/div[1]/h3/span"  # Name
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, item_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in SEARCH ITEM {item_xpath} could not be found within the specified timeout.")
    
    # ELEMENT APPEARS AFTER UNSUCCESSFUL SEARCH   
    def get_unsuccesful_search_element(self):
        element_css_selector = ".bds-c-empty-state__title"
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, element_css_selector))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in UNSUCCESFULL SEARCH ITEM {element_css_selector} could not be found within the specified timeout.")
    # WebDriverWait(self.driver, 0.5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".bds-c-empty-state__title")))
    # assert self.driver.find_element(By.CSS_SELECTOR, ".bds-c-empty-state__title").text == "Sonuç bulunamadı"
    
    # MENU ITEMS DISPLAYED WITHOUT SEARCH UNDER RELATED CATEGORIES
    # ELEMENT STORE: Name, price, Sepete Ekle
    def get_menu_item_elements(self): 
        item_xpath =  "//*[@id=\"menu__category-id-0\"]/ul/li[1]/button"
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, item_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in MENU ITEM {item_xpath} could not be found within the specified timeout.")

    # ELEMENT STORE: Name only
    def get_menu_item_name_elements(self, index): # Name
        item_name_xpath =  self.MENU_ITEM_NAME_XPATH_TEMPLATE.format(index=index)
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, item_name_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in MENU ITEM NAME {item_name_xpath} could not be found within the specified timeout.")

    # ELEMENT STORE: Price only
    def get_menu_item_price_elements(self, index): # price
        # after search gelenler böyle ilerliyor
        item_price_xpath =  self.MENU_ITEM_PRICE_XPATH_TEMPLATE.format(index=index)
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, item_price_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in MENU ITEM PRICE {item_price_xpath} could not be found within the specified timeout.")

    # ADD TO CART BUTTON (PLUS SIGN NEAR EACH)
    def get_add_to_cart_button_elements(self): 
        
        add_to_cart_item_xpath =  "//*[@id=\"menu__category-id-0\"]/ul/li[1]/button"
        #add_to_cart_item_css_selector = "#quantity-stepper-0-34032949 .fl-none"
        # By.CSS_SELECTOR, "#quantity-stepper-0-34032949 .fl-none"
        #//*[@id="quantity-stepper-0-34032949"]
        # //*[@id="quantity-stepper-0-34032949"] , arttır mı bu
        #//*[@id="menu__category-id-0"]/ul/li[1]/div[3]/div
        # //*[@id=\"menu__category-id-0\"]/ul/li[1]/button
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, add_to_cart_item_xpath))
                #EC.visibility_of_element_located((By.CSS_SELECTOR, add_to_cart_item_css_selector))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in ADD TO CART BUTTON ITEM {add_to_cart_item_xpath} could not be found within the specified timeout.")
    
    # SECOND ADD TO CART BUTTON (PLUS SIGN NEAR EACH)
    def get_second_add_to_cart_button_elements(self): 
        add_to_cart_item_xpath =  "/html/body/div[8]/div/div[2]/div/div/div/footer/div/div[2]/button/span"
        
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, add_to_cart_item_xpath))
                #EC.visibility_of_element_located((By.CSS_SELECTOR, add_to_cart_item_css_selector))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in SECOND ADD TO CART BUTTON ITEM {add_to_cart_item_xpath} could not be found within the specified timeout.")

    #
    def get_cart_item_elements(self):
        cart_item_xpath =  "//*[@id=\"cart\"]/div[2]/div[1]/div[3]/div/ul/li/div/section/div/div[2]/div[1]/p"
        # //*[@id="cart"]/div[2]/div[1]/div[3]/div/ul/li/div/section/button
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, cart_item_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CARD ITEM {cart_item_xpath} could not be found within the specified timeout.")
    
    # 
    def get_quantity_cart_item_elements(self):
        
        cart_item_quantity_xpath =  "//*[@id=\"quantity-stepper-34032949\"]/div[2]"
        
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, cart_item_quantity_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CART ITEM QUANTITY {cart_item_quantity_xpath} could not be found within the specified timeout.")
    
    # INCREASE QUANTITY CART ITEM
    def get_increase_quantity_cart_item_button_elements(self):
        increase_cart_item_quantity_xpath =  "//*[@id=\"quantity-stepper-34032949\"]/div[3]/button"

        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, increase_cart_item_quantity_xpath))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in INCREASE CART ITEM QUANTITY BUTTON  {increase_cart_item_quantity_xpath} could not be found within the specified timeout.")
    
    # DECREASE QUANTITY CART ITEM
    def get_decrease_quantity_cart_item_button_elements(self):
        decrease_cart_item_quantity_XPATH = "//*[@id=\"quantity-stepper-34032949\"]/div[1]/button"
        
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, decrease_cart_item_quantity_XPATH))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in DECREASE CART ITEM QUANTITY BUTTON  {decrease_cart_item_quantity_XPATH} could not be found within the specified timeout.")
    
    # TRASH BUTTON CART
    def get_trash_cart_button_elements(self):
        trash_cart_button_XPATH = "//*[@id=\"quantity-stepper-34032949\"]/div[1]/button"
        
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, trash_cart_button_XPATH))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in TRASH CART BUTTON  {trash_cart_button_XPATH} could not be found within the specified timeout.")
    
    # EMPTY CART ELEMENT
    def get_empty_cart_elements(self):
        empty_cart_XPATH = "//*[@id=\"cart\"]/div[2]/div[1]/div[2]/div/div[2]"
        
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, empty_cart_XPATH))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in EMPTY CART {empty_cart_XPATH} could not be found within the specified timeout.")
    
    # TOTAL PRICE CART ELEMENT
    def get_total_price_cart_element(self):
        total_price_cart_XPATH = "//*[@id=\"cart\"]/div[2]/div[2]/div/div/dl/dd"
        
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, total_price_cart_XPATH))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in TOTAL PRICE CART {total_price_cart_XPATH} could not be found within the specified timeout.")
    

    # CHECKOUT(CONFIRM) CART BUTTON ELEMENT
    def get_checkout_cart_button_element(self):
        checkout_cart_XPATH = "//*[@id=\"cart\"]/div[2]/div[2]/div/div/button"
        
        try: 
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, checkout_cart_XPATH))
            )
        except TimeoutException:
            raise AssertionError(f"Element located in CHECKOUT CART {checkout_cart_XPATH} could not be found within the specified timeout.")
    
    
    # second add to cart button
    # "/html/body/div[8]/div/div[2]/div/div/div/footer/div/div[2]/button/span"
    # 

      # Menu Item NAME
      #//*[@id="menu__category-id-0"]/ul/li[1]/div[2]/div/h3/span

      # for another category: Kutu & Kova Menüler
      #//*[@id="menu__category-id-3037386"]/ul/li[2]/div[2]/div/h3/span
      
      # Menu Item Price
      # //*[@id="menu__category-id-0"]/ul/li[1]/div[2]/div/div/p
      
      # //*[@id="menu__category-id-0"]/ul/li[2]/div[2]/div/h3/span
      #//*[@id="menu__category-id-0"]/ul/li[4]/div[2]/div/h3/span

      # xpathler böyle devam ediyor               "//*[@id=\"menu__category-id--1\"]/ul/li[2]/button"

        # avantajlı menüler altındaki bir item , Medium Burger Menü,  230 TL - Sepete Ekle
        #//*[@id="menu__category-id-2441884"]/ul/li[1]/button

        # bir sonraki category,kemikli-kemiksiz menüler altında bir item:
        # //*[@id="menu__category-id-3037385"]/ul/li[1]/button

        # bir sonraki category, kutu kova menüler
        # //*[@id="menu__category-id-3037386"]/ul/li[1]/button
        # category ismi kontrol etmeden, arama yaptıktan sonra, li[1] , li[2] şeklinde içinde gezinerek kontrol edebilirim
        # ama bu xpath ile istediğim text e ulaşabilecek miyim bakalım bi deneyeyim önce

        # sonra arama yaptırdığımda da bakayım, farklı categoryden arayınca nasıl geliyor.
        # avantajlı menülerden arattım:
        # //*[@id="menu__category-id--1"]/ul/li[1]/button , arama sonucu herkes category-id-1 oluor. başa getirildiğinde sanırım

        # menu price and etc.
        # category popüler ilk item
        # //*[@id="menu__category-id-0"]/ul/li[1]/button
        # //*[@id="menu__category-id-2441884"]/ul/li[1]/button