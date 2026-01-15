def add(a, b):
    return a + b

def test(a, b):
    assert add(5, 2) == 7
    
def subtract(a, b):
    return a - b

def tst_subtract(a, b):
    assert subtract(5, 2)==3
    
import pytest
from OOP import school, employee, payment
def test_school_info():
    school = school.School("sajah", "ktm")
    assert school.get_info() == "school name: sajah, location: ktm"

def test_employee_display():
    emp = employee.Employee("sajah", 101)
    assert emp.display() == "employee name: sajah, id: 101"

def test_payment_cash():
    cash_payment = payment.Cash(100, "USD")
    assert cash_payment.show() == "Payment amount: 100 USD"
    