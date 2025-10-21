'''
from random import randint

numbers = [randint(1, 10) for i in range(10)]
print("Исходный список:", numbers)

squared_numbers = [x**2 for x in numbers]
print("Список квадратов:", squared_numbers)

numbers = [2, 8, 4, 15, 6, 10, 12]

for num in numbers:
    if num == 15:
        break
    if num % 2 == 0:
        print(num)

numbers = [5, 12, 3, 9, 7, 12, 1]

max_value = max(numbers)
min_value = min(numbers) 

max_index = numbers.index(max_value)
min_index = numbers.index(min_value) 

print("Список:", numbers)
print("Наибольший элемент:", max_value, "его индекс:", max_index)
print("Наименьший элемент:", min_value, "его индекс:", min_index)
'''

text = input("Введите текст: ")
words = text.split()
glasni = "aeiou"

translated_words = []

for word in words:
    if word[0] in glasni:
        translated_words.append(word + "way")
    else:
        for i, letter in enumerate(word):
            if letter in glasni:
                translated_words.append(word[i:] + word[:i] + "ay")
                break
        else:
            translated_words.append(word + "ay")

translated_text = " ".join(translated_words)

print("Перевод на 'поросячью латынь':")
print(translated_text)