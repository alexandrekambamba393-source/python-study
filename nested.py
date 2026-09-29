2. # Write a program that:
# => Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

# Takes the user's credit score and annual income as input
credit_score = (input("Enter your credit score: "))
annual_income = (input("Enter your annual income: "))

credit_score=float(credit_score)
annual_income=float(annual_income)

# Check credit score and income conditions
if credit_score > 700:
    if annual_income > 50000:
        print("Loan approved.")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")