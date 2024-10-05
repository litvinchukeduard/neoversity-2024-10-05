from datetime import datetime
'''
Написати функцію, яка буде рахувати вік людини
'''

def calculate_persons_age(birthday_date: datetime) -> int:
    """ A function to calculate persons age """
    today = datetime.now().date()
    # days = (today - birthday_date.date()).days
    age = today.year - birthday_date.year

    # if (today.month < birthday_date.month) or (today.day < birthday_date.day)
    # if (today.month < birthday_date.month) or (today.month == birthday_date.month and today.day < birthday_date.day):

    if ((today.month, today.day) < (birthday_date.month, birthday_date.day)):
        age -= 1

    if age < 0:
        age = 0


    return age


person_one_birthday = datetime(2000, 1, 1) # age = 24
person_two_birthday = datetime(2024, 9, 5) # age = 0
person_three_birthday = datetime(2023, 10, 4) # age = 1
person_four_birthday = datetime(2023, 11, 4) # age = 0
person_five_birthday = datetime(2025, 10, 10) # age = 0 

print(calculate_persons_age(person_one_birthday))
print(calculate_persons_age(person_two_birthday))
print(calculate_persons_age(person_three_birthday))
print(calculate_persons_age(person_four_birthday))
print(calculate_persons_age(person_five_birthday))