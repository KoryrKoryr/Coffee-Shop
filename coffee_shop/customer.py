# Import the Coffee and Order classes
from coffee import Coffee
from order import Order

# Define the Customer class
class Customer:
    # Class-level attribute to store all customers
    all_customers = []

    # Constructor method
    def __init__(self, name):
        # Validate the name
        self._validate_name(name)
        # Assign name to the customer
        self._name = name
        # Initialize the orders list
        self._orders = []
        # Add the customer to the all_customers list
        Customer.all_customers.append(self)

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
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    # Method to return all orders associated with the customer
    def orders(self):
        return self._orders

    # Method to return all unique coffees associated with the customer
    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    # Method to create a new order for the customer
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee instance.")
        # Create a new Order instance and add it to the customer's orders list
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        return new_order

    # Class method to find the customer who spends the most on a specific coffee
    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee instance.")
        
        # Create a dictionary to store the total spending of each customer on the specified coffee
        customer_spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price

        # If no orders were found for the specified coffee, return None
        if not customer_spending:
            return None

        # Return the customer who spent the most on the specified coffee
        return max(customer_spending, key=customer_spending.get)