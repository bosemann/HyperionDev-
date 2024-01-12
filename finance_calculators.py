# This is a program that allows the user to access two different
# financial calculators
# An investment calculator and a home loan repayment calculator



'''pseudocode solution
1. user should choose want calculation they want to do
         investment
         bond
2. capitalization should not affect the entries
3. if user selects investments, user should input
        amount of money depositing
        the interest rate
        the number of years
        simple or compound
4. Calculate the amount they get back back after given period and 
    interest rate.
5. Print out the answer
6. if user selects bond, user should input 
        present value of house
        interest rate
        number of months to repay
7. calculate the money user will have to repay each month
8. output the answer'''

import math

# The code is printing a menu for the user to choose between two options:
# "investment" or "bond". It provides a brief description of each option.
print("----------------------------------------------------------------------")
print('''investment - to calculate the amount of interest you'll earn on
your investment
bond        - to calculate the amount you'll have to pay on a 
home loan''')
print()

# The code snippet is implementing a while loop that prompts the user to enter
# either "investment" or "bond" from a menu. It then takes the user's input and
# converts it to lowercase.
while True:
    user_input = input('''Enter either "investment" or "bond" from the menu
    above to proceed: ''')
    selection = user_input.lower()

    if selection == "investment":
        deposit = int(input("Enter How much you want to deposit? "))
        interest_rate = int(input("Enter the interest rate "))
        time = int(input("Enter the number of years to invest "))
        interest_type = input("Enter either 'simple' or 'compound'")
        interest_selection = interest_type.lower()
        rate = interest_rate / 100
        if interest_selection == "simple":
            simple_amount = deposit * (1 + rate * time)
# printing amount earned with simple interest
            result = float(simple_amount)
            result = float(round(result, 2))
            print(f' {result} is the total amount with interest')
            break
        elif interest_selection == "compound":
            compound_amount = deposit * math.pow((1 + rate ), time)
# printing amount earned with compound interest
            result = float(compound_amount)
            result = float(round(result, 2))
            print(f' {result} is the total amount with interest')
            break
# if selection is bond then house value, annual rate, number months are input     
    elif selection == "bond":
        house_value = int(input("Enter the present value of your house? "))
        annual_rate = int(input("Enter the interest rate "))
        num_months = int(input("Enter number of months to repay bond? "))
        monthly_int_rate = (annual_rate / 100) / 12
        repayment = (monthly_int_rate * house_value) / (1 -
        (1 + monthly_int_rate)**(-num_months))
# bond repayment is printed
        result = float(repayment)
        result = float(round(result, 2))
        print(f'you will have to pay {result} each month')
        break
    else:
        print("Input error please try again")
