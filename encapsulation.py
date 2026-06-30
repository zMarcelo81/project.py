class CityEmployee:
    used_ids = set()

    def __init__(self, employee_id, name, salary):
        self.set_employee_id(employee_id)
        self.set_name(name)
        self.set_salary(salary)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        employee_id = employee_id.strip().upper()
        if len(employee_id) < 3:
            raise ValueError("Employee ID is too short.")
        if employee_id in CityEmployee.used_ids:
            raise ValueError("Duplicate employee ID.")
        self.__employee_id = employee_id
        CityEmployee.used_ids.add(employee_id)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name.strip()) < 2:
            raise ValueError("Invalid name.")
        self.__name = name.strip().title()

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary must be positive.")
        self.__salary = salary

    def calculate_bonus(self):
        return self.__salary * 0.05


class ITStaff(CityEmployee):
    def calculate_bonus(self):
        return self.get_salary() * 0.10