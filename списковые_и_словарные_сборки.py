a = [x for x in range(10) if x > 3]
b = [x ** 2 for x in range(5)]
print(a)  # [4, 5, 6, 7, 8, 9]
print(b)  # [0, 1, 4, 9, 16]
c_1 = {k: v for k, v in{'a':5, 'b':15, "c":20, "d":8}.items() if v < 10}
c_2 = {k: v for k, v in{'a':5, 'b':15, "c":20, "d":8}.items() if v > 10}
c_3 = {k: v for k, v in{'a':5, 'b':15, "c":20, "d":8}.items() if v == 10}
c_4 = {k: v for k, v in{'a':5, 'b':15, "c":20, "d":8}.items() if v != 10}
print(c_1)  # {'a': 5, 'd': 8}
print(c_2)  # {'b': 15, 'c': 20}
print(c_3)  # {}
print(c_4)  # {'a': 5, 'b': 15, 'c': 20, 'd': 8}
