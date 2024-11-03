file_path = 'C:/Users/thoma/Downloads/Data.csv'
class Customer:
    def __init__(self, customer_id, customer_age, customer_income, home_ownership, employment_duration, loan_intent, loan_grade, loan_amnt, loan_int_rate, term_years, historical_default, cred_hist_length, Current_loan_status):
        self.customer_id = customer_id
        self.customer_age = customer_age
        self.customer_income = customer_income
        self.home_ownership = home_ownership
        self.employment_duration = employment_duration
        self.loan_intent = loan_intent
        self.loan_grade = loan_grade
        self.loan_amnt = loan_amnt
        self.loan_int_rate = loan_int_rate
        self.term_years = term_years
        self.historical_default = historical_default
        self.cred_hist_length = cred_hist_length
        self.current_loan_status = Current_loan_status

    def __repr__(self):
        return (f"Customer({self.customer_id}, {self.customer_age}, {self.customer_income}, {self.home_ownership}, "
                f"{self.employment_duration}, {self.loan_intent}, {self.loan_grade}, {self.loan_amnt}, "
                f"{self.loan_int_rate}, {self.term_years}, {self.historical_default}, {self.cred_hist_length}, "
                f"{self.current_loan_status})")

def read_customers_from_csv(file_path):
    customers = []
    with open('C:/Users/thoma/Downloads/Data.csv', 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:  # Skip header line
            values = line.strip().split(',')
            customer_data = dict(zip(headers, values))
            customers.append(Customer(
                customer_id=customer_data['customer_id'],
                customer_age=int(customer_data['customer_age']),
                customer_income=(customer_data['customer_income']),
                home_ownership=customer_data['home_ownership'],
                employment_duration=customer_data['employment_duration'],
                loan_intent=customer_data['loan_intent'],
                loan_grade=customer_data['loan_grade'],
                loan_amnt=(customer_data['loan_amnt']),
                loan_int_rate=(customer_data['loan_int_rate']),
                term_years=int(customer_data['term_years']),
                historical_default=bool(customer_data['historical_default']),
                cred_hist_length=int(customer_data['cred_hist_length']),
                Current_loan_status=customer_data['Current_loan_status']
            ))
    return customers

# Example usage
file_path = 'C:/Users/thoma/Downloads/Data.csv'
customers = read_customers_from_csv('C:/Users/thoma/Downloads/Data.csv')
for customer in customers:
    print(customer)