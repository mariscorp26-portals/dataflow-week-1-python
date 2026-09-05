# Assessment 7 - Return only even numbers

def get_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


numbers = [1, 2, 3, 4, 5, 6]

print("Even numbers:", get_even_numbers(numbers))