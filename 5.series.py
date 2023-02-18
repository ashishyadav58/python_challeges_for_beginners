options = input('''
********** SERIES *********

1.Odd Numbers
2.Even Numbers
3.Prime Numbers
4.Whole Numbers

Select by typing 1, 2, 3, 4: ''')

num = int(input('''
Enter the range: '''))

if options == "1":
	for i in range(1, num+1, 2):
		print(i)
elif options == "2":
	for j in range(0, num+1, 2):
		print(j)
elif options == "3":
	for n in range(1, num+1):
		for k in range(2, n):
			if n % i == 0:
				break
			else:
				print(n)
				break
elif options == "4":
	for m in range(0, num+1):
		print(m)