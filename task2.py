
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

print("Всі числа діапазону:", end=" ")
current_number = number1
while current_number <= number2:
    print(current_number, end=" ")
    current_number += 1
    

print("\nВсі числа діапазону в спадному порядку:", end=" ")
current_number = number2
while number1 <= current_number:
    print(current_number, end=" ")
    current_number -= 1
    
    
print("\nВсі числа, кратні 7:", end=" ")
current_number = number1
while current_number <= number2:
    if current_number %7 == 0 : 
        print(current_number, end=" ")
    current_number += 1


print("\nКількість чисел, кратних 5:", end=" ")
count_multiples_5 = 0
current_number = number1
while current_number <= number2:
    if current_number %5 == 0 : 
        count_multiples_5 += 1
    current_number += 1
print(count_multiples_5)