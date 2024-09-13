class Coffee:
    all_coffees = []

    def __init__(self, name):
        self._validate_name(name)
        self._name = name
        self._orders = []
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    def _validate_name(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string of at least 3 characters.")

    def orders(self):
        return self._orders

    def customers(self):
        return list(set([order.customer for order in self._orders]))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
