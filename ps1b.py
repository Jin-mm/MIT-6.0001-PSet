annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))

portion_down_payment = 0.25
downpayment = total_cost * portion_down_payment
monthly_base = annual_salary / 12
current_savings = 0
r = 0.04
i = 0

while current_savings < downpayment:
	if i == 0:
		current_savings += monthly_base * portion_saved
		i += 1
	elif i % 6 != 0:
		current_savings += current_savings * r / 12
		current_savings += monthly_base * portion_saved
		i += 1
	else:
		current_savings += current_savings * r / 12
		monthly_base = monthly_base * (1 + semi_annual_raise)
		current_savings += monthly_base * portion_saved
		i += 1


print("Number of months: ", i, current_savings)
