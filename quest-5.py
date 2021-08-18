prices = [57.8, 46.51, 97, 22.32, 17.03, 39.5, 63, 74.2, 85, 91.1]
idx = 0
answer = []
while idx < len(prices):
    prices_parts = str(prices[idx]).split('.')
    if len(prices_parts) == 2:
        answer.append(f"{prices_parts[0]} руб {int(prices_parts[1]):02d} коп")
    else:
        answer.append(f"{prices_parts[0]} руб 00 коп")
    idx += 1
print(", ".join(answer))
new_answer = answer
answer.sort()
print(", ".join(answer))
new_answer.sort(reverse=True)
print(", ".join(new_answer))
print(", ".join(sorted(new_answer[:5])))
