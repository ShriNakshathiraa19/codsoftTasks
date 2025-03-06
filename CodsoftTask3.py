import random
import string

def generate_password(length):
    
    letters = string.ascii_letters  
    digits = string.digits  
    special_chars = string.punctuation  

    
    all_chars = letters + digits + special_chars

    
    password = (
        random.choice(letters) +
        random.choice(digits) +
        random.choice(special_chars)
    )

    
    password += ''.join(random.choices(all_chars, k=length - 3))

    
    password = ''.join(random.sample(password, len(password)))

    return password


try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password length should be at least 4 characters for security.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number for password length.")
