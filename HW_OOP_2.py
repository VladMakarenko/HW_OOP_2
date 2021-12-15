from datetime import date, datetime
import numpy as np

class Employee:
    def __init__(self, first_name, last_name, email, phone, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.salary = salary

    @staticmethod
    def work():
        return "I come to the office"

    def check_salary(self, month):
        d1 = date(2021, month, 1)
        d2 = datetime.now()
        work_day = np.busday_count(d1.strftime("%Y-%m-%d"), d2.strftime("%Y-%m-%d"))
        work_day = work_day + 1
        salary_day = self.salary * work_day
        return salary_day

    def level_salary(self, salary_recruiter, salary_programmer):

        if salary_recruiter < salary_programmer:
            return 'a programmer with a higher salary\n'
        else:
            return 'a recruiter with a higher salary\n'


class Recruiter(Employee):
    position = "Recruiter"
    hired_this_month = ""

    def __str__(self):
        return f'{self.position}:' + f' {self.first_name} {self.last_name}'

    @staticmethod
    def work():
        return "I come to the office and start hiring"


class Programmer(Employee):
    position = "Programmer"
    tech_stack = ''
    closed_this_month = ''

    def __str__(self):
        return f'{self.position}:' + f' {self.first_name} {self.last_name}\n'

    @staticmethod
    def work():
        return "I come to the office and start coding"


a = Recruiter("Ivanov", "Ivan", "asd@gmail", "911", 1000)
b = Programmer("Petrov", "Petr", "adasdasda@gmail", "102", 5000)

print('Salary recruiter = ' + str(a.check_salary(12)))
print('Salary programmer = ' + str(b.check_salary(12)) + '\n')

print(a.level_salary(1000, 5000))

print(a.__str__())
print(b.__str__())

print(a.work())
print(b.work())
