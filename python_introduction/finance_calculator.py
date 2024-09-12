monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
interest = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest)
print(f"Your monthly savings are ${int(monthly_savings)}")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")