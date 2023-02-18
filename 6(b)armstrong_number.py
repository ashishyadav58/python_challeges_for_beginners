import math

num = int(input("Enter the number: "))

length = len(str(num))

new = 0

for i in range(length):
	calc = int(math.pow(int(str(num)[i]), length))
	new = calc + new

if int(num) == new:
	print(f"{num} is a armstrong number")
else:
	print(f"{num} is not a armstrong number")