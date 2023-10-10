import re

class Student:
    def __init__(self, name, age=13, grade="12th") -> None:
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            new_name = re.sub(r'[^a-zA-Z]', "", new_name)
            self._name = new_name.title()
        else:
            print("Name must have at least three characters")
    
    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 11 <= new_age <= 18:
            self._age = new_age
        else:
            print("Age must be a number between 11 and 18")

    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        new_grade = re.sub(r'[th]', "", new_grade)
        if 9 <= int(new_grade) <= 12:
            self._grade = new_grade + "th"
        else:
            print("Grade must be formatted as between 9th and 12th grade")

    def __str__(self) -> str:
        return f"Name: {get_name()}\nAge: {get_age()}\nGrade: {get_grade()}"
    
    def advance(self, years_advanced):
        set_grade(years_advanced)

    def study(self, subject):
        return f"{self._name} is studying {subject}"
