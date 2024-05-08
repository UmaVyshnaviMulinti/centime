from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

class CartAutomation:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.url = url
        self.product_names = []
        self.driver.implicitly_wait(10)
    def collect_product_names(self):
        self.driver.get(self.url)

        self.product_names = [element.text for element in self.driver.find_elements(By.XPATH, "//div[@class='woocommerce']//h3")]
        print("Products on the homepage:", self.product_names)

    def add_products_to_cart(self):
        add_to_cart_buttons = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart']"))
        )

        for button in add_to_cart_buttons:
            time.sleep(5)  
            button.click()

    def verify_products_in_cart(self):
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "View Basket").click()

        cart_products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//tbody//tr//td[@class='product-name']"))
        )

        cart_product_names = [product.text for product in cart_products]
        for product_name in self.product_names:
            assert product_name in cart_product_names, f"Product '{product_name}' not added to the cart"

        print("All products added successfully.")
    def deleteproducts(self):
        cart_products = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//tbody//tr//td[@class='product-name']"))
        )

        cart_product_names = [product.text for product in cart_products]
        
        for product_name in cart_product_names:
            self.driver.find_element(By.XPATH,"//a[@class='remove']").click()
            time.sleep(3)
        assert self.driver.find_element(By.XPATH,"//p[@class='cart-empty']").is_displayed(), "Products are not deleted successfully"
        print("Products Deleted successfully")
    
    def registrationandlogin(self):
        self.driver.find_element(By.XPATH, "//a[text()='My Account']").click()
        time.sleep(3)
        # Registration
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.clear()
        email_input.send_keys("vyshuvyshnavi2000@gmail.com")
        password_input = self.driver.find_element(By.XPATH, "//input[@id='reg_password']")
        password_input.clear()
        password_input.send_keys("Vyshnavi@20")
        self.driver.find_element(By.XPATH, "//input[@name='register']").click()
    
        try:
            registration_message = self.driver.find_element(By.XPATH, "//li[text()=' An account is already registered with your email address. Please login.']")
            assert registration_message.is_displayed(), "User registration successfully done, Kindly login from next time"
        except NoSuchElementException:
            print("User registration successfully done, Kindly proceed for logi")
            pass  # If registration message not found, proceed to login
        
        # Login
        email_login_input = self.driver.find_element(By.XPATH, "//input[@id='username']")
        email_login_input.clear()
        email_login_input.send_keys("vyshuvyshnavi2000@gmail.com")
        password_login_input = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password_login_input.clear()
        password_login_input.send_keys("Vyshnavi@20")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@name='login']").click()
        time.sleep(5)
    

    def address(self):
        self.driver.find_element(By.XPATH,"//a[text()='Addresses']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[text()='Edit']").click()
        fn=self.driver.find_element(By.XPATH,"//input[@id='billing_first_name']")
        fn.clear()
        fn.send_keys("Vyshnavi")
        ln=self.driver.find_element(By.XPATH,"//input[@id='billing_last_name']")
        ln.clear()
        ln.send_keys("Mulinti")
        ph=self.driver.find_element(By.XPATH,"//input[@id='billing_phone']")
        ph.clear()
        ph.send_keys("0000000000")
        place=self.driver.find_element(By.XPATH,"//input[@id='billing_address_1']")
        place.clear()
        place.send_keys("Andhra")
        add=self.driver.find_element(By.XPATH,"//input[@id='billing_city']")
        add.clear()
        add.send_keys("Tadipatri")
        pin=self.driver.find_element(By.XPATH,"//input[@id='billing_postcode']")
        pin.clear()
        pin.send_keys("515411")
        self.driver.find_element(By.XPATH,"//input[@class='button']").click()
        self.driver.find_element(By.XPATH,"//a[text()='Addresses']").click()
        assert self.driver.find_element(By.XPATH,"//div[@class='u-column1 col-1 woocommerce-Address']//address").is_displayed(), "Address not saved successfully"
        print("Address Saved successfully")
        time.sleep(10)


    def close_browser(self):
        self.driver.quit()


if __name__ == "__main__":
    cart_automation = CartAutomation("https://practice.automationtesting.in/")
    cart_automation.collect_product_names()
    cart_automation.add_products_to_cart()
    cart_automation.verify_products_in_cart()
    cart_automation.deleteproducts()
    cart_automation.registrationandlogin()
    cart_automation.address()
    cart_automation.close_browser()
