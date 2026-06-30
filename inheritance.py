class Citizen:
    def __init__(self, citizen_id, name, age):
        self.citizen_id = citizen_id
        self.name = name
        self.age = age

    def calculate_city_benefits(self):
        return "Basic city services"


class StudentCitizen(Citizen):
    def calculate_city_benefits(self):
        return "Student discount and library access"