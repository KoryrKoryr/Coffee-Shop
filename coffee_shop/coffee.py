# Define the Coffee class
class Coffee:
    # Class-level attribute to store all coffees
    all_coffees = []

    # Constructor method
    def __init__(self, name):
        # Validate the name
        self._validate_name(name)
        # Assign name to the coffee
        self._name = name
        # Initialize the orders list
        self._orders = []
        # Add the coffee to the all_coffees list
        Coffee.all_coffees.append(self)

    # Getter method for the name attribute
    @property
    def name(self):
        return self._name

    # Setter method for the name attribute
    @name.setter
    def name(self, value):
        # Validate the new name
        self._validate_name(value)
        # Update the name attribute if it is valid
        self._name = value

    # Private method to validate the name
    def _validate_name(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string of at least 3 characters.")

    # Method to return all orders associated with the coffee
    def orders(self):
        return self._orders

    # Method to return all unique customers associated with the coffee
    def customers(self):
        return list(set([order.customer for order in self._orders]))

    # Method to return the number of orders associated with the coffee
    def num_orders(self):
        return len(self._orders)

    # Method to return the average price of orders associated with the coffee
    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)