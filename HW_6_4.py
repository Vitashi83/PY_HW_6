class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses = []
        self.grades = {}

    def rate_st_for_lect(self, lecturer, course, grade):
        if isinstance (lecturer, Lecturer) and (course in lecturer.courses) or (course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

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
        self.courses_in_progress = []
        self.courses = []
        self.grades = {}
    
    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}'
        return a
      
class Lecturer(Mentor):
    def _init_(self, name, surname):
        super()._init_(self, name, surname)
        #self.courses_in_progress = []
        #self.courses = []
        #self.grades = {}

    def ever_rat(self):
        s=0
        k=0
        for i in self.grades.values():
            for j in i:
                s+=j
                k+=1
        return (s/k)
    
    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ever_rat()}'
        return a

class Reviewer(Mentor):
    def _init_(self, name, surname):
        super()._init_(self, name, surname)
                
    def rate_rv(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Студент не занимается на данном курсе'

def compare_lect():
    if lecturer_1.ever_rat() > lecturer_2.ever_rat():
        print(f'У {lecturer_1.name} {lecturer_1.surname} больше всех лекторов средняя оценка за лекции: {lecturer_1.ever_rat()}')
    else:
        print(f'У {lecturer_2.name} {lecturer_2.surname} меньше всех лекторов средняя оценка за лекции: {lecturer_2.ever_rat()}')

def compare_home():
    if student_1.ever_rat() < student_2.ever_rat():
        print(f'У {student_1.name} {student_1.surname} больше всех средняя оценка за домашние задания: {student_1.ever_rat()}')
    else:
        print(f'У {student_2.name} {student_2.surname} меньше всех средняя оценка за домашние задания: {student_2.ever_rat()}')

student_1 = Student('Ruoy', 'Eman', 'man')
student_1.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git']

reviewer_1 = Reviewer('lebron', 'James')
reviewer_1.courses += ['Python']
reviewer_1.courses += ['Git']
 
reviewer_1.rate_rv(student_1,'Python',8)
reviewer_1.rate_rv(student_1,'Python',10)
reviewer_1.rate_rv(student_1,'Git',10)
reviewer_1.rate_rv(student_1,'Git',7)

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_in_progress += ['Python', 'Git']

student_1.rate_st_for_lect(lecturer_1, 'Python', 10)
student_1.rate_st_for_lect(lecturer_1, 'Python', 10)
student_1.rate_st_for_lect(lecturer_1, 'Git', 9)
student_1.rate_st_for_lect(lecturer_1, 'Git', 8)

student_2 = Student('Pety', 'Pupik', 'man')
student_2.finished_courses += ['Введение в программирование']
student_2.courses_in_progress += ['Python', 'Git']

reviewer_2 = Reviewer('Ylia', 'Jva')
reviewer_2.courses += ['Python']
reviewer_2.courses += ['Git']
 
reviewer_2.rate_rv(student_2,'Python',9)
reviewer_2.rate_rv(student_2,'Python',10)
reviewer_2.rate_rv(student_2,'Git',10)
reviewer_2.rate_rv(student_2,'Git',10)

lecturer_2 = Lecturer('Sony', 'Bud')
lecturer_2.courses_in_progress += ['Python', 'Git']

student_2.rate_st_for_lect(lecturer_2, 'Python', 8)
student_2.rate_st_for_lect(lecturer_2, 'Python', 8)
student_2.rate_st_for_lect(lecturer_2, 'Git', 9)
student_2.rate_st_for_lect(lecturer_2, 'Git', 8)

print(reviewer_1, f'\n')
print(lecturer_1, f'\n')
print(student_1, f'\n')

print(reviewer_2, f'\n')
print(lecturer_2, f'\n')
print(student_2)

def sr_dz(self, student, course, grade):
    n = 0
    for n in student:
        n = n + 1
        if isinstance(student, Student) and course in self.courses and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
                return 'Студент не занимается на данном курсе'
        s=0
        k=0
        for i in self.grades.values():
            for j in i:
                s+=j
                k+=1
        return (s/k)




print(sr_dz)        
