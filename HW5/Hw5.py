# AI. Порграма має відповісти на питання чи є введений стрінг
# 1 - номером телефону
# 2 - email-ом
# 3 - Іменем з ініціалами
# 4 - Даними невідомого формату
#
# +380631112233 -> Phone
# bcdef@abc.efg -> email   3+ letters @ 3 letters. 3 letters
# Bill J.I. -> name   2 words
# something else -> unknown

input_string = input("Input your data: ")

if (input_string.startswith("+380")
        and len(input_string) == 13
        and input_string[1:].isdigit()):
    print("Phone")


elif "@" in input_string:
    parts = input_string.split("@")
    if len(parts) == 2:
        username, domain = parts
        domain_parts = domain.split(".")
        if (len(username) >= 3
                and len(domain_parts[0]) >= 3
                and len(domain_parts[1]) >= 3):
            print("email")

elif " " in input_string:
    parts = input_string.split(" ")
    if len(parts) == 2:
        first_name, initials = parts
        if first_name.isalpha() and all(x.isalpha()
                                        or x == '.' for x in initials):
            print("name")

else:
    print("unknown")
