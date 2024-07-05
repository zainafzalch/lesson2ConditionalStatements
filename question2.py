# 2. The Greatest Showdown

# Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

# Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4. "

number_1 = int(input("Input a number 1: "))
number_2 = int(input("Input a number 2: "))
number_3 = int(input("Input a number 3: "))

if number_1 > number_2 and number_1 > number_3:
    print(str(number_1) + " is the greatest")
elif number_2 > number_1 and number_2 > number_3:
    print(str(number_2) + " is the greatest")
else:
    print(str(number_3) + " is the greatest")

#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

def lowestAndHighest(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        print(str(num1) + " is the lowest")
    elif num2 <= num3 and num2 <= num1:
        print(str(num2) + " is the lowest")
    else:
        print(str(num3) + " is the lowest")

    if num1 >= num2 and num1 >= num3:
        print(str(num1) + " is the greatest")
    elif num2 >= num1 and num2 >= num3:
        print(str(num2) + " is the greatest")
    else:
        print(str(num3) + " is the greatest")

print(lowestAndHighest(int(input("Enter num1: ")), int(input("Enter num2: ")), int(input("Enter num3: "))))