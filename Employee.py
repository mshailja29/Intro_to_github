# Author: Shailja Manoj Maheshwari
# Date: 18th Nov 2023
# Description: This program defines a base class Employee with protected member variables for name, ID,
# and pay rate, along with methods for calculating pay and accessing/modifying member variables.

class Employee():
    def __init__(self, name, emp_id,pay_rate):
        self._name = name
        self._emp_id = emp_id
        self._pay_rate = pay_rate

    def calcPay(self, hours_worked):
        return hours_worked * self._pay_rate

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, emp_id):
        self._emp_id = emp_id

    def get_pay_rate(self):
        return  self._pay_rate

    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate