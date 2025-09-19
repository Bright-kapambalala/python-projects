#grade evaluator

name = str(input("enter your name: "))
score = int(input("enter your score: "))
if score <60:
     print("student:",name,"\nscore:",score ,"\nGrade:F")
elif score >= 60 and score  <= 69:
     print("student:",name,"\nscore:",score ,"\nGrade:D")

elif score >= 70 and score  <= 79:
     print("student:",name,"\nscore:",score ,"\nGrade:C")

elif score >= 80 and score  <= 89:
     print("student:",name,"\nscore:",score ,"\nGrade:B")

elif score >= 90 and score  <= 100:
     print("student:",name,"\nscore:",score ,"\nGrade:A")

#if score is above 100 or below 0
else:
    print("INVALID")
