class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.age} tuổi - Điểm: {self.grade}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


if __name__ == "__main__":
    student = Student("SV001", "Nguyen Van A", 20, 8.5)
    print(student)
    print(student.to_dict())