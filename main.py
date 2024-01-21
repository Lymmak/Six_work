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

    def select_operation(self):
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            return self.add()
        elif choice == '2':
            return self.subtract()
        elif choice == '3':
            return self.multiply()
        else:
            return "Invalid choice"

if __name__ == '__main__':
    calculator = Calculator()
    calculator.get_numbers()
    result = calculator.select_operation()
    print("Result:", result)