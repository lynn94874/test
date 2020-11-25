import math


def f(x):
    a = math.sqrt((x ** float(x / 10)))
    return a


def integrate(a, b, n):
    ans = float(0)
    k = float((b - a) / n)

    for i in range(1, n+1):
        ans += k * f(float(a + k * (i - 0.5)))

    return ans


a = int(input())
b = int(input())
print(integrate(a, b, 100000))
