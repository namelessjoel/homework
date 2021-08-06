class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.lecturer_grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name) 

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'  

    def get_average_grade(self):
        grade = []
        for grades in self.grades.values():
            for number in grades:
                grades.append(number)
        return round(sum(grade) / len(grade), 1)

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            return self.get_average_grade() < other_student.get_average_grade() 

    def __str__(self):
        res =(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')
        return res
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lecturer_grades}')
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
        if course in student.grades:
          student.grades[course] += [grade]
        else:
          student.grades[course] = [grade]
      else:
        return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res

def aw_rate_students(student_list, course_name):
  result = 0
  if course_name in Student.courses_in_progress or Student.finished_courses:
    for element in Student.grades.values():
      result += element
    return round(sum(result) / len(result), 1)
        

student_1 = Student('Emma', 'Stone', 'Female')
student_1.add_courses_in_progress('Python')
student_1.add_courses_in_progress('Git')
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jack', 'Nolan', 'Male')
student_2.add_courses_in_progress('Python')
student_2.add_courses_in_progress('Git')
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Nora', 'Trae')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Rita', 'Pale')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Git', 10)

print(student_1 > student_2)

print(student_1.grades)
print(lecturer_1.lecturer_grades)