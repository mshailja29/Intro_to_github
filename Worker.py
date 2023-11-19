# Author: Shailja Manoj Maheshwari
# Date: 18th Nov 2023
# Description: Defines a subclass Worker inheriting from Employee, adding a private member variable for shift (day or night),
# and providing methods to access and modify the shift information.

from Employee import Employee

class Worker(Employee):
    def __init__(self, name, emp_id, pay_rate, shift):
        super().__init__(name, emp_id, pay_rate)
        self.__shift = shift

    def get_shift(self):
        return self.__shift

    def set_shift(self, shift):
        self.__shift = shift