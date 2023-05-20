import math
import app 

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def sqrt(self, x):
        self.check_type(x)
        self.check_positive_number(x)
        return math.sqrt(x)

    def log10(self, x):
        self.check_type(x)
        self.check_positive_number(x)
        return math.log10(x)

    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be number")
        
    def check_positive_number(self, x):
        if x < 0:
            raise TypeError("Parameter must be positive number")
        
    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print('add', result)

    result = calc.substract(10, 2)
    print('substract', result)

    result = calc.multiply(4, 7)
    print('multiply', result)

    result = calc.divide(10, 10)
    print('divide', result)

    result = calc.power(3, 3)
    print('power', result)

    result = calc.sqrt(4)
    print('sqrt', result)

    result = calc.log10(-1000)
    print('log10', result)
