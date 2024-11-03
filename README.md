# Assignment6
A.) Create a customer class, complete with initialization function. Use the data in your file to create customer objects for each sample in your data.

Loan dataset columns: customer_id: Unique identifier for each customer customer_age: Age of the customer customer_income: Annual income of the customer home_ownership: Home ownership status (e.g., RENT, OWN, MORTGAGE) employment_duration: Duration of employment in months loan_intent: Purpose of the loan (e.g., PERSONAL, EDUCATION, MEDICAL, VENTURE) loan_grade: Grade assigned to the loan loan_amnt: Loan amount requested loan_int_rate: Interest rate of the loan term_years: Loan term in years historical_default: Indicates if the customer has a history of default (Y/N) cred_hist_length: Length of the customer's credit history in years Current_loan_status: Current status of the loan (DEFAULT, NO DEFAULT)

What does the code do?
1.) Defines a customer class with the column attriubutes, id, age, income,... 
2.) Reads the csv file and creates Customer objects for each row (not including header)
 3.) read_customers_from_csv processes the CSV data into a list defined as Customer. 
4.) Reads the customer data from the file. 
5.) prints each customer object to the console.


Any object oriented programming?
Yes, Where it defines Customer Class and, takes the customer data within it and then creates and uses objects based on this class. 
1.) You define a customer class with attributes and methods. 
2.) Then creates objects (instances) of the Customer class

Why is it important?
Reusability: once a class is created, it can be reused in different parts of a program. Promoting reuse of code. 
Maintainability: Makes code easier to maintain and modify: changing one part of the program can be made with minimal impact on everything else. 
Scaleability: helps where new features of components can be added without disrupting the functionality of the code.



