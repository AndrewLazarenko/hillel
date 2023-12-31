# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 6 - вивести повідомлення "Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить цифру 7 - вивести повідомлення "Вам пощастить!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
# P.S. На екран має бути виведено лише одне повідомлення,
# якщо вік користувача містить цифру 7 - тільки відповідне повідомлення!
# Також подумайте над варіантами, коли введені невірні або неадекватні (неможливі) дані.
age = input('Введіть ваш вік:')
if age.isdigit():
    verif_age = int(age)
    if '7' in str(verif_age):
        print('Вам пощастить!')
    elif verif_age < 6:
        print('Де твої батьки?')
    elif verif_age < 16:
        print('Це фільм для дорослих!')
    elif verif_age == 40:
        print('Ви Артем? Але білетів вже немає!')
    elif verif_age > 65 and verif_age < 124:
        print('Покажіть пенсійне посвідчення!')
    elif verif_age > 124:
        print('Перевірте введені данні')
    else:
        print('А білетів вже немає!')
else:
    print('Введіть будь ласка ціле число')
