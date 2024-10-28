class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

#Метод выставления оценки лектору
    def add_grade_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lectures_grade:
                lecturer.lectures_grade[course] += [grade]
            else:
                lecturer.lectures_grade[course] = [grade]
        else:
            return 'Ошибка'  

#Метод для вычисления средней оценки студента
    def get_average_grade(self):
        av_grade = []
        for course in self.courses_in_progress:
            av_grade += self.grades[course]
        return sum(av_grade) / len(av_grade)
    
    def __ge__(self, student):
        return self.get_average_grade() >= student.get_average_grade()
    def __eq__(self, student):
        return self.get_average_grade() == student.get_average_grade()
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_grade()}\n\
Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer(Mentor):
    def __init__ (self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.lectures_grade = {}

    def get_average_grade(self):
        av_grade = []
        for course in self.courses_attached:
            av_grade += self.lectures_grade[course]
        return sum(av_grade) / len(av_grade)
    
    def __ge__(self, lecturer):
        return self.get_average_grade() >= lecturer.get_average_grade()
    def __eq__(self, lecturer):
        return self.get_average_grade() == lecturer.get_average_grade()
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}"
    
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
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

#Добавили студентов
djons = Student('Roy', 'Djons', 'male')
djons.courses_in_progress += ['Python']
ignatov = Student('billy', 'ignatov', 'male')
ignatov.courses_in_progress += ['Python', 'Git']
ignatov.finished_courses += ['Введение в программирование']

#Добавили лектора 
mkrtchan = Lecturer('Pavel', 'mkrtchan')
mkrtchan.courses_attached += ['Python', 'Git']
ruslanov = Lecturer('Ruslan', 'Ruslanov')
ruslanov.courses_attached += ['Python']

#Добавили Reviewer 
cidorov = Reviewer('Cidr', 'Cidorov')
petrov = Reviewer('Petr', 'Petrrov')

### Студент ставит оценку лектору
djons.add_grade_lector(mkrtchan, 'Python', 9)
ignatov.add_grade_lector(mkrtchan, 'Python', 10)
ignatov.add_grade_lector(mkrtchan, 'Git', 2)
djons.add_grade_lector(ruslanov, 'Python', 3)
ignatov.add_grade_lector(ruslanov, 'Python', 7)

### Reviewer ставит оценку студенту
cidorov.add_grade_student(djons, 'Python', 5)
cidorov.add_grade_student(ignatov, 'Python', 2)
petrov.add_grade_student(ignatov, 'Git', 9)
petrov.add_grade_student(ignatov, 'Python', 4)


###Демонстрация работы кода
#Вывели информацию о студентах и преподователях
print('Список лекторов')
print(mkrtchan)
print(ruslanov)
print()
print('Список Студентов')
print(ignatov)
print(djons)

print('\nСравнение лекторов')
#Сравнили лекторов
if (mkrtchan == ruslanov):
    print(f'{mkrtchan.name} {mkrtchan.surname} и {ruslanov.name} {ruslanov.surname} имеют одинаковый средний балл')
else:
    if (mkrtchan >= ruslanov):
        print(f'{mkrtchan.name} {mkrtchan.surname} имеет средний бал выше, чем {ruslanov.name} {ruslanov.surname}')
    else:
        print(f'{ruslanov.name} {ruslanov.surname} имеет средний бал выше, чем {mkrtchan.name} {mkrtchan.surname}')

print('\nСравнение студентов')
#Сравнили студентов
if (djons == ignatov):
    print(f'{djons.name} {djons.surname} и {ignatov.name} {ignatov.surname} имеют одинаковый средний балл')
else:    
    if (djons >= ignatov):
        print(f'{djons.name} {djons.surname} имеет средний бал выше, чем {ignatov.name} {ignatov.surname}')
    else:
        print(f'{ignatov.name} {ignatov.surname} имеет средний бал выше, чем {djons.name} {djons.surname}')