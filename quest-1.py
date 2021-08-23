def num_translate_adv(number):
    numbers = {'zero': 'ноль',
               'one': 'один',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}
    if number[0].isupper() and numbers.get(number.lower()):
        return numbers.get(number.lower()).title()
    else:
        return numbers.get(number)


number = input('Введите число: ')
print(num_translate_adv(number))
