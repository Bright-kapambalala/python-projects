def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

students = []
marks = []

# Take input for 5 students
while len(students) < 5:
    name = input("Enter student name: ")
    students.append(name)
    
    mark = int(input(f"Enter marks for {name}: "))
    marks.append(mark)

for i in range(len(students)):
    grade = calculate_grade(marks[i])
    print ()
    print (f"{students[i]}: {marks[i]} – Grade {grade}")
