class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self._validate_price(price)
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._validate_price(value)
        self._price = value

    def _validate_price(self, price):
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float or integer between 1.0 and 10.0.")
