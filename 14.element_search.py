List = []

num = int(input("How many entries you want? "))

for i in range(1, num+1):
	user = input(f"Enter the values {i}: ")
	if user.isalpha() == True:
		List.append(user)
	elif user.isalpha() == False:
		List.append(int(user))

print(" ")
print(f'Your list is ready: {List}')

print(" ")
search = input("Search for element: ")

for j in range(num):
	if search == List[j]:
		print(f'Given element ({search}) is found at index {j}')