value = input("Enter a value in single character :- ")

if len(value) == 1:
    if value.lower() in "aeiou":
        print("It is a vowel")
    
    elif value.isalpha():
        print("It is a Conconent")
    else:
        print("Enter a valid input")
else:
    print("Enter only one character")