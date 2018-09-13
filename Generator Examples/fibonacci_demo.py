#fibonacci_demo.py

def example_fibonacci():
    #Example: Fibonacci sequence using generators
    
    def fibonacci(limit):
        """ Generate the fibonacci sequence, stop when 
            we reach the specified limit """
        current = 0
        previous1 = 0
        previous2 = 0
        while current <= limit:
            return_value = current
            previous2 = previous1
            previous1 = current
            if current == 0:
                current = 1
            else:
                current = previous1 + previous2
            yield return_value

    for term in fibonacci(144):
        print(term)

example_fibonacci()
