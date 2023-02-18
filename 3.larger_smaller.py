num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

def larger():
	if num1 > num2 and num1 > num3:
		print(f"Larger number: {num1}")
	elif num2 > num1 and num2 > num3:
		print(f"Larger number: {num2}")
	elif num3 > num1 and num3 > num2:
		print(f"Larger number: {num3}")

larger()


def smaller():
	if num1 < num2 and num1 < num3:
		print(f"Smaller number: {num1}")
	elif num2 < num1 and num2 < num3:
		print(f"Smaller number: {num2}")
	elif num3 < num1 and num3 < num2:
		print(f"Smaller number: {num3}")

smaller()