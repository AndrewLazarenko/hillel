# Доопрацюйте гру з занятя наступним чином:
# додайте підказки для користувача.
# якщо різниця між числами 1-2 - "Гаряче"
# якщо різниця між числами 3-5 - "Тепло"
# якщо різниця між числами 6 і більше- "Холодно"
# додайте лічильник спроб вгадати. користувач повинен вгадати число за
# фіксовану кількість спроб (визначіть кількість спроб самостійно).
# якщо він не вгадав за фіксовану кількість спроб -
# гра завершується з відповідним повідомленням
from random import randint


def get_user_number(prompt='Enter number', lower_limit=None, upper_limit=None):
    while True:
        try:
            res = int(input(f'{prompt}: '))
        except Exception:
            print('Wrong input!')
        else:
            if lower_limit is not None and res < lower_limit:
                print(f'Number should be bigger than {lower_limit}!')
                continue
            if upper_limit is not None and res > upper_limit:
                print(f'Number should be less than {upper_limit}!')
                continue
            return res


def get_comp_number(lower_limit, upper_limit):
    return randint(lower_limit, upper_limit)


def compare_numbers(comp_number, user_number):
    diff = abs(comp_number - user_number)
    if diff >= 1 and diff <= 2:
        return "Hot"
    elif diff >= 3 and diff <= 5:
        return "Warm"
    elif diff >= 6:
        return "Cold"


def game():
    lower_limit = 0
    upper_limit = 9
    max_tries = 5
    attempts = 0

    comp_number = get_comp_number(lower_limit, upper_limit)

    while attempts < max_tries:

        user_number = get_user_number(
            f'Guess the number [{lower_limit}-{upper_limit}]',
            lower_limit, upper_limit)
        attempts += 1

        if user_number == comp_number:
            print('Congratulations!')
            break
        else:
            hint = compare_numbers(comp_number, user_number)
            print(f'Try again! {hint}')
            print(f'Attempts remaining: {max_tries - attempts}')

    if attempts == max_tries:
        print("Game Over!")


game()
