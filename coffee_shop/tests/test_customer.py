import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Invalid name (too long)

    with pytest.raises(ValueError):
        Customer("")  # Invalid name (too short)

    valid_customer = Customer("John")
    assert valid_customer.name == "John"

def test_customer_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

    # Check that the order is in the customer's order list
    assert order in customer.orders()

def test_customer_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    customer.create_order(coffee1, 4.5)
    customer.create_order(coffee2, 6.0)

    coffees = customer.coffees()

    assert coffee1 in coffees
    assert coffee2 in coffees
    assert len(coffees) == 2  # Ensure the unique list of coffees is returned

def test_most_aficionado():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Espresso")

    customer1.create_order(coffee, 5.0)  # Alice spends 5.0
    customer2.create_order(coffee, 6.0)  # Bob spends 6.0
    customer1.create_order(coffee, 3.0)  # Alice spends 3.0 more (total 8.0)

    assert Customer.most_aficionado(coffee) == customer1  # Alice spent the most
