import csv
import os


# Custom exception 
class InvalidSalaryError(Exception):
    pass

# bonus function
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)
    if "cap" in options:
        result = min(result, options["cap"])
    return result


#  Classes 
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"{self.name} earns {self.salary} per month"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()} and manages {self.team_size} people"


#  Read data from employees.csv
path = os.path.join(os.path.dirname(__file__), "..", "employees.csv")
with open(path, newline="") as f:
    employees = list(csv.DictReader(f))
for e in employees:
    e["salary"] = int(e["salary"])   

# List comprehension: 
above_50k = [e["name"] for e in employees if e["salary"] > 50000]
print("Above 50000:", above_50k)

# map + lambda: 10% raise 
raised = list(map(lambda e: {**e, "salary": e["salary"] * 1.1}, employees))

# filter: Chennai employees
chennai = list(filter(lambda e: e["city"] == "Chennai", employees))
print("Chennai:", [e["name"] for e in chennai])

# try / except / finally 
try:
    emp = Employee("Test", -500)
except InvalidSalaryError as err:
    print("Error:", err)
finally:
    print("Transaction finished")

# for loop: 

stopped_at = None
for e in employees:
    s = e["salary"]
    if s == 0:
        continue          
    if s > 85000:
        stopped_at = e["name"]
        break             
