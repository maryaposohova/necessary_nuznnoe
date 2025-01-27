# def all_variants(text): # generator
#     l = len(text)
#     for start in range(l):
#         for end in range(start +1, l+1):
#             yield  text[start : end]
#
#
# a = all_variants("abc")
# for i in a:
#     print(i)
# """
# Результат:
# a
# ab
# abc
# b
# bc
# c
# """
# """
# ### Объяснение:
#
# 1. **Цикл `for size in range(1, l + 1)`:**
#    - Проходит по всем возможным длинам подстрок, начиная с 1 и до полной длины строки `l`.
#
# 2. **Цикл `for start in range(l - size + 1)`:**
#    - Определяет стартовую позицию подстроки с учетом текущей длины `size`, чтобы не выходить за пределы строки.
#
# 3. **`yield text[start:start + size]`:**
#    - Возвращает подстроку от позиции `start` длиной `size`.
#
# Таким образом, этот код генерирует подстроки в нужном порядке: сначала все одномерные, затем двумерные, и так далее.
#
# """


def all_variants(text):  # generator
    l = len(text)
    for size in range(1, l + 1):  # с 1 и до длины +1
        for start in range(l - size + 1):  # начало
            yield text[start:start + size]

a = all_variants("abc")
for i in a:
    print(i)
"""
Результат:
a
b
c
ab
bc
abc
"""

"""
Этот код определяет генераторную функцию `all_variants`, которая создает все возможные подстроки (последовательные 
подцепочки) из заданного текста. Давайте разберем его подробно.

### Функция `all_variants`

```python
def all_variants(text):  # generator
    l = len(text)
    for size in range(l):
        for simbol in range(size + 1, l + 1):
            yield text[size : simbol]
```

- **`text`**: Это входная строка, из которой будут генерироваться подстроки.
- **`l = len(text)`**: Вычисляем длину строки `text` и сохраняем ее в переменной `l`.
- **Внешний цикл `for size in range(l)`**: Этот цикл перебирает индексы от 0 до `l-1`, определяя начало подстроки.
- **Внутренний цикл `for simbol in range(size + 1, l + 1)`**: Этот цикл перебирает индексы от `size + 1` до `l`, 
определяя конец подстроки (не включая).
- **`yield text[size : simbol]`**: Генерирует подстроку от индекса `size` до `simbol` (не включая) и возвращает её. 
`yield` делает функцию генератором, который возвращает элементы по одному, сохраняя свое состояние между вызовами.

### Использование генератора

После определения функции генератора, переменной `a` присваивается генератор, вызванный с аргументом `"abc"`:

```python
a = all_variants("abc")
```

Цикл `for` итерируется по этому генератору, выводя каждую подстроку:

```python
for i in a:
    print(i)
```

### Результат выполнения

Вот какие подстроки будут выведены при запуске программы:

1. `a` (подстрока от индекса 0 до 1)
2. `ab` (подстрока от индекса 0 до 2)
3. `abc` (подстрока от индекса 0 до 3)
4. `b` (подстрока от индекса 1 до 2)
5. `bc` (подстрока от индекса 1 до 3)
6. `c` (подстрока от индекса 2 до 3)

Этот код эффективно генерирует и выводит все возможные подстроки строки `"abc"`. Каждый вызов `yield` 
возвращает подстроку, и выполнение функции приостанавливается до следующего обращения к генератору.
"""

"""
Ссылка на задание:
https://urban-university.ru/members/courses/course999421818026/20231204-
0000domasnee-zadanie-po-teme-generatory-155372347511
"""