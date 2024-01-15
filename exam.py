class NumberManipulator:
    def add_ten(self, number):
        return number + 10

if __name__ == "__main__":
    manipulator = NumberManipulator()
    input_number = float(input("Введіть число: "))
    result = manipulator.add_ten(input_number)
    
    print(f"Вхідне число: {input_number}")
    print(f"Результат після додавання 10: {result}")
