# Student_Test_GPA
# SDEV220
# Gage Lipman
#Program takes user input for, first name, last name, and gpa and compares it against a set value to determine whether they have
#made deans list or honor roll. 

student_Lname = ''

while student_Lname.lower() != 'zzz':
    student_Fname = input('Please enter the student\'s first name: ')
    student_Lname = input('Please enter the student\'s last name (or "zzz" to quit): ')

    if student_Lname.lower() == 'zzz':
        break

    student_name = student_Fname + " " + student_Lname

    while True:
        Student_GPA_input = input(f'Please provide {student_name}\'s GPA: ')
        try:
            Student_GPA = float(Student_GPA_input)
            break
        except ValueError:
            print('Please provide a numeric value with a decimal point.')

    if Student_GPA >= 3.5:
        print(f'{student_name} has made the Dean\'s List!')
    elif Student_GPA >= 3.25:
        print(f'{student_name} has made the Honor Roll!')
    else:
        print(f'{student_name} did not qualify for honors.')

print("Thank you for checking GPAs.")
