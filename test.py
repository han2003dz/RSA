import math
import random


class code:
    def input(self, values):
        while True:
            p = int(values['-P-'])
            q = int(values['-Q-'])
            if(self.is_prime(p) and self.  s_prime(q)):
                return True


    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    # check số nguyên tố
    def is_prime(self, n):
        if n <= 2: return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
#     random số nguyên tố
    def random_prime(self, phi):
        while True:
            num = random.randint(2, phi)
            if self.is_prime(num)
                return num



