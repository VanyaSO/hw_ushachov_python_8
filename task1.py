# Start and end of range
number1 = int(input("Enter start of range: "))
number2 = int(input("Enter end of range: "))

# If the range is specified from highest to lowest
if number2 < number1:
    number1, number2 = number2, number1
    

while number1 <= number2:
    if number1 %7 == 0 :   
        print(number1)
    number1 += 1
    
