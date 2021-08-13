duration = int(input('Введите время в секундах '))                     # Вводим int кол-во секунд для преобразования
duration_ans = ''                                                      # Обьявление переменной с ответом
while True:                                                            # Бесконечный цикл (заканчиваем на break)
    if duration >= 86400:                                              # Проверяем кол-во секунд на возможное наличие в них дней
        day = duration//86400                                          # Вычисление кол-ва дней (тип переменной - целочисленное)
        duration_ans = str(day) + ' дн '                               # создание строки ответа, который содежит перем. day ставшую строкой и добавление сокращенного обозначения дней
        duration = duration%86400                                      # Сокращение входного числа с секундами посредством остатка от деления на количество дней
        continue                                                       # Запускаем заново цикл
    if duration >= 3600:
        hour = duration//3600
        duration_ans = duration_ans + str(hour) + ' час '              # Добавляем всю строку в начале, чтобы не потерять ранее высчитанные дни
        duration = duration%3600
        continue
    if duration >= 60:
        minute = duration//60
        duration_ans = duration_ans + str(minute) + ' мин '
        duration = duration%60
        continue
    if duration < 60:
        duration_ans = duration_ans + str(duration) + ' сек'           # Так как нам не нужно преобразовывать секунды, то используем переменную duration
        break                                                          # Выходим из цикла при этом условии
    break                                                              # Также выходим из цикла, если число делиться на 60 без остатка
print('Длительность: ', duration_ans)                                  # Выводим полученный ответ