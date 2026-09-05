# Assessment 5 - FizzBuzz

# Print numbers from 1 to 50.
# Multiples of 3 = Fizz
# Multiples of 5 = Buzz
# Multiples of both = FizzBuzz

for number in range(1, 51):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)