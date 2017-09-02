import time

def fib(n):
    if n == 0:
        f = 0
    elif n == 1:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

start_time = time.time()
print(fib(40))
print("--- %s seconds ---" % (time.time() - start_time))