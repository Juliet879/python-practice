# class Zoom:
#     def __init__(self,max_number):
#         self.max_number = max_number

#     def add_student(self,names):
#         self.names = names

#     def check_space(self,admit):
#         self.admit = admit
#         space_available = self.max_number - self.admit
#         print(f"{space_available} spaces available in the meeting")


# course1 = Zoom(7)

# # names = input("Please enter the names of the students in the waiting room :  ".split(","))
# # print( course1.add_student(names))
# print(course1.add_student("Juliet"))
# print(course1.check_space(4))
students = []
def add_student(name):
    students.append(name)
    print(students)

(add_student("juliet")
