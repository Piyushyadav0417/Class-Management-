class OnlineCourse:
    def __init__(self, course,instructor ):
        self.course = course
        self.instructor = instructor
        self.students = []
    
    def enroll_student(self, student):
        self.students.append(student)
        print(f"Congrats! {student} You are succesfully Enrolled in {self.course}")
    
                        
    def course_details(self):
        print(f"{self.course} ")
        print(f"Instructor Name: {self.instructor}")
        print(f"Enrolled Students: ")
        for student in self.students:
            print(student)

        
    def compled_course(self, name):
        for student in self.students:
            if student.name in self.students:
                self.students.remove(student)
                print(f"{name} has completed the course!")
        print(f"{name} is not enrolled in this course")
    
    def avg_grade(self, grade):
        total = sum(grade)
        average = total/len(grade)
        print(f"The average grade is: {average}")


    
    
#Arguments For OnlineCourse Student
course_input = input("Enter a course: ").lower()
Instructor_name = input("Enter a Instructor: ").lower()
student_name = input("Enter student name: ").lower()
grade = list(map(int, input("Enter Your each subject marks with spaces: ").split()))


C = OnlineCourse(course_input, Instructor_name)
C.avg_grade(grade)


# This will show How For Details and Enroll
num_student = int(input("How many Students want to Enroll: "))    
for _ in range(num_student):
    enroll_name = input("Enter student name who want to enroll: ").lower()
    C.enroll_student(enroll_name)
C.course_details()


# This will show How For compled_course
competion_student = input("Enter student course competion student name: ").lower()
C.compled_course(competion_student)