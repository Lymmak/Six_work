class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def get_numbers(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

if __name__ == '__main__':
    pass