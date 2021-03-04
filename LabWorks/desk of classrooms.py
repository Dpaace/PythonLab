'''
A school decided to replace the desks in three classrooms.
Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks
that can be purchased.
The program should read three integers: the number of students in each of the three  classes a, b and c respectively.
In the first test there are three groups.
The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks.
11 desks are also enough fot the third group of 22 students.
So we need 32 desks in total.
'''

class1 = int(input("Enter the number of students in first class :"))
class2 = int(input("Enter the number of students in second class :"))
class3 = int(input("Enter the number of students in third class :"))
desk1 = class1 // 2
desk2 = class2 // 2
desk3 = class3 // 2
remain1 = class1 % 2
remain2 = class2 % 2
remain3 = class3 % 2
class1_desk = desk1 + remain1
class2_desk = desk2 + remain2
class3_desk = desk3 + remain3
total = desk1 + desk2 + desk3 + remain1 + remain2 + remain3
print(f"Class 1 needs {class1_desk} desks")
print(f"Class 2 needs {class2_desk} desks")
print(f"Class 3 needs {class3_desk} desks")
print("Total number of desks needed ", total)


'''
print(desk1, desk2, desk3)
print(remain1, remain2, remain3)
'''