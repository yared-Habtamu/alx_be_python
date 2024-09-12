monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_saving = monthly_income - monthly_expenses
interest = 0.05
projected_savings = monthly_saving * 12 + (monthly_saving * 12 * interest)
print(f"Your monthly savings are ${int(monthly_saving)}")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")