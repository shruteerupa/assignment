def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    elif n>1:
        for i in range(2, n + 1):
            print(a)
            temp=a
            a=b
            b=a+temp


import math


def CheckPerfect(x):
    i = int(math.sqrt(x))
    return (x == i * i)


def CheckFibo(n):
    if (CheckPerfect(5 * n * n + 4) or CheckPerfect(5 * n * n - 4)):
        print("Fibonacci")
    else:
        print("Not Fibonacci")
num =int(input('enter a the num'))
result_o=CheckFibo(num)
result=fibonacci(num)
print(result)
print(result_o)



