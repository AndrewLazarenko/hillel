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

def determine_year_form(age):
    last_digit = age % 10
    last_two_digits = age % 100
    if 11 <= last_two_digits <= 14:
        return "років"
    elif last_digit == 1:
        return "рік"
    elif 2 <= last_digit <= 4:
        return "роки"
    else:
        return "років"
