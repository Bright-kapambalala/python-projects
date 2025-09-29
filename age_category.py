# age_category.py
name = str(input("enter your name: "))
age = int(input("enter your age: "))

if age > 0 and age <= 12:
  category = "child"
elif age > 12 and age <= 19:
  category = "teen"
elif age > 19 and age <= 59:
  category = "adult"
elif age > 59:
  category = "senior"
elif age < 0 :
  category = "invalid"
  
print ("Name: ",name ,"\nAge: ",age , "\nCategory: ",category)
