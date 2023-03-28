from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Store, Section, Product


class TestCreateProduct(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_store = Store.objects.create(
            name='testName123',
            contacts='TestContacts',
            address='TestAddress'
        )

        test_user = User.objects.create_user(
            username='Testusername1',
            password='NewPassword123'
        )

        test_section = Section.objects.create(
            name='TestSection'
        )

        test_product = Product.objects.create(
            title='TestProduct',
            type='Test',
            price=99.99,
            quantity=1,
            description='Test Description',
            location=test_store,
            section=test_section,
            status='Stored'
        )

    def test_repr_methods(self):
        product = Product.objects.get(id=1)
        section = Section.objects.get(id=1)
        store = Store.objects.get(id=1)
        self.assertEqual(str(product), 'TestProduct')
        self.assertEqual(str(section), 'TestSection')
        self.assertEqual(str(store), 'testName123 TestAddress')

    def test_product_content(self):
        product = Product.objects.get(id=1)
        title = f"{product.title}"
        product_type = f"{product.type}"
        price = f"{product.price}"
        quantity = f"{product.quantity}"
        description = f"{product.description}"

        self.assertEqual(title, 'TestProduct')
        self.assertEqual(product_type, 'Test')
        self.assertEqual(price, '99.99')
        self.assertEqual(quantity, '1')
        self.assertEqual(description, 'Test Description')

    def test_product_status(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.status, 'Stored')
        self.assertFalse(product.status == 'Ordered')
        self.assertFalse(product.status == 'Transit')
        self.assertFalse(product.status == 'Returned')
        self.assertFalse(product.status == 'Damaged')
        self.assertFalse(product.status == 'Sold')



