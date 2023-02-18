num = []

for i in range(1, 6+1):
	num.append(int(input(f"Enter the number {i}: ")))
num.sort()

print(" ")
print(f'before Swaping: {num}')
	
	
def swap(value1, value2):
	num[value1], num[value2] = num[value2], num[value1]
	
for j in range(0, len(num), 2):
	swap(j, j+1)

#swap(2, 3)
#swap(4, 5)

print(f'After Swaping: {num}')