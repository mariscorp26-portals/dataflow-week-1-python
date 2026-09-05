# Assessment 14 - Palindrome

# A palindrome reads the same forwards and backwards.

word = input("Enter a word: ")

reverse = word[::-1]

if word == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")