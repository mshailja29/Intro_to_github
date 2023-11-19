# Author: Shailja Manoj Maheshwari
# Date: 18th Nov 2023
# Description: Defines a subclass Supervisor inheriting from Employee, adding a private member variable for the supervisor's level,
# and overrides the pay calculation method to include a bonus based on the level.

from Employee import Employee

class Supervisor(Employee):
    def __init__(self, name, emp_id, pay_rate, level):
        super().__init__(name, emp_id, pay_rate)
        self. __level = level

    def calcPay(self, hours_worked):
        base_pay = super().calcPay(hours_worked)
        bonus = 1000.00 * self.__level
        return base_pay + bonus

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level