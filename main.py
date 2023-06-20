import math
import random
import docx
import hashlib
from docx import Document
import chardet


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def phi_n(p, q):
    if isPrime(p) and isPrime(q):
        phi = (p - 1) * (q - 1)
        return phi


def randomPrime():
    while True:
        a = random.randint(3, 150)
        if isPrime(a):
            return a


def euclid(b, phi):
    if gcd(b, phi) != 1:
        return None
    m0 = phi
    y = 0
    x = 1
    if phi == 1:
        return 0
    while b > 1:
        q = b // phi
        t = phi
        phi = b % phi
        b = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x


def public_key(p, q):
    phi = phi_n(p, q)
    arr = []
    for i in range(2, phi):
        if (gcd(i, phi) == 1) and (isPrime(i)):
            arr.append(i)
    if len(arr) == 0:
        return None
    return random.choice(arr)


def private_key(p, q, e):
    phi = phi_n(p, q)
    d = euclid(e, phi)
    return d


if __name__ == '__main__':
    p = 17
    q = 11
    e = public_key(p, q)
    d = private_key(p, q, e)
    print(e)
    print(d)
    b = 15
    c = b










































