student_details = {}

user = int(input("How many entries you want?: "))

for i in range(1, user+1):
    print(" ")
    rollno = int(input("Enter Student's Roll Number: "))
    name = input("Enter Student's Name: ")
    marks = int(input("Enter Student's Marks: "))

    student_details[rollno] = [name, marks]

print(" ")
print(f'''**** Student Details ****
{student_details}''')

for student in student_details:
	if student_details[student][1] == 75:
		print(("Student who scored 75 marks is/are:", student_details[student][0]))