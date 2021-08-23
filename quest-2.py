def thesaurus_adv(*args):
    d = dict()
    for name in args:
        lastname = name.split()[1][0]
        firstname = name[0]
        if lastname not in d:
            d[lastname] = dict()
        if firstname not in d[lastname]:
            d[lastname][firstname] = []
        d[lastname][firstname].append(name)
    return d


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
