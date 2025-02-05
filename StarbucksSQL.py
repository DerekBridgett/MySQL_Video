import pandas as pd
import random
from faker import Faker

fake = Faker()

# Set the number of records
NUM_CUSTOMERS = 1000
NUM_STORES = 50
NUM_ORDERS = 5000
NUM_PRODUCTS = 20
NUM_EMPLOYEES = 200
NUM_LOYALTY = 800
NUM_SUPPLIERS = 30

# Generate Customers
customers = [[fake.uuid4(), fake.name(), fake.email(), fake.phone_number(), random.randint(18, 75)]
             for _ in range(NUM_CUSTOMERS)]
df_customers = pd.DataFrame(customers, columns=["customer_id", "name", "email", "phone", "age"])

# Generate Stores
stores = [[i, fake.city(), fake.state(), fake.zipcode()] for i in range(1, NUM_STORES + 1)]
df_stores = pd.DataFrame(stores, columns=["store_id", "city", "state", "zipcode"])

# Generate Products
products = [[i, random.choice(["Latte", "Espresso", "Frappuccino", "Mocha", "Americano"]),
             round(random.uniform(3, 7), 2)] for i in range(1, NUM_PRODUCTS + 1)]
df_products = pd.DataFrame(products, columns=["product_id", "product_name", "price"])

# Generate Orders
orders = [[fake.uuid4(), random.choice(df_customers["customer_id"]),
           random.randint(1, NUM_STORES), random.randint(1, NUM_PRODUCTS),
           fake.date_between(start_date="-2y", end_date="today"), round(random.uniform(3, 20), 2)]
          for _ in range(NUM_ORDERS)]
df_orders = pd.DataFrame(orders, columns=["order_id", "customer_id", "store_id", "product_id", "order_date", "amount"])

# Generate Employees
employees = [[fake.uuid4(), fake.name(), random.randint(1, NUM_STORES),
              random.choice(["Barista", "Manager", "Cashier"]), round(random.uniform(30000, 60000), 2)]
             for _ in range(NUM_EMPLOYEES)]
df_employees = pd.DataFrame(employees, columns=["employee_id", "name", "store_id", "position", "salary"])

# Generate Loyalty Program
loyalty = [[random.choice(df_customers["customer_id"]), random.randint(100, 5000)]
           for _ in range(NUM_LOYALTY)]
df_loyalty = pd.DataFrame(loyalty, columns=["customer_id", "points"])

# Generate Suppliers
suppliers = [[i, fake.company(), fake.city()] for i in range(1, NUM_SUPPLIERS + 1)]
df_suppliers = pd.DataFrame(suppliers, columns=["supplier_id", "supplier_name", "location"])

# Save to CSV
df_customers.to_csv("customers.csv", index=False)
df_stores.to_csv("stores.csv", index=False)
df_products.to_csv("products.csv", index=False)
df_orders.to_csv("orders.csv", index=False)
df_employees.to_csv("employees.csv", index=False)
df_loyalty.to_csv("loyalty.csv", index=False)
df_suppliers.to_csv("suppliers.csv", index=False)

print("Mock data saved as CSV files.")
