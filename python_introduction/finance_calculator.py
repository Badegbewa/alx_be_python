monthly_income = input("Enter your monthly income: 5000 ")
monthly_expenses = input("Enter your total monthly expenses: 4000 ")
monthly_income = float(5000)
monthly_expenses = float(4000)
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"your monthly savings are ${monthly_savings}.")
print(f"projected savings after one year, with interest, is: ${projected_savings}")