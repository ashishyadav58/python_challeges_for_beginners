import string

tech = '''Technology is the application of knowledge for achieving practical goals in a reproducible way. The word technology can also mean the products resulting from such efforts, including both tangible tools such as utensils or machines, and intangible ones such as software'''


#Creating function to vowels & consonants character
def count_vol_cons(upper, lower):
	totalvowel = 0
	totalcons = 0
	
	vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] #List of vowels
	
	for i in vowels:
		totalvowel = totalvowel + tech.count(i)
	print(f"No.of Vowels are: {totalvowel}")
	
	consonants = upper+lower #List of consonants
	for letter in vowels:
		consonants.remove(letter)
	
	for j in consonants:
		totalcons = totalcons + tech.count(j)
	print(f"No.of Consonants are: {totalcons}")
		
count_vol_cons(list(string.ascii_uppercase), list(string.ascii_lowercase))



#Creating function to count upper & lower case character
def count_upper_lower(upper, lower):
	totaluppercase = 0
	totallowercase = 0
	
	for u in upper:
		totaluppercase = totaluppercase + tech.count(u)
	print(f"No.of Uppercase characters are: {totaluppercase}")
	
	for l in lower:
		totallowercase = totallowercase + tech.count(l)
	print(f"No.of Lowercase characters are: {totallowercase}")
		
	
count_upper_lower(list(string.ascii_uppercase), list(string.ascii_lowercase))