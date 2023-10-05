"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(number):
    increaser = int(2)
    while increaser <= number/2:
        if number % increaser == 0:
            return False
        else:
            increaser += 1
    return True

def primes(number_of_primes):
    list = []
    num = 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
            num += 1
        else:
            num += 1

    return list

while True:
    try:
        inputs = int(input("Enter number of primes to get here:"))
        if inputs<1:
            print("Must be a positive integer, try again:")
        else:
            break
    except ValueError:
        print("That wasn't an integer value, try again:")
    else:
        break



print(primes(inputs))