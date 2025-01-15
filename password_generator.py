import random
import string

def password_generator(min_length,numbers=True,special_chars=True):
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd)<min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria1 = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special
        
    return pwd

min_len = int(input("Enter The Minimum length Of The Password: "))
has_number = input("Do You want numbers in your password(y/n): ").lower() == "y"
has_special = input("Do You want Special Characters in your password(y/n): ").lower() == "y"

pwd=password_generator(min_len,has_number,has_special)
print(pwd) 

