# Import the necessary classes
from customer import Customer
from coffee import Coffee
from order import Order

# Function to run interactive debugging
def main():
    # Step 1: Create Customers
    print("Creating customers...")
    korir = Customer("Korir")
    busolo = Customer("Busolo")
    munene = Customer("Munene")
    print(f"Customers: {korir.name}, {busolo.name}, {munene.name}")

    # Step 2: Create Coffees
    print("\nCreating coffees...")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
    print(f"Coffees: {latte.name}, {espresso.name}, {cappuccino.name}")

    # Step 3: Create Orders
    print("\nCreating orders...")
    order1 = korir.create_order(latte, 4.5)
    order2 = busolo.create_order(espresso, 6.0)
    order3 = korir.create_order(cappuccino, 5.5)
    order4 = munene.create_order(latte, 3.5)
    order5 = busolo.create_order(latte, 4.0)

    print(f"Order 1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")
    print(f"Order 2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")
    print(f"Order 3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")
    print(f"Order 4: {order4.customer.name} ordered {order4.coffee.name} for ${order4.price}")
    print(f"Order 5: {order5.customer.name} ordered {order5.coffee.name} for ${order5.price}")

    # Step 4: Check Customer Orders
    print("\nChecking Korir's orders...")
    korir_orders = korir.orders()
    for order in korir_orders:
        print(f"Korir ordered {order.coffee.name} for ${order.price}")

    # Step 5: Check Coffee Orders
    print("\nChecking who ordered a Latte...")
    latte_orders = latte.orders()
    for order in latte_orders:
        print(f"{order.customer.name} ordered a Latte for ${order.price}")

    # Step 6: Get unique list of coffees ordered by Bob
    print("\nChecking unique coffees ordered by Busolo...")
    busolo_coffees = busolo.coffees()
    for coffee in busolo_coffees:
        print(f"Busolo ordered {coffee.name}")

    # Step 7: Get number of times Espresso was ordered
    print("\nChecking number of times Espresso was ordered...")
    espresso_count = espresso.num_orders()
    print(f"Espresso was ordered {espresso_count} times")

    # Step 8: Calculate average price of Latte orders
    print("\nCalculating average price of Latte orders...")
    avg_price_latte = latte.average_price()
    print(f"The average price of a Latte is ${avg_price_latte:.2f}")

    # Step 9: Finding the customer who spent the most on Latte
    print("\nFinding the most aficionado for Latte...")
    top_customer_for_latte = Customer.most_aficionado(latte)
    if top_customer_for_latte:
        print(f"{top_customer_for_latte.name} spent the most on Latte.")
    else:
        print("No orders for Latte yet.")

if __name__ == "__main__":
    main()
