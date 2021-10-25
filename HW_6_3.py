class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_st_for_lect(self, lecturer, course, grade):
        if isinstance (lecturer, Lecturer)and(course in lecturer.courses)and ((course in self.finished_courses)or(course in self.courses_in_progress)):
            if course in lecturer.grades:
               lecturer.grades[course]+=[grade]
            else:
                lecturer.grades[course]=[grade]

    def ever_rat(self):
        s=0
        k=0
        for i in self.grades.values():
            for j in i:
                s+=j
                k+=1
        return (s/k)
    
    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.ever_rat()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return a
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses = []
    
    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}'
        return a
        
class Lecturer(Mentor):
    def _init_(self, name, surmane):
        super()._init_(self, name, surname)
        self.courses = []
        self.grades = {}

class Reviewer(Mentor):
    def _init_(self, name, surmane):
        super()._init_(self, name)
                
    def rate_rv(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Студент не занимается на данном курсе'

student_1 = Student('kobe', 'braynt', 'man')
student_1.finished_courses += ['git']
student_1.courses_in_progress += ['Python']

reviewer_1=Reviewer('lebron', 'James')
reviewer_1.courses += ['Python']
reviewer_1.courses += ['git']
 
reviewer_1.rate_rv(student_1,'Python',8)
reviewer_1.rate_rv(student_1,'Python',8)
reviewer_1.rate_rv(student_1,'Python',10)
reviewer_1.rate_rv(student_1,'Python',10)

print(student_1)
print(reviewer_1)