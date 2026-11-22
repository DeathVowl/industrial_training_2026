class WORKER:
    """Класс сотрудника винодельческой организации."""

    def __init__(self, full_name="", position="", salary=0.0, hire_year=0):
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.hire_year = hire_year

    @classmethod
    def with_params(cls, full_name, position, salary, hire_year):
        return cls(full_name, position, salary, hire_year)

    def __del__(self):
        pass

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary

    def set_hire_year(self, hire_year):
        self.hire_year = hire_year

    def show(self):
        print(f"ФИО: {self.full_name} | Должность: {self.position} | "
              f"Зарплата: {self.salary} | Год поступления: {self.hire_year}")

    def __str__(self):
        return (f"{self.full_name} — {self.position}, "
                f"зарплата {self.salary}, принят в {self.hire_year}")

    def get_experience(self, current_year):
        return current_year - self.hire_year