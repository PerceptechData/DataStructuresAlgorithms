import timeit

times = {
    'O(N)': None,
    'O(N^2)': None,
    'O(log n)': None,
    'O(2^n)': None,
    'O(n!)': None
}


def order_n(a, b):
    if a > b:
        return True
    else:
        return False


def order_n_squared(steps):
    for a in steps:
        for b in steps:
            print(a, ' ', b)


def log_time(N):
    for index in range(0, len(N), 3):
        print(N[index])


def fibonacci(n):
    if n <= 1:
        return n
    print(n)
    return fibonacci(n - 1) + fibonacci(n - 2)


def heap_permutation(data, n):
    if n == 1:
        print(data)
        return

    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]


start = timeit.default_timer()
order_n(1, 7)
stop = timeit.default_timer()
times['O(N)'] = stop - start

start = timeit.default_timer()
order_n_squared([1, 2, 3, 4, 5, 6, 7])
stop = timeit.default_timer()
times['O(N^2)'] = stop - start

start = timeit.default_timer()
log_time([1, 2, 3, 4, 5, 6, 7])
stop = timeit.default_timer()
times['O(log n)'] = stop - start

start = timeit.default_timer()
print(fibonacci(7))
stop = timeit.default_timer()
times['O(2^n)'] = stop - start

start = timeit.default_timer()
data = [1, 2, 3, 4, 5, 6, 7]
heap_permutation(data, len(data))
stop = timeit.default_timer()
times['O(n!)'] = stop - start


print(times)
