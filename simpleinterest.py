def calculate_simple_interest(principal, time, senior_citizen=False):
    if senior_citizen:
        rate_of_interest = 0.15
    else:
        rate_of_interest = 0.12 if principal > 100000 else 0.10

    simple_interest = principal * rate_of_interest * time
    return simple_interest
principal_amount = float(input("Enter the principal amount: "))
time_period = float(input("Enter the time period (in years): "))
customer_type = input("Are you a senior citizen? (yes/no): ").lower() == "yes"
interest_amount = calculate_simple_interest(principal_amount, time_period, customer_type)
print(f"The simple interest is: {interest_amount}")
