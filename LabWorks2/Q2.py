'''
WAP which accepts marks of four subjects and display total marks, percentage and grade.
    Hint: more that 70% -> distinction, more than 60% -> first, more that 40% -> pass, less than 40% -> fail
'''

sub_english = int(input("Enter the marks obtained in English:"))
sub_nepali = int(input("Enter the marks obtained in Nepali:"))
sub_math = int(input("Enter the marks obtained in Math:"))
sub_science = int(input("Enter the marks obtained in Science:"))

total_marks = sub_math + sub_nepali + sub_english + sub_science

per = ((total_marks / 400) * 100)

print(f"Total marks: {total_marks}")
print(f"Percentage: {per} %")

if per > 70 :
    print("Distinction")
    print("Grade: A")
elif per > 60 and per <= 70:
    print("First")
    print("Grade:B")
elif per > 40 and per <=60:
    print("Pass")
    print("Grade:C")
elif per < 40:
    print("Fail")