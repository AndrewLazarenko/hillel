# Наришіть декоратор, який вимірює час виконання функції
# Задекоруйте цим декоратором вашу програму "Касир"

import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {elapsed_time:.5f}"
              f": секунд")
        return result

    return wrapper


@timer_decorator
def verif_age():
    while True:
        try:
            age = int(input("Введіть ваш вік: "))
            if 0 <= age <= 124:
                return age
            else:
                print("Введіть вік в діапазоні від 0 до 124 років.")
        except ValueError:
            print("Введіть, будь ласка, ціле число")


@timer_decorator
def determine_year_form(age):
    last_digit = age % 10
    last_two_digits = age % 100
    if last_two_digits >= 11 and last_two_digits <= 14:
        return "років"
    elif last_digit == 1:
        return "рік"
    elif last_digit >= 2 and last_digit <= 4:
        return "роки"
    else:
        return "років"


@timer_decorator
def print_message(age):
    year_form = determine_year_form(age)
    if '7' in str(age):
        print(f"Вам {age} {year_form}, вам пощастить")
    elif age < 7:
        print(f"Тобі ж {age} {year_form}! Де твої батьки?")
    elif age < 16:
        print(f"Тобі лише {age} {year_form}, а це фільм для дорослих!")
    elif age > 65:
        print(f"Вам {age} {year_form}? Покажіть пенсійне посвідчення!")
    else:
        print(
            f"Незважаючи на те, що вам {age} {year_form}, білетів всеодно нема!")


age = verif_age()
print_message(age)
