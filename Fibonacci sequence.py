def fib(n):
   if n <= 1:
    return n
   else:
        return(fib(n-1) + fib(n-2))


terms = 10


if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fib(i))