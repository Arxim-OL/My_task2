# Задача "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for x in numbers:
    if x == 0 or x == 1:
        continue
    is_prime = True
    for y in range(x):
        if y == 0 or y == 1:
            continue
        if x % y == 0:
            is_prime = False
    if is_prime:
        primes.append(x)
    else:
        not_primes.append(x)
print ('Исходный код:')
print ('numbers =',numbers)
print ('Вывод на консоль:')
print ('primes:', primes)
print ('not_primes:', not_primes)

