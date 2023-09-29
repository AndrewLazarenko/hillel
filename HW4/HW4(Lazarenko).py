# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран
# кількість слів, які містять дві голосні літери підряд.
text = input('Enter your text:')
vowels = "aeiouAEIOU"
words = text.split()
count = 0

for word in words:
    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            count += 1
            break

print(f"Number of words with two vowels in a row: {count}")
#Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
# "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720,
# "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких попадають в діапазон між мінімальною і максимальною ціною.
# Наприклад:
lower_limit = 35.9
upper_limit = 37.339
prices = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

matching_stores = [store for store, price in prices.items()
                   if lower_limit <= price <= upper_limit]

print(f'match:{matching_stores}')