def foo():
    i = 1
    while i > 0:
        yield i
        i -= 1

for i in foo():
    print(i)