# Task 1
print("Hello, World!")


# Task 2
name = input("What is your name? ")
age = input("How old are you? ")

print("Hello", name, "you are", age, "years old.")


# Task 3
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Task 4
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number * i)



# Task 5
number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)


# Task 6
numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number:", largest)


# Task 7
word = input("Enter a word: ")

count = 0

for letter in word:
    if letter in "aeiou":
        count = count + 1

print("Number of vowels:", count)


# Task 8
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)


# Task 9
word = input("Enter a word: ")

reverse = ""

for letter in word:
    reverse = letter + reverse

print("Reverse:", reverse)


# Task 10
a = 0
b = 1

for i in range(10):
    print(a)
    
    next_number = a + b
    a = b
    b = next_number

    