class Customer:
    def __init__(self, customer_id, customer_age,customer_income, home_ownership, employment_duration, loan_intent, loan_grade, loan_amnt, loan_int_rate, term_years, historical_default, cred_hist_length, Current_loan_status):
        self.customer_id = customer_id
        self.age = customer_age
        self.income = customer_income
        self.ownership = home_ownership
        self.employment = employment_duration
        self.intent = loan_intent
        self.grade = loan_grade
        self.amount = loan_amnt
        self.int_rate = loan_int_rate
        self.term = term_years
        self.default = historical_default
        self.cred_hist = cred_hist_length
        self.status = Current_loan_status

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.age}, {self.ownership}, {self.employment}, {self.intent}, {self.grade}, {self.amount}, {self.int_rate}, {self.term}, {self.default}, {self.cred_hist}, {self.status})"

def read_customers_from_csv(file_path):
    customers = []
    with open('C:/Users/thoma/Downloads/Data.csv', 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            customer_data = line.strip().split(',')
            customer = Customer(
                customer_id=str(customer_data[0]),
                customer_age=(customer_data[1]),
                customer_income=(customer_data[2]),
                home_ownership=str(customer_data[3]),
                employment_duration=str(customer_data[4]),
                loan_intent=str(customer_data[5]),
                loan_grade=str(customer_data[6]),
                loan_amnt=(customer_data[7]),
                loan_int_rate=(customer_data[8]),
                term_years=(customer_data[9]),
                historical_default=customer_data[10].strip().lower() == 'true',
                cred_hist_length=(customer_data[11]),
                Current_loan_status=str(customer_data[12])



            )
            customers.append(customer)
    return customers

# Example usage
file_path = 'C:/Users/thoma/Downloads/Data.csv'
customers = read_customers_from_csv('C:/Users/thoma/Downloads/Data.csv')
for customer in customers:
    print(customer)