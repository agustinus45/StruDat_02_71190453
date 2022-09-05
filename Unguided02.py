import timeit

def fibonacci_rekursif(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

def fibonacci_iteratif(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

n=10

start = timeit.default_timer()
fibonacci_rekursif(n)
end = timeit.default_timer()
rekursif = end-start

start = timeit.default_timer()
fibonacci_iteratif(n)
end = timeit.default_timer()
iteratif = end-start

for i in range(1,n+1):
    print('n =',i,', iteratif',iteratif,'detik, rekursif',rekursif,'detik')