
# name = input("Enter name to serve food ")
students = ["Juliet","Mildred","Emelda","Judith","Mervyl","Gard","Salma"]
for student in students:
    if student not in students:
        print("You can serve")
    else:
        print("You have already served")
