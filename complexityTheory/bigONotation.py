# Linear Complexity O(N)

def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])


# Quadratic Complexity O(n^2)

def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item2)


quadratic_algo([4, 5, 6, 8])
