first = input ('Введите first = ')
second = input ('Введите second = ')
third = input ('Введите third = ')

if first == second and first == third:
    print (3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)