#  функция для подсчета чисел (агрегация или агрегирование данных, чисел0
def sum_num_fron_range(start, finish):
    i = start
    sum = 0
    while i <= finish:
        sum += i
        i = i + 1
        # print(i, end=' ')
    return sum


print(sum_num_fron_range(2, 20))

