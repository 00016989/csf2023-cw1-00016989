v = int(input("Untill which number you need fibonacci numbers: "))
a = [0]
i = 1
def fibonacci(c):
    i = 1
    while True:
        a.append(i)
        i = i + a[-2]
        if i > c:
            break
    a.remove(0)
    return a
f = fibonacci(v)
print(f)
