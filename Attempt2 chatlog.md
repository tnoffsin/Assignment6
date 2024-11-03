tnoffsin: without using outside libraries Create a customer class, complete with an initialization function. Use the data in the reference file to create customer objects for each sample in your data

GitHub Copilot: To create a `Customer` class and initialize it with data from a CSV file without using outside libraries, you can follow these steps:

1. Define the `Customer` class with an `__init__` method.
2. Read the CSV file line by line.
3. Create `Customer` objects for each line in the CSV file.

Here's an example implementation:

```python
class Customer:
    def __init__(self, customer_id, name, email, age):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.name}, {self.email}, {self.age})"

def read_customers_from_csv(file_path):
    customers = []
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            customer_data = line.strip().split(',')
            customer = Customer(
                customer_id=customer_data[0],
                name=customer_data[1],
                email=customer_data[2],
                age=int(customer_data[3])
            )
            customers.append(customer)
    return customers

# Example usage
file_path = 'DATA.CSV'
customers = read_customers_from_csv(file_path)
for customer in customers:
    print(customer)
```

This code assumes that your CSV file has the following structure:

```
customer_id,name,email,age
1,John Doe,john.doe@example.com,30
2,Jane Smith,jane.smith@example.com,25
...
```

Make sure to replace the `file_path` variable with the actual path to your `DATA.CSV` file. This script will read the CSV file, create `Customer` objects for each row, and print them out.