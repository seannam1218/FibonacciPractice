import time

memo = {}

def fib(n):
    for k in range(0, n+1):
        if k == 0:
            f = 0
        elif k == 1:
            f = 1
        else:
            f = memo[k - 1] + memo[k - 2]
        memo[k] = f
    return memo[n]

start_time = time.time()
print(fib(46660))
print("--- %s seconds ---" % (time.time() - start_time))