if __name__=="__main__":
 print("Script is running directly")

#Write a decorator that calls a function twice.

def twice_func(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@twice_func
def hola():
    return print('Hola')

hola()