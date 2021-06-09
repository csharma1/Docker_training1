def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number*factorial(number-1)
num = int(input("Enter a number to Find Factorial: "))
if num<0:
    print("Can't find Factorial for number less than zero")
else:
    print("Factorial of",num,"is:",factorial(num))
