from coffee import Coffee
from order import Order
class Customer:
    all_customers = []

    def __init__(self, name):
        self._validate_name(name)
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    def _validate_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee instance.")
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee instance.")
        
        customer_spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price

        if not customer_spending:
            return None

        return max(customer_spending, key=customer_spending.get)
