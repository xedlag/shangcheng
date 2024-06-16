# tests.py
# 用于测试 Django 应用的文件。

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem, Order, OrderItem

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            stock=100
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.stock, 100)

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.user.username, 'testuser')

class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            stock=100
        )
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_item_creation(self):
        cart_item = CartItem.objects.get(cart=self.cart, product=self.product)
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.product.name, "Test Product")

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.order = Order.objects.create(user=self.user, total_price=20.00)

    def test_order_creation(self):
        order = Order.objects.get(user=self.user)
        self.assertEqual(order.total_price, 20.00)

class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.order = Order.objects.create(user=self.user, total_price=20.00)
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            stock=100
        )
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=2, price=10.00)

    def test_order_item_creation(self):
        order_item = OrderItem.objects.get(order=self.order, product=self.product)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.price, 10.00)
        self.assertEqual(order_item.product.name, "Test Product")
