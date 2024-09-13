# Define the Order class
class Order:
    # Class-level attribute to store all orders
    all_orders = []

    # Constructor method
    def __init__(self, customer, coffee, price):
        # Validate the price
        self._validate_price(price)
        # Assign customer, coffee, and price to the order
        self._customer = customer
        self._coffee = coffee
        self._price = price
        # Add the order to the all_orders list and the customer and coffee's order lists
        Order.all_orders.append(self)
        customer._orders.append(self)
        coffee._orders.append(self)

    # Getter method for the customer attribute
    @property
    def customer(self):
        return self._customer

    # Getter method for the coffee attribute
    @property
    def coffee(self):
        return self._coffee

    # Getter method for the price attribute
    @property
    def price(self):
        return self._price

    # Setter method for the price attribute
    @price.setter
    def price(self, value):
        # Validate the new price
        self._validate_price(value)
        # Update the price attribute if it is valid
        self._price = value

    # Private method to validate the price
    def _validate_price(self, price):
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float or integer between 1.0 and 10.0.")