import unittest
from cart_automation import CartAutomation

class TestCartAutomation(unittest.TestCase):

    def setUp(self):
        self.cart_automation = CartAutomation("https://practice.automationtesting.in/")
        
    def tearDown(self):
        self.cart_automation.close_browser()

    def test_collect_product_names(self):
        self.cart_automation.collect_product_names()
        product_names = self.cart_automation.product_names
        self.assertTrue(len(product_names) > 0, "No product names collected")

    def test_add_products_to_cart(self):
        self.cart_automation.collect_product_names() 
        self.cart_automation.add_products_to_cart()
    

    def test_verify_products_in_cart(self):
        self.cart_automation.collect_product_names() 
        self.cart_automation.add_products_to_cart() 
        self.cart_automation.verify_products_in_cart()


    def test_delete_products(self):
        self.cart_automation.collect_product_names()
        self.cart_automation.add_products_to_cart()
        self.cart_automation.verify_products_in_cart() 
        self.cart_automation.deleteproducts()
        


    def test_registration_and_login(self):
        self.cart_automation.collect_product_names()
        self.cart_automation.add_products_to_cart()
        self.cart_automation.verify_products_in_cart() 
        self.cart_automation.deleteproducts()
        self.cart_automation.registrationandlogin()
        
        
    def test_address(self):
        self.cart_automation.collect_product_names()
        self.cart_automation.add_products_to_cart()
        self.cart_automation.verify_products_in_cart() 
        self.cart_automation.deleteproducts()
        self.cart_automation.registrationandlogin()  
        self.cart_automation.address()


if __name__ == '__main__':
    unittest.main()
