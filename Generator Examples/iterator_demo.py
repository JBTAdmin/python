#iterator_demo.py

def example_basic():
    # Example: basic demo of iterators
    
    my_list = [1,2,3,"Python",4]
    my_tuple = (5,6,7,"Rocks")
    my_set = {8,9,10}
    for item in my_list:
        print(item)
    for item in my_tuple:
        print(item)
    for item in my_set:
        print(item)
    for x in range(5):
        print(x)

def example_for():
    # Example: for statement works over a list, but not over a float

    my_list = [3,5,7,9]
    my_float = 1.1
    for item in my_list:
        print(item)
    for item in my_float:
        print(item)

def example_next():
    # Example: using next() method
    # (Strings are iterables too!)
    
    import time

    my_string = "Python"
    print("Setting up the iterator...")
    iterator = iter(my_string)
    print("Let's see what our iterator looks like when printed...")
    print(iterator)
    print("It's a string iterator - we'll get the string back one character at a time")
    print("Now we'll print the first three characters")
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print("Taking a break - zzz")
    time.sleep(2)
    print("Now we'll print the last three characters")
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print("If we try to get more items, we'll get a StopIteration exception...")
    print("Normally you'd want to catch it with a try ... except block")
    print(next(iterator))

def example_custom():
    #Example: defining a custom iterable, then using an iterator to loop over it

    class PowersOfTwo:
        """Iterable object that returns the powers of two up to a specified limit"""
        def __init__(self,limit):
            self.limit = limit
        def __iter__(self):
            self.counter = 0
            return self
        def __next__(self):
            if self.counter < self.limit:
                number = self.counter
                self.counter += 1
                return 2 ** number
            else:
                raise StopIteration()

    #create the object
    my_powers = PowersOfTwo(8)
    print("Iterating using for")
    for i in my_powers:
        print(i)
    print("Iterating using iter/next")
    my_powers_iterator = iter(my_powers)
    print(next(my_powers_iterator))
    print(next(my_powers_iterator))
    print(next(my_powers_iterator))
    print("Three is enough!")

# example_next()
example_custom()