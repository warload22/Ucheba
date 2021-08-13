for percentage in range(100):
    percentage = percentage + 1
    if percentage // 10 == 1:
        print(percentage, ' процентов')
    elif percentage % 10 == 1:
        print(percentage, ' процент')
    elif percentage % 10 == 2 or percentage % 10 == 3 or percentage % 10 == 4:
        print(percentage, ' процента')
    else:
        print(percentage, ' процентов')