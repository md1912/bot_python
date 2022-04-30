def convert_dollars(dollars):
    return 'Юань: {:,.3f}'.format(dollars * 6.75)

print(convert_dollars(15))