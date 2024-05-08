import unittest
from cart_automation import CartAutomation

class TestCartAutomation(unittest.TestCase):

    def setUp(self):
        self.cart_automation = CartAutomation("https://practice.automationtesting.in/")
        
    def tearDown(self):
        self.cart_automation.close_browser()

    # Positive Flows

    def test_collect_product_names_positive(self):
        self.cart_automation.collect_product_names()
        product_names = self.cart_automation.product_names
        self.assertTrue(len(product_names) > 0, "No product names collected")

    def test_add_products_to_cart_positive(self):
        self.cart_automation.collect_product_names() 
        self.cart_automation.add_products_to_cart()
    
    def test_verify_products_in_cart_positive(self):
        self.cart_automation.collect_product_names() 
        self.cart_automation.add_products_to_cart() 
        self.cart_automation.verify_products_in_cart()

    def test_delete_products_positive(self):
        self.cart_automation.collect_product_names()
        self.cart_automation.add_products_to_cart()
        self.cart_automation.verify_products_in_cart() 
        self.cart_automation.deleteproducts()

    def test_registration_and_login_positive(self):
        self.cart_automation.collect_product_names()
        self.cart_automation.add_products_to_cart()
        self.cart_automation.verify_products_in_cart() 
        self.cart_automation.deleteproducts()
        self.cart_automation.registrationandlogin()
        
    def test_address_positive(self):
        self.cart_automation.collect_product_names()
        self.cart_automation.add_products_to_cart()
        self.cart_automation.verify_products_in_cart() 
        self.cart_automation.deleteproducts()
        self.cart_automation.registrationandlogin()  
        self.cart_automation.address()

    # Negative Flows

    def test_registration_with_existing_email_negative(self):
        self.cart_automation.registrationandlogin()
        """Test registration with an existing email"""
        # Implement test case for registration with an existing email.


    def test_invalid_login_credentials_negative(self):
        self.cart_automation.registrationandlogin()
        """Test login with invalid credentials."""
        # Implement test case for login with invalid credentials.

    def test_invalid_address_details_negative(self):
        self.cart_automation.address()
        """Test adding invalid address details."""
        # Implement test case for adding invalid address details.

if __name__ == '__main__':
    unittest.main()
