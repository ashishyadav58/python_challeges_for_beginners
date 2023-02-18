import sympy

factors = []

num = int(input("Enter the number: "))

if sympy.isprime(num) == True:
	print(f"{num} is a prime number")
else:
	for i in range(1, num + 1):
		if num % i == 0:
			factors.append(i)

if len(factors) > 2:
	print(f"{num} is a Composite number")