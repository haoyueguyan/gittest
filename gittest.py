print("123")
def new_func():
    print("test")

def new_func1(new_func):
    new_func()

new_varnew_var = new_func1(new_func)
