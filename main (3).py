''' implement a function  called sort_students that takes
a list of student object as input and sorts the list based on their cgpa(cumulative  group point average ) in descending order. Each student object  has the following  attributes :name(string),roll_number(string),and cpga (float).test the function  with different  input lists  of students.
class student:

def __init__(self,name,roll_number,cpga)
self.name=name
self.roll_number=roll_number
self.cpga=cpga
def.sort_student(student_list):
#sort the list of student  in descending  order of cgpa
sorted (student_list,key=lambda student:student  cgpa reserve =true )
#syntax_lambda arg:exp
return.sorted _students
# example usage:
students=[student ("Hari"),"A123",7.2,student ("saumya","A124",8.9,student ("mahidhar","A125"9.5,student "srikanth","A126", 9.9)]
sorted_student =sort_students (students)
#print the sorted list of sstudent for student in sorted_students:
print(" Name:{},roll_number:{},cgpa:{}",format (student.name,student.roll_number,student.cgpa))
