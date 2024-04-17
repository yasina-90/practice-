import unittest

class TestMyDiv(unittest.TestCase):
    def test_my_div_with_two_positive_numbers(self):
        self.assertEqual(my_div(4, 2), 2)

    def test_my_div_with_two_negative_numbers(self):
        self.assertEqual(my_div(-4, -2), 2)

    def test_my_div_with_a_zero_dividend(self):
        self.assertEqual(my_div(0, 2), 0)

    def test_my_div_with_a_zero_divisor(self):
        self.assertEqual(my_div(4, 0), ValueError)

if __name__ == '__main__':
    unittest.main()
def my_sum(a,b):
    return a+b

def my_sub(a,b):
    return a-b

def my_mul(a,b):
    return a*b

def my_div(a,b):
    return a/b

def my_mod(a,b):
    return a%b

def my_exp(a,b):
    return a**b

def simple_calc():
    num1 = int(input("Enter first number: "))
    operator = input("\nEnter operator: + for addition, - for subtraction, * for multiplication, / for division, % for mod, ** for exponent: ")
    num2 = int(input("\nEnter second number: "))

    # Declreation
    if operator == "+":
        print (f'\n you want to sum between {num1} and {num2} ')
    if operator == "-":
        print (f'\n you want to minus between {num1} and {num2} ')
    if operator == "*":
        print (f'\n you want to multiply between {num1} and {num2} ')
    if operator == "/":
        print (f'\n you want to divide between {num1} and {num2} ')
    if operator == "%":
        print (f'\n you want to mod between {num1} and {num2} ')
    if operator == "**":
        print (f'\n you want to exponent between {num1} and {num2} ')

    # Operation
    if operator == "+":
        result = my_sum(num1,num2)
        print(f"{num1} + {num2} = ",result)
    elif operator == "-":
        result = my_sub(num1,num2)
        print(f"{num1} - {num2} = ",result)
    elif operator == "*":
        result = my_mul(num1,num2)
        print(f"{num1} * {num2} = ",result)
    elif operator == "/":
        result = my_div(num1,num2)
        print(f"{num1} / {num2} = ",result)
    elif operator == "%":
        result = my_mod(num1,num2)
        print(f"{num1} % {num2} = ",result)
    elif operator == "**":
        result = my_exp(num1,num2)
        print(f"{num1} ** {num2} = ",result)
    return result

c= simple_calc()
print(f'c is {c}')