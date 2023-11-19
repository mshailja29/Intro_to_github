# Author: Shailja Manoj Maheshwari
# Date: 18th Nov 2023
# Description: Manages a small company's employees by providing functions to calculate total pay for a list of employees and to list employee information.
# Includes a main function for user interaction, allowing the addition of supervisors and workers to a
# list and displaying their information and total pay.
from Supervisor import Supervisor
from Worker import Worker

def calcTotalPay(employee_list):
    total_pay = 0
    for emp in employee_list:
        total_pay += emp.calcPay(40)  # Assuming each employee has worked 40 hours
    return total_pay

def listEmployees(employee_list):
    for emp in employee_list:
        if isinstance(emp, Supervisor):
            print(f"Supervisor: {emp.get_name()}, ID: {emp.get_emp_id()}, Pay Rate: ${emp.get_pay_rate()}, Level: {emp.get_level()}")
        elif isinstance(emp, Worker):
            print(f"Worker: {emp.get_name()}, ID: {emp.get_emp_id()}, Pay Rate: ${emp.get_pay_rate()}, Shift: {emp.get_shift()}")

def main():
    employees = []
    num_employees = int(input("How many employees do you want to add? "))

    for _ in range(num_employees):
        emp_type = input("Do you want to add a Supervisor or a Worker? ").lower()

        if emp_type == "supervisor":
            name = input("Enter Supervisor's name: ")
            emp_id = input("Enter Supervisor's ID: ")
            pay_rate = float(input("Enter Supervisor's pay rate: "))
            level = int(input("Enter Supervisor's level: "))
            supervisor = Supervisor(name, emp_id, pay_rate, level)
            employees.append(supervisor)
        elif emp_type == "worker":
            name = input("Enter Worker's name: ")
            emp_id = input("Enter Worker's ID: ")
            pay_rate = float(input("Enter Worker's pay rate: "))
            shift = int(input("Enter Worker's shift (1 for day, 2 for night): "))
            worker = Worker(name, emp_id, pay_rate, shift)
            employees.append(worker)
        else:
            print("Incorrect input. Please try again.")

    listEmployees(employees)
    total_pay = calcTotalPay(employees)
    print(f"Total pay for all employees: ${total_pay}")

if __name__ == "__main__":
    main()
