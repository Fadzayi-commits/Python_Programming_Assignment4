def factorial(n):
    fac = n
    for i in range(1, n):
        fac *= i
    return fac
print(factorial(5))