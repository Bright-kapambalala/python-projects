# student_marks.py
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [85, 92, 78, 88, 95]

def assign_grade(mark):
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

# calculate average manually
total = 0
for s in scores:
    total += s
average = total / len(scores) # len returns number of items in a list

print ("       Student Results      ")
for i in range(len(names)):
    grade = assign_grade(scores[i])
    # I used f-string for better formatting
    print(names[i] + ": " + str(scores[i]) + " -> Grade " + grade)

print ("Average marks:", round(average, 1))
