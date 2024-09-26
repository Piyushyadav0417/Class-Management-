class OnlineCourse:
    def __init__(self, course,instructor ):
        self.course = course
        self.instructor = instructor
        self.students = []
    
    def enroll_student(self, student):
        self.students.append(student)
        print(f"Congrats! {student.name} You are succesfully Enrolled in {self.course}")
        
    def course_details(self):
        print(f"{self.course} ")
        print(f"Instructor Name: {self.instructor}")
        # print(f"Enrolled Students: {', '.join(self.students)}")
        print(f"Enrolled Students: ")
        for student in self.students:
            print(student.name)
        
    def compled_course(self, name):
        for student in self.students:
            if student.name in self.students:
                self.students.remove(student)
                print(f"{name} has completed the course!")
        print(f"{name} is not enrolled in this course")
    
    def avg_grade(self, grades):
        total = sum(student.grades)
        average = total/len(student.grades)
        print(f"The average grade is: {round(average)}")

#Second Class
class Student:
    def __init__(self, name, grades):
        self.name = name 
        self.grades = grades

    
    
#Arguments For OnlineCourse Student
course_input = input("Enter a course: ").lower()
name = input("Enter a Instructor: ").lower()
student = input("Enter your name: ").lower()


course = OnlineCourse(course_input, name)
#Arguments For Class Student
num_student = int(input("Enter number of students: "))    
for _ in range(num_student):
    student_name = input("Enter student name: ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Enter a grade: "))
        grades.append(grade)
    student = Student(student_name, grades)
    course.enroll_student(student)
    course.avg_grade(student)
course.course_details()