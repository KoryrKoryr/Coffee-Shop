# Coffee Shop

- **Coffee Shop** is a **domain model** of a coffee shop using object oriented programming.

## Features

- Manage orders for multiple customers
- Calculate total number of orders and average price for a particular customer
- Identify the customer who has spent the most money on a specific coffee

## Directory Structure

```plaintext
coffee_shop/
├── tests/                # Directory for unit tests
│   ├── test_customer.py  # Tests for Customer class
│   ├── test_coffee.py    # Tests for Coffee class
│   └── test_order.py     # Tests for Order class
│
├── coffee.py             # Contains the Coffee class
├── customer.py           # Contains the Customer class
├── debug.py              # Interactive script to test the model
├── order.py              # Contains the Order class
└── README.md             # Project overview and instructions
```

## Setup

1. Clone the Repository
   - git clone https://github.com/KoryrKoryr/Coffee-Shop
   - cd Coffee-Shop
   - cd coffee_shop
2. Set up a virtual environment within this directory using `pipenv`

   - pipenv install
   - pipenv shell

3. Install Dependancies
   - pipenv install pytest
4. Run Tests

   - Run tests using the command `pytest`

5. Debug the code
   - Run `python debug.py` on the terminal to interactively test the functionality of the model.

## How to use

- On a new python file `new_entry.py` created in the directory, begin by importing the classes.

```plaintext
  from customer import Customer
  from coffee import Coffee
  from order import Order
```

- Create customers:

```plaintext
  cher = Customer("Cher")
  kinya = Customer("Kinya")
```

- Create coffee types:

```plaintext
  latte = Coffee("Latte")
  espresso = Coffee("Espresso")
```

- Cher places an order for a latte

```plaintext
  order1 = cher.create_order(latte, 7.8)
```

- Kinya orders an espresso

```plaintext
  order2 = kinya.create_order(espresso, 3.4)
```

- Check how many times latte has been ordered

```plaintext
  print(f"Latte was ordered {latte.num_orders()} times.")
```

- Calculate the average price for lattes

```plaintext
  print(f"Average price of Latte: ${latte.average_price():.2f}")
```

- Find the customer who spent the most on lattes

```plaintext
  top_customer = Customer.most_aficionado(latte)
  if top_customer:
    print(f"{top_customer.name} spent the most on Latte.")
```

- Run the code on the terminal

```plaintext
  python new_entry.py
```

## Output

- This will be the output :

```plaintext
   Latte was ordered 1 times.
   Average price of Latte: $7.80
   Cher spent the most on Latte.

```
