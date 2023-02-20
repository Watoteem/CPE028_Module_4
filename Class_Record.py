import Student
import Grades


p1 = Student.Student("Joshua Advincula", 22)
p4 = Grades.Grades("CPE028", 3, 50)
print(p1)
print("Name: ", p1.name)
print("Age: ",p1.age)
print("Course Code: ", p4.course_code)
print("Course Unit: ", p4.course_units)
print("Course Grade: ", p4.course_grade)