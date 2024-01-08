class Student:
    """ Класс для задания вводных данных студентов """

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def set_lecturer_grade(self, lecturer, course, grade):
        """Функция выставления оценки лекторам"""

        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average_grade(self):
        """Функция расчета средней оценки за домашние задания по всем курсам, которые проходит студент"""

        if len(self.grades) == 0:
            return 0
        elif len(self.grades) == 1:
            average_grade: float = 0
            for course_grades in self.grades.values():
                average_grade += sum(course_grades)/len(course_grades)
            return average_grade
        else:
            grades_summary: float = 0
            grades_amount: int = 0
            for course_grades in self.grades.values():
                grades_summary += sum(course_grades)
                grades_amount += len(course_grades)
            return grades_summary/grades_amount

    def __str__(self):
        """Вывод информации о студенте"""

        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.calc_average_grade()}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}\n'

    def __lt__(self, other):
        return self.calc_average_grade() < other.calc_average_grade()

    def __gt__(self, other):
        return self.calc_average_grade() > other.calc_average_grade()

    def __eq__(self, other):
        return self.calc_average_grade() == other.calc_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average_grade(self):
        """Функция расчета средней оценки за лекции по всем курсам, которые ведет лектор"""

        if len(self.grades) == 0:
            return 0
        elif len(self.grades) == 1:
            average_grade: float = 0
            for course_grades in self.grades.values():
                average_grade += sum(course_grades)/len(course_grades)
            return average_grade
        else:
            grades_summary: float = 0
            grades_amount: int = 0
            for course_grades in self.grades.values():
                grades_summary += sum(course_grades)
                grades_amount += len(course_grades)
            return grades_summary/grades_amount

    def __str__(self):
        """Вывод информации о лекторе"""

        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.calc_average_grade()} \n'

    def __lt__(self, other):
        return self.calc_average_grade() < other.calc_average_grade()

    def __gt__(self, other):
        return self.calc_average_grade() > other.calc_average_grade()

    def __eq__(self, other):
        return self.calc_average_grade() == other.calc_average_grade()


class Reviewer(Mentor):
    def set_grade(self, student, course, grade):
        """Функция расчета средней оценки за домашние задания студентам выбранного курса"""

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Вывод информации о проверяющем"""

        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n'


def calc_average_student_grade(students, course):
    """Функция расчета средней оценки за домашние задания по студентам выбранного курса"""

    summary_grade: float = 0
    course_students: int = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            summary_grade += sum(student.grades[course])
            course_students += 1
    return summary_grade/course_students


def calc_average_lecturer_grade(lecturers, course):
    """Функция расчета средней оценки за лекции по лекторам выбранного курса"""

    summary_grade: float = 0
    course_lecturers: int = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            summary_grade += sum(lecturer.grades[course])
            course_lecturers += 1

    return summary_grade/course_lecturers


# студент 1
student_1 = Student('Mari', 'Awer', 'woman')
student_1.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'C++']

# студент 2
student_2 = Student('Antonio', 'Stia', 'man')
student_2.finished_courses += ['C#']
student_2.courses_in_progress += ['Python', 'Git']

# лектор 1
lecturer_1 = Lecturer('Will', 'Sead')
lecturer_1.courses_attached += ['Python', 'C++']

# лектор 2
lecturer_2 = Lecturer('Mike', 'Neal')
lecturer_2.courses_attached += ['Python', 'Git']

# проверяющий 1
reviewer1 = Reviewer('Sam', 'Bucky')
reviewer1.courses_attached += ['Python', 'C++']

# оценки проверяющего 1 для обоих студентов
reviewer1.set_grade(student_1, 'Python', 10)
reviewer1.set_grade(student_1, 'C++', 6)
reviewer1.set_grade(student_2, 'Python', 8)

# проверяющий 2
reviewer2 = Reviewer('Sally', 'Dun')
reviewer2.courses_attached += ['Python', 'Git']

# оценки проверяющего 2 для обоих студентов
reviewer2.set_grade(student_1, 'Python', 5)
reviewer2.set_grade(student_2, 'Python', 9)
reviewer2.set_grade(student_2, 'Git', 5)

# оценки студента 1 для лекторов
student_1.set_lecturer_grade(lecturer_1, 'Python', 10)
student_1.set_lecturer_grade(lecturer_1, 'C++', 9)
student_1.set_lecturer_grade(lecturer_2, 'Python', 8)

# оценки студента 2 для лекторов
student_2.set_lecturer_grade(lecturer_1, 'Python', 8)
student_2.set_lecturer_grade(lecturer_2, 'Python', 10)
student_2.set_lecturer_grade(lecturer_2, 'Git', 8)

# вывод информации о студентах
print(student_1)
print(student_2)

# вывод информации о лекторах
print(lecturer_1)
print(lecturer_2)

# вывод информации о проверяющих
print(reviewer1)
print(reviewer2)

# сравнение студентов по средней оценке за домашнее задание
print('Средняя оценка у студента 1 выше, чем у студента 2? Ответ: ', student_1 > student_2)
print('Средняя оценка у студента 1 ниже, чем у студента 2? Ответ: ', student_1 < student_2)
print('Средняя оценка у студента 1 равна средней оценке у студента 2? Ответ: ', student_1 == student_2)

# сравнение лекторов по средней оценке за лекции
print('Средняя оценка у лектора 1 выше, чем у лектора 2? Ответ: ', lecturer_1 > lecturer_2)
print('Средняя оценка у лектора 1 ниже, чем у лектора 2? Ответ: ', lecturer_1 < lecturer_2)
print('Средняя оценка у лектора 1 равна средней оценке у лектора 2? Ответ: ', lecturer_1 == lecturer_2)

# подсчет студентов
all_students = [student_1, student_2]

# расчет средней оценки для студентов курса Python
average_python_students_grade = calc_average_student_grade(all_students, 'Python')
print('Средняя оценка для студентов курса Python', average_python_students_grade)

# расчет средней оценки для студентов курса Git
average_git_students_grade = calc_average_student_grade(all_students, 'Git')
print('Средняя оценка для студентов курса Git', average_git_students_grade)

# подсчет лекторов
all_lecturers = [lecturer_1, lecturer_2]

# расчет средней оценки для лекторов курса Python
average_python_lecturers_grade = calc_average_lecturer_grade(all_lecturers, 'Python')
print('Средняя оценка для лекторов курса Python', average_python_lecturers_grade)

# расчет средней оценки для лекторов курса Git
average_git_lecturers_grade = calc_average_lecturer_grade(all_lecturers, 'Git')
print('Средняя оценка для лекторов курса Git', average_git_lecturers_grade)
