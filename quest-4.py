items = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
idx = 0
while idx < len(items):
    items_parts = items[idx].split(' ')
    print('Привет,', items_parts[-1].capitalize() + "!")
    idx += 1
