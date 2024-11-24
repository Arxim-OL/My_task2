# Задание "Слишком древний шифр"
min_first_stones = 3
min_second_stones = 1
max_stones = 20
first_field_of_stones = []
stones = []

for i in range (max_stones + 1):
    if i >= min_first_stones:
        first_field_of_stones.append (i)
    if i >= min_second_stones:
        stones.append (i)
for x in first_field_of_stones:
    second_field_of_stones = []
    for y in stones:
        if y > x:
            break
        for z in stones:
            if z < y or z == y:
                continue
            if z > x:
                break
            if x % (y + z) == 0:
                second_field_of_stones.append (y)
                second_field_of_stones.append (z)
    string = ''
    for j in second_field_of_stones:
        string += str (j)
    print(x, '-',string)



