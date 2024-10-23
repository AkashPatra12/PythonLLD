print("\n\nDecorators")
def logger(func):
    def wrapper(*args, **kwargs):
        print("function called with args", args)
        result = func(*args, **kwargs)
        print("result is", result)
    return wrapper

@logger
def addition(a, b):
    return a+b

addition(5, 10)

print("\n\nDecorator chaining")

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

# Example usage
print(greet("Akash"))

