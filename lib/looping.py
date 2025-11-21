# looping.py

# Function 1: Countdown from 10 to 1 and print "Happy New Year!"
def happy_new_year():
    i = 10  # start at 10
    while i > 0:  
        print(i)
        i -= 1  
    print("Happy New Year!")  # final message

# Function 2: Square each integer in a list
def square_integers(int_list):
    return [x**2 for x in int_list]

# Function 3: FizzBuzz from 1 to 100
def fizzbuzz():
    for i in range(1, 101):  
        if i % 3 == 0 and i % 5 == 0:  
            print("FizzBuzz")
        elif i % 3 == 0:  
            print("Fizz")
        elif i % 5 == 0:  
            print("Buzz")
        else:  
            print(i)

# Optional: testing the functions
if __name__ == "__main__":
    print("Testing happy_new_year():")
    happy_new_year()
    
    print("\nTesting square_integers():")
    print(square_integers([1, 2, 3, 4, 5]))
    
    print("\nTesting fizzbuzz():")
    fizzbuzz()
