x = int(input("Enter a number of repetitions: "))

def repeat(num_times):
    def decorator(func):
        def wrapper():
            for _ in range(num_times):
                func()
        return wrapper
    return decorator

@repeat(x)
def hello():
    print('Hello')

hello()