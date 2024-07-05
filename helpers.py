import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def simulate_random_user_interactions(driver):
        # Simulate scrolling down using JavaScript
        scroll_script1 = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(scroll_script1)
        time.sleep(2)
        scroll_script2 = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(scroll_script2)
        time.sleep(2)  # Wait for page to load after scroll

        # Simulate mouse hover action
        element_to_hover_over = driver.find_element(By.XPATH, "//input[@id=\'search-input\']")
            
        ActionChains(driver).move_to_element(element_to_hover_over).perform()
        time.sleep(1)  # Wait for hover effect to apply

# remove special characters, numbers and spaces
# make string only first alphabet is capital
def format_word(input_string):
        import re

        clean_and_format_string = lambda s: re.sub(r'[^a-zA-Z]', '', s).capitalize()
        return clean_and_format_string(input_string)
