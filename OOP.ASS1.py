class Student:
    def __init__(self, student_id, name, program):
        self.student_id = student_id
        self.name = name
        self.program = program
        self.score = None

    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Score: {self.score}")

    def update_record(self, score):
        if Student.is_valid_score(score):
            self.score = score
        else:
            print("Invalid score. Use 0 to 100.")

    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    @classmethod
    def from_string(cls, text):
        student_id, name, program = text.split(",")
        return cls(int(student_id), name, program)


class Exam:
    GRADE_BANDS = (("A", 80), ("B", 70), ("C", 60), ("D", 50))

    def __init__(self, code, title, pass_mark):
        self.code = code
        self.title = title
        self.pass_mark = pass_mark

    def display_info(self):
        print(f"Exam: {self.code} - {self.title} (pass mark: {self.pass_mark})")

    def check_result(self, student):
        if student.score is None:
            return "No score yet"
        if student.score >= self.pass_mark:
            return "Pass"
        return "Fail"

    def get_grade(self, student):
        if student.score is None:
            return "No score yet"
        for letter, minimum in Exam.GRADE_BANDS:
            if student.score >= minimum:
                return letter
        return "F"


students = {}


def add_student(student):
    students[student.student_id] = student


def display_students():
    for student_id, student in students.items():
        student.display_info()


s1 = Student(6144, "Mohammed", "Software Engineering")
s1.update_record(78)
s1.display_info()

exam1 = Exam("PROG211", "Object Oriented Programming 1", 50)
exam1.display_info()
print(exam1.check_result(s1))

s2 = Student(5656, "Aminata", "Software Engineering")
s2.update_record(45)

add_student(s1)
add_student(s2)
display_students()
print(exam1.check_result(s2))

s3 = Student.from_string("1107,Kadiatu,Software Engineering")
s3.update_record(150)
s3.update_record(67)
add_student(s3)
display_students()

print(exam1.get_grade(s1))
print(exam1.get_grade(s2))
print(exam1.get_grade(s3))