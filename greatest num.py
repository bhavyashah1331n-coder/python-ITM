Num1=int(input("Enter the number1: "))
Num2=int(input("Enter the number2: "))
Num3=int(input("Enter the number3: "))
if (Num1 >= Num2) & (Num1 >= Num3):
    largest = Num1
elif (Num2 >= Num1) & (Num2 >= Num3):
    largest = Num2
else:
    largest = Num3
print("The Greatest Number is",largest)

