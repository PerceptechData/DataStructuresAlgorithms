# Constant Time O(N)

def order_n(a, b):
    if a > b:
        return True
    else:
        return False


# order_n(5, 8)


# Squared Time O(N^2)

def order_n_squared(steps):
    for a in steps:
        for b in steps:
            print(a, ' ', b)


# order_n_squared([1, 2, 3, 4, 5, 6, 7])


# Logarithmic Time — O(log n)

def log_time(N):
    for index in range(0, len(N), 3):
        print(N[index])


# log_time([2, 4, 6, 8, 10, 12, 14, 16])


# Exponential Time O(2^n)

def fibonacci(n):
    if n <= 1:
        return n
    print(n)
    return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5))


# Factorial O(n!)
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


data = [1, 2, 3]
heap_permutation(data, len(data))
