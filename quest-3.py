import random


def get_jokes(n):
    '''
    Принимает на вход кол-во шуток, на выход - шутки.
    '''

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    d = []
    for _ in range(n):
        d.append(f"{nouns[random.randint(0, 4)]} {adverbs[random.randint(0, 4)]} {adjectives[random.randint(0, 4)]}")
    return d


print(get_jokes(int(input("Введите количество шуток: "))))
