class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
# Метод для получения информации о студенте
    def get_info(self):
        return (f'{self.name} {self.surname} - {self.gender}\nУчится - {self.courses_in_progress}\n\
Закончил - {self.finished_courses}\nИмеет оценки - {self.grades}\n')

#Метод выставления оценки лектору
    def add_grade_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lectures_grade:
                lecturer.lectures_grade[course] += [grade]
            else:
                lecturer.lectures_grade[course] = [grade]
        else:
            return 'Ошибка'  

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        return (f'{self.name} {self.surname} преподаёт {self.courses_attached}')

class Lecturer(Mentor):
    def __init__ (self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lectures_grade = {}

    def get_grade(self):
        return (f'{self.surname} получил следующие оценки от студентов: {self.lectures_grade}')
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def add_grade_student(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка' 

    #Создали экземпляры студентов

djons = Student('Roy', 'Djons', 'male')
djons.courses_in_progress += ['Python']
ignatov = Student('billy', 'ignatov', 'male')
ignatov.courses_in_progress += ['Python']
    #Добавили лектора 
mkrtchan = Lecturer('Pavel', 'mkrtchan')
mkrtchan.courses_attached += ['Python']
    #Добавили Reviewer 
cidorov = Reviewer('Cidr', 'Cidorov')

### Студент ставит оценку лектору
djons.add_grade_lector(mkrtchan, 'Python', 9)
ignatov.add_grade_lector(mkrtchan, 'Python', 10)
print(mkrtchan.get_grade()) 

### Reviewer ставит оценку студенту
cidorov.add_grade_student(djons, 'Python', 5)
cidorov.add_grade_student(ignatov, 'Python', 2)

print(djons.get_info())
print(ignatov.get_info())


# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)
