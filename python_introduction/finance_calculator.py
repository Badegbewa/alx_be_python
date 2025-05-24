monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
# Keep asking for monthly income until a valid number is entered
while True:
    try:
        monthly_income = float(input("Enter your monthly income: "))
        break
    except ValueError:
        print("Please enter a valid number for income.")

# Keep asking for monthly expenses until a valid number is entered
while True:
    try:
        monthly_expenses = float(input("Enter your total monthly expenses: "))
        break
    except ValueError:
        print("Please enter a valid number for expenses.")

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
5000