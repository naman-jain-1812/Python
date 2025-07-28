student_marks = {'Naman':95,'Samarth':85,'Priyank':75}
student_name = input("Enter the student's name:")
if (student_name in student_marks):
    mark = student_marks[student_name]
    print("{}'s marks : {}".format (student_name,mark))
else:
    print("Student not found")