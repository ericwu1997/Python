"""
    name    : prime.py
    author  : Eric Wu, A00961904
    data    : 03/20/2020
"""
import math

def getMod(b,e,m):
    """This function returns the modulus of a given number
    Args:
        b (int): base of the number
        e (int): exponent
        m (int): modulus
    Returns:
        int: modulus result
    """
    return (b ** (e)) % m

def isPrime(x):
    """This function check if a number is prime or not
    Args:
        x (int): number to be checked
    Returns:
        bool: true if the number is prime, false otherwise
    """
    if x > 1:
        for i in range(2, (int)(math.sqrt(x))+1):
            # if the number is divisible by smaller number, return False
            if (x % i) == 0:
                return False
        else:
            return True

def listPrimes(n):
    """This function returns a list of prime number in a given range
    Args:
        n (int): range of number to check for prime, starting from 1.
    Returns:
        list of prime number found in range, empty if none
    """
    prime_list = []
    if(n < 3):
        # if n == 2, append 2 to prime list
        if (n == 2):
            prime_list.append(2)
        return prime_list
    else :
        prime_list.append(2)
        # check for prime starting from 3 up to n
        for i in range(3, n):
            # if a prime is found, append to list
            if(isPrime(i)):
                prime_list.append(i)
    return prime_list

def gcd(a,b):
    """This function gets the greatest common devisor between two number
    Args:
        a (int): first number
        b (int): second number
    Returns:
        int: the greatest common devisor
    """
    # Get the smaller number between a & b
    small = b if a > b else a
    # check for gcd from 1 up to the lower number between a & b
    for i in range(1, small+1): 
        if((a % i == 0) and (b % i == 0)): 
            gcd = i 
    return gcd

def primeFactor(n):
    """This function gets the prime factor of a given number n
    Args:
        n (int): number
    Returns:
        list of prime factor
    """
    prime_list = []
    # If n less than 2, return n
    if (n < 2):
        prime_list.append(n)
        return prime_list
    # Get all factor of 2 and append to list
    while n % 2 == 0: 
        prime_list.append(2)
        n = n / 2
    # Check through prime number less then sqrt(n)
    for i in range(3,int(n+1),2):
        while n % i== 0: 
            prime_list.append(i)
            n = n / i
    return prime_list
