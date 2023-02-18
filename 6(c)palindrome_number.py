num = int(input("Enter the number: "))

calc = int(str(num)[::-1])

if num == calc:
	print(f"{str(num)} is a palindrome number")
else:
	print(f"{str(num)} is not a palindrome number")