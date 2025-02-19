# Умножение двух чисел

# def multiply_numbers_from_range(start, finish):
#     return start * finish
#
#
# print(multiply_numbers_from_range(5, 6))

# Умножение всех чисел
def mul_num_fron_range(start, finish):
    i = start
    mul = 1
    while i <= finish:
        mul *= i
        i = i + 1
        print(i, end=' ')
    return mul


print(mul_num_fron_range(2, 20))

# началось с 2 по 20
print(2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20)

