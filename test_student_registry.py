import pytest
from student_registry import Student

def test_student_initialization():
    student = Student("Alice")
    assert student.get_name == "Alice"
    assert student.get_age == 13
    assert student.get_grade == "12th"

def test_student_name_setter():
    student = Student("Alice")
    student.set_name = "Alex"
    assert student.get_name == "Alex"

def test_student_age_setter():
    student = Student("Alice")
    student.set_age = 14
    assert student.get_age == 14

def test_student_grade_setter():
    student = Student("Alice")
    student.set_grade = "10th"
    assert student.get_grade == "10th"

def test_invalid_name_setter():
    student = Student("Alice")
    student.set_name = 123
    assert student.get_name == "Alice"

def test_invalid_age_setter():
    student = Student("Alice")
    student.set_age = "invalid"
    assert student.get_age == 13

def test_invalid_grade_setter():
    student = Student("Alice")
    student.set_grade = "13th"
    assert student.get_grade == "12th"

# Write tests for Class methods

def test_print_student(capsys): #note that when testing __str__ method you have to compare to stdout with capsys
    student = Student("Jimmy")
    print(student)
    captured = capsys.readouterr()
    expected_output = "Name: Jimmy\nAge: 13\nGrade: 12th\n"
    assert captured.out == expected_output

def test_subject():
    student = Student("Jimmy")
    assert student.study("Computer Science") == "Jimmy is studying Computer Science"

def test_advance():
    student = Student("Jimmy", 15, "10th")
    student.advance(1)
    assert student.get_grade == "11th"
