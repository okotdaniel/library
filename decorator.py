def decorator(func):
    def wrapper(i):
        wrapper.called += 1
        return func(i)
    wrapper.called = 0
    return wrapper

@decorator
def decorated_func(i):
    return i + 1

if __name__ == '__main__':

    print(decorated_func.called)

    for i in range(5):
        print(decorated_func(i))

    print("Number of times decorator was called", decorated_func.called)