# Агрегация строк (агрегация - это накопление результата во вр итерации (result += text))
def repeat(text, times):
    result = ''
    i = 1
    while i <= times:
        result += text
        i = i + 1
    return result

result = ''
result = result + ' 1234'
result = result + ' 1234'
result = result + ' 1234'

print(repeat('1234 ', 4))