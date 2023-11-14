import unittest
import time
from functions.swag_labs import Swag_labs


class TestSwag_labs(unittest.TestCase):
    def setUp(self):
        self.swag_lab = Swag_labs()
        self.swag_lab.login('standard_user', 'secret_sauce')

    def test_c1_add_to_card(self):
        self.swag_lab.add_to_card()

    def test_c2_shopping_cart_page(self):
        self.swag_lab.add_to_card()
        self.swag_lab.shopping_cart_page()

    def test_c3_remove_product(self):
        self.swag_lab.add_to_card()
        self.swag_lab.shopping_cart_page()
        self.swag_lab.remove_product()

    def test_c4_checkout(self):
        self.swag_lab.add_to_card()
        self.swag_lab.shopping_cart_page()
        self.swag_lab.checkout()

    def test_c5_shipment_information(self):
        self.swag_lab.add_to_card()
        self.swag_lab.shopping_cart_page()
        self.swag_lab.checkout()
        self.swag_lab.shipment_information('Laura', 'Andrade', '410001')

    def test_c6_finalize_purchase(self):
        self.swag_lab.add_to_card()
        self.swag_lab.shopping_cart_page()
        self.swag_lab.checkout()
        self.swag_lab.shipment_information('Laura', 'Andrade', '410001')
        self.swag_lab.finalize_purchase()

    def test_c7_back_to_products(self):
        self.swag_lab.add_to_card()
        self.swag_lab.shopping_cart_page()
        self.swag_lab.checkout()
        self.swag_lab.shipment_information('Laura', 'Andrade', '410001')
        self.swag_lab.finalize_purchase()
        self.swag_lab.back_to_products()

    def test_c8_product_detail(self):
        self.swag_lab.product_detail()

    def test_c9_reset_app_state(self):
        self.swag_lab.product_detail()
        self.swag_lab.reset_app_state()

    def test_c10_about(self):
        self.swag_lab.about()

    def test_c11_logout(self):
        self.swag_lab.logout()

    def tearDown(self):
        time.sleep(2)
        print('¡Se ha completado el Test Aumatico!')
        self.swag_lab.close()