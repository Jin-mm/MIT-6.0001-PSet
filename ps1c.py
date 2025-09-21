annual_salary = float(input('Enter your annual salary: '))
semi_annual_raise = .07
r = 0.04
total_cost = 1000000
downpayment = total_cost * 0.25



def savings(savingrate, annualsalary):
	monthly_base = annualsalary / 12
	current_savings = 0
	for i in range(1,37):
		if i % 6 != 0:
			current_savings += current_savings * r / 12
			current_savings += monthly_base * (savingrate / 10000)
		else:
			current_savings += current_savings * r / 12
			monthly_base = monthly_base * (1 + semi_annual_raise)
			current_savings += monthly_base * (savingrate / 10000)
	return current_savings


def best_saving_rate(annualsalary):
	low = int(0)
	high = int(10000)
	guess = (low + high) // 2
	num = 0
	#first check the edge case
	if savings(10000, annual_salary) < downpayment:
		print("It is not possible to pay the down payment in 3 years.")
		return
	
	while low <= high:
		num += 1 # So the only case where low > high and the loop ends without success is when no solution exists.
		savings_now = savings(guess, annual_salary)
		if abs(savings_now - downpayment) <= 100:
			return(guess, num)
		elif savings_now < downpayment:
			low = guess + 1
			guess = (low + high) // 2
		else:
			high = guess - 1
			guess = (low + high) // 2

t = best_saving_rate(annual_salary)
if t is not None:
	print("best saving rate:", t[0], "\n" + "bisection search:", t[1])

	
		
