
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def rate_lesson(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        sum = 0
        len = 0
        for key in lecturer.grades.keys():
            for grad in list(lecturer.grades[key]):
                sum = sum + grad
                len += 1
        lecturer.average_rating = round(sum / len, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.average_rating}\n" \
              f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
              f"Завершенные курсы: {self.finished_courses}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0
        self.students_list = []

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f"Имя: {self.name} \n" \
              f"Фамилия: {self.surname} \n" \
              f"Средняя оценка за лекции: {self.average_rating}"
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        sum = 0
        len = 0
        for key in student.grades.keys():
            for grad in list(student.grades[key]):
                sum = sum + grad
                len += 1
        student.average_rating = round(sum / len, 2)

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}"
        return res


first_student = Student("Сергей", "Акиньшин", "i")
first_student.finished_courses += ["Введение в программирование"]
first_student.courses_in_progress += ["Python"]
first_student.courses_in_progress += ["GIT"]

second_student = Student("Филипп", "Беликов", "i")
second_student.courses_in_progress += ["Python"]
second_student.courses_in_progress += ["GIT"]
second_student.finished_courses += ["Введение в программирование"]

first_lecturer = Lecturer("Darren", "Porter")
first_lecturer.courses_attached += ["Python"]
first_lecturer.courses_attached += ["GIT"]

second_lecturer = Lecturer("Sean", "Tyas")
second_lecturer.courses_attached += ["GIT"]

first_reviewer = Reviewer("Евгений", "Власов")
first_reviewer.courses_attached += ["Python"]

second_reviewer = Reviewer("Роман", "Мессер")
second_reviewer.courses_attached += ["GIT"]
second_reviewer.courses_attached += ["Python"]


student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]


def average_rating_hw(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


def average_rating_lesson(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


first_student.rate_lesson(second_lecturer, "GIT", 6)
first_student.rate_lesson(second_lecturer, "GIT", 5)
first_student.rate_lesson(first_lecturer, "GIT", 10)
first_student.rate_lesson(first_lecturer, "GIT", 9)
first_student.rate_lesson(first_lecturer, "Python", 9)
second_student.rate_lesson(first_lecturer, "Python", 8)
second_student.rate_lesson(first_lecturer, "Python", 10)

second_reviewer.rate_hw(first_student, "Python", 8)
second_reviewer.rate_hw(first_student, "GIT", 9)
second_reviewer.rate_hw(first_student, "GIT", 10)
first_reviewer.rate_hw(first_student, "Python", 10)
first_reviewer.rate_hw(second_student, "Python", 8)
first_reviewer.rate_hw(second_student, "Python", 8)
first_reviewer.rate_hw(second_student, "Python", 9)

print("Список студентов:")
print(f"{first_student}\n")
print(f"{second_student}\n")
print("Список лекторов:")
print(f"{first_lecturer}\n")
print(f"{second_lecturer}\n")
print("Список проверяющих:")
print(f"{first_reviewer}\n")
print(f"{second_reviewer}\n")


print(f"Средняя оценка за дз у Акиньшина больше, чем у Беликова {second_student < first_student}")
print(f"Средняя оценка за лекции у Porter меньше, чем у Tyas {second_lecturer < first_lecturer}\n")


print(f'Средняя оценка студентов за курс GIT: {average_rating_hw(student_list, "GIT")}')
print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {average_rating_lesson(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {average_rating_lesson(lecturer_list, "GIT")}')