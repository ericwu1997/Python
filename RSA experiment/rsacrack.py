# main.py

"""
    name        : rsacrack.py
    author      : Eric Wu, A00961904
    data        : 03/20/2020
    description : This is a sample programe that simulate rsa cracking process
                  User should input a valid public key pair For example, 
                  rsacrack.py 3 187. The unit_test.sh in the same directory 
                  provides some sample testing data
"""

import sys
from lib.prime import *

"""This function calculate totient used for the private key generation
    Args:
        e (int): public key 
        n (int): modulus
    Returns:
        int: totient
"""
def calculateTotient(e, n):
    pair = primeFactor(n)
    if len(pair) != 2:
        return -1
    return ((pair[0]-1) * (pair[1]-1))

"""This function calculate private key
    Args:
        e (int): public key 
        n (int): totient
    Returns:
        int: private key
"""
def calculatePrivateKey(e, phi):
    # check if theres only two prime factor
    print("check prime factor...", end = '')
    factors=primeFactor(phi+1)
    if len(factors) == 2 and e in factors:
        if(factors[0]==e):
            return factors[1]
        return factors[0]
    print(" failed")

    # bruteforce
    print("bruteforce...",end = '')
    i=2
    while(True):
        if i%2 != 0 and (e*i)%phi == 1:
            print("         success")
            return i
        i=i+1

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Usage: e \u03C6")
        sys.exit()
    e = int(sys.argv[1])
    n = int(sys.argv[2])
    phi = calculateTotient(e, n)
    if phi == -1:
        print("Invalid key pair")
        sys.exit()
    private_key = calculatePrivateKey(e, phi)
    print("Private Key (d): ", private_key)