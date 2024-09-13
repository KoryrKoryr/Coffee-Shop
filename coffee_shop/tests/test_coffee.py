import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A")  # Invalid coffee name (too short)

    valid_coffee = Coffee("Latte")
    assert valid_coffee.name == "Latte"

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer1 = Customer("Denis")
    customer2 = Customer("Kiki")

    order1 = customer1.create_order(coffee, 5.0)
    order2 = customer2.create_order(coffee, 6.0)

    orders = coffee.orders()
    assert order1 in orders
    assert order2 in orders
    assert len(orders) == 2

def test_coffee_customers():
    coffee = Coffee("Latte")
    customer1 = Customer("Denis")
    customer2 = Customer("Kiki")

    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)

    customers = coffee.customers()
    assert customer1 in customers
    assert customer2 in customers
    assert len(customers) == 2

def test_num_orders():
    coffee = Coffee("Espresso")
    customer1 = Customer("Denis")
    customer2 = Customer("Kiki")

    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)

    assert coffee.num_orders() == 2  # Two orders placed

def test_average_price():
    coffee = Coffee("Espresso")
    customer1 = Customer("Denis")
    customer2 = Customer("Kiki")

    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 7.0)

    assert coffee.average_price() == 6.0  # Average of 5.0 and 7.0 is 6.0

    # Test for case where no orders exist
    empty_coffee = Coffee("Latte")
    assert empty_coffee.average_price() == 0  # No orders, average should be 0
