import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result = func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__}ran in {end-start} time")
        return result
    return wrapper

# timer function is called when we apply decorator then every function move from inside the decorator function like timer
@timer
def example_function(n):
    time.sleep(n)
    
example_function(2)