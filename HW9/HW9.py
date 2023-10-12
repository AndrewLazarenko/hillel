from lib import timer_decorator
from lib import verif_age
from lib import determine_year_form


@timer_decorator
def cashier(age):
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
cashier(age)
