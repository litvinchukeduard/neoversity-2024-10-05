import re
import random
import string
"""
Написати функцію, яка буде генерувати випадковий пароль потрібної довжини
"""
# generate_random_password(8) -> hgftdrM-

# Написати код, який буде генерувати рядок випадкових символів довжиною у password_length - 2

# Пароль має містити як мінімум одну літеру, одну літеру у верхньому регістрі та один спец-символ

# password_length <= 2 M a -
def generate_random_password(password_length: int) -> str:
    if password_length <= 2:
        raise ValueError
    
    password = ""
    for i in range(0, password_length - 2):
        password += chr(random.randint(97, 122))

    uppercase_letter = chr(random.randint(65, 90))
    special_character = chr(random.randint(33, 47))

    return password + uppercase_letter + special_character

# def generate_random_password_alternative():
    #  password.append(random.choice(string.ascii_letters + string.digits + '@#$%^&+='))

def generatepassord():
    password = []
    for i in range(8):
        password += (random.choice(\
            string.ascii_letters + string.digits + '@#$%^&+='))
    return ''.join(password)

print(generatepassord())


user_password = generate_random_password(8)

user_password = "hgftdrM-"

if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', user_password):
    print("Valid password")
else:
    if len(user_password) < 8:
        print("Password is too short")
    elif not re.match(r'[A-Za-z]', user_password):
        print("Password must contain at least one letter")
    elif not re.match(r'[^@#$%^&+=]', user_password):
        print("Password must contain at least one special character")