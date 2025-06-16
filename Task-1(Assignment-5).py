# dictionary of student marks

dictionary = {'Alice':85,'Bob':90,'Mary':72,'Christiana':54,'Nick':62}
name = input("Enter the students's name: ").capitalize()
if name in dictionary:
    print(name + "'s marks:", dictionary[name])
else:
    print("Student not found.")