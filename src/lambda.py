A = 3


def get_func():
    return lambda x: x | A


print(get_func()(4))

m = map(lambda x, y: x + y, ((999, 2), (4, 5)), ((3, 4), (6, 8)))
print(list(m))
