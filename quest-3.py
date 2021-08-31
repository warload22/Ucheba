tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen():
    new_tutors = (el for el in tutors)
    new_klasses = (el for el in klasses)
    for items in zip(new_klasses, new_tutors):
        yield items[::-1]
    for rest in new_tutors:
        yield rest, None


f_gen = gen()
for idx in f_gen:
    print(idx)
    