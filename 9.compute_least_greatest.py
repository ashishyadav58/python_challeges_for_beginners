import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = math.gcd(num1, num2)
lcm = math.lcm(num1, num2)

print(f''' 
Greatest common factor of {num1}, {num2} is: {gcd}
Least common factor of {num1}, {num2} is: {lcm}''')