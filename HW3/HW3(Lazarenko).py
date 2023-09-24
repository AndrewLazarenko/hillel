# 1 завдання:
# Напишіть код, який зформує строку, яка містить певну інформацію
# про символ за його номером у слові. Наприклад
# "The [номер символу] symbol in '[тут слово]' is ' [символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".\
word = input("Enter word:")
counter = input("Enter number:")
if counter.isdigit():
    counter = int(counter)
    try:
        print(f"The {counter} symbol in {word} is {word[counter - 1]}")
    except:
        print("Error! There is no symbol with that number")
else:
    print('Only numbers are supported')

# 2 завдання
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.
string = input("Enter your phrase to count the number of words:")
res = string.split()
if len(res) >= 1:
    print(f'In your phrase {len(res)} word')
else:
    print(f'In your phrase {len(res)} words')

# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7.0, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for data in lst1:
    if type(data) == int or type(data) == float:
        lst2.append(data)
print(lst2)
