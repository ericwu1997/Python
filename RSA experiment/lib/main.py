"""
    name    : main.py
    author  : Eric Wu, A00961904
    data    : 03/20/2020
"""

from prime import *

def main():
    """This is the driver function
    """
    print("getMod(5,15,13) -> ", getMod(5,15,13))
    print("getMod(15,18,17) -> ", getMod(15,18,17))
    print("getMod(456,18,17) -> ", getMod(456,18,17))
    print("getMod(145,102,101) -> ", getMod(145,102,101))
    print("getMod(14,3,12) -> ", getMod(14,3,12))
    print("")
    print("isPrime(10) -> ", isPrime(10))
    print("isPrime(57) -> ", isPrime(57))
    print("isPrime(97) -> ", isPrime(97))
    print("isPrime(23) -> ", isPrime(23))
    print("isPrime(2) -> ", isPrime(2))
    print("")
    print("listPrimes(37) -> ", listPrimes(37))
    print("listPrimes(20) -> ", listPrimes(20))
    print("listPrimes(2) -> ", listPrimes(2))
    print("listPrimes(81) -> ", listPrimes(81))
    print("listPrimes(49) -> ", listPrimes(49))
    print("")
    print("gcd(5,7) -> ", gcd(5,7))
    print("gcd(10,100) -> ", gcd(10,100))
    print("gcd(38,52) -> ", gcd(38,52))
    print("gcd(24,48) -> ", gcd(24,48))
    print("gcd(50,20) -> ", gcd(50,20))
  
main()