
# Користувач вводить із клавіатури два числа (початок і кінець діапазону). 
# Необхідно проаналізувати всі числа в цьому діапазоні. Потрібно вивести на екран:
# 1. Всі числа діапазону.
# 2. Всі числа діапазону в спадному порядку:
# 3. Всі числа, кратні 7.
# 4. Кількість чисел, кратних 5.

# Start and end of range
number1 = int(input("Enter start of range: "))
number2 = int(input("Enter end of range: "))

# If the range is specified from highest to lowest
if number2 < number1:
    number1, number2 = number2, number1

while number1 <= number2: 
    if number1 % 3 == 0:
        print("Fizz")
    elif number1 % 5 == 0:
        print("Buzz")
    elif number1 % 3 == 0 and number1 % 5 == 0:
        print("Fizz Buzz")
    else:
        print(number1)
    number1 += 1
        