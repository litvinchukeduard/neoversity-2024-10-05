# import datetime
from datetime import datetime, timedelta

# import math

"""
Написати функцію, яка буде рахувати кількість днів між датами
"""
# 05-10-2024
# dd-mm-yyyy

def days_between_two_dates(date_one: str, date_two: str) -> int:
    """ A function to calculate difference between two dates in days """
    # result = "05-10-2024".split('-')
    # datetime(year=result[3])
    # result = datetime(2024, 6, 10).date() - datetime(2024, 5, 10).date()
    # print(result)

    # 05hello10
    # str p time
    # str parse time
    date_one_datetime = datetime.strptime(date_one, "%d-%m-%Y")
    date_two_datetime = datetime.strptime(date_two, "%d-%m-%Y")

    return (date_one_datetime - date_two_datetime).days

    # str f time
    # str format time
    # datetime.strftime(date, "")

print(days_between_two_dates("05-10-2024", "06-10-2024"))

