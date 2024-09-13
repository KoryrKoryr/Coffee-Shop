import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Latte")

    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Invalid price (below 1.0)

    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)  # Invalid price (above 10.0)

    valid_order = Order(customer, coffee, 5.0)
    assert valid_order.price == 5.0

def test_order_customer_and_coffee():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)

    assert order.customer == customer
    assert order.coffee == coffee

def test_order_price_update():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 6.0)

    order.price = 7.0
    assert order.price == 7.0

    with pytest.raises(ValueError):
        order.price = 12.0  # Invalid price, should raise an error
