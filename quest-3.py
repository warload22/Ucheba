items = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
idx = 0
while idx < len(items):
    if items[idx].isdigit() or ('+' in items[idx] and items[idx][1:].isdigit()) or (
            '-' in items[idx] and items[idx][1:].isdigit()):
        if ('+' in items[idx] and items[idx][1:].isdigit()) or ('-' in items[idx] and items[idx][1:].isdigit()):
            items[idx] = items[idx][0:].zfill(3)
        else:
            items[idx] = items[idx].zfill(2)
        items[idx] = '"' + items[idx] + '"'
        idx += 1
    else:
        pass
    idx += 1
print(' '.join(items))
