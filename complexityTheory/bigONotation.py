# Constant Complexity (O(C))

def constant_algo(items):
    result = items[0] * items[0]
    print(result)


constant_algo([4, 5, 6, 8])


# Linear Complexity (O(n))

def linear_algo(items):
    for item in items:
        print(item)


linear_algo([4, 5, 6, 8])


# Quadratic Complexity (O(n^2))
def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item)


quadratic_algo([4, 5, 6, 8])
