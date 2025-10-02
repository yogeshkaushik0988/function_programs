def timing_decorator(func):
    """
    A decorator that measures the execution time of a function.
    """
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@timing_decorator
def long_running_function(n):
    """A sample function to demonstrate decorator."""
    sum_val = 0
    for i in range(n):
        sum_val += i * i
    return sum_val

print(f"Result: {long_running_function(1000000)}")