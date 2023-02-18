import string

L1 = []

entries = int(input("How many entries you want? "))

for i in range(1, entries+1):
	user = int(input(f"Enter the number {i}: "))
	L1.append(user)

print(" ")
print(f'Largest Number in a list: {max(L1)}')
print(f'Smallest Number in a list: {min(L1)}')