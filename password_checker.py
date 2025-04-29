import string

password = input("Enter your password: ")

length = len(password) >= 8
lower = any(char.islower() for char in password)
upper = any(char.isupper() for char in password)
digit = any(char.isdigit() for char in password)
special = any(char in string.punctuation for char in password)

if length and lower and upper and digit and special:
    print("Strong password!")
else:
    print("Weak password! Please include:")
    if not length:
        print("- At least 8 characters")
    if not lower:
        print("- At least one lowercase letter")
    if not upper:
        print("- At least one uppercase letter")
    if not digit:
        print("- At least one number")
    if not special:
        print("- At least one special character")
