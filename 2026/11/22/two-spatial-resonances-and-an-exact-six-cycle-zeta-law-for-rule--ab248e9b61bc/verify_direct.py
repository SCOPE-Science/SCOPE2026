#!/usr/bin/env python3
"""Independent direct bitwise exhaustive checker for finite cyclic Rule 22 rings.

Run: python3 verify_direct.py
Requires only Python standard library. Tests all states at n=3,...,20.
"""

def count_expected(n):
    a = 24 if n % 8 == 0 else 0
    b = 10 * (4**(n//10)+2) if n % 10 == 0 else 0
    return a+b

def rule22(x,n):
    mask = (1 << n)-1
    l = ((x << 1)&mask) | (x >> (n-1))
    r = (x >> 1) | ((x&1) << (n-1))
    return (l ^ x ^ r ^ (l&x&r)) & mask

def main():
    for n in range(3,21):
        periodic6 = 0
        periodic2 = 0
        periodic1 = 0
        periodic3 = 0
        for x in range(1 << n):
            y = rule22(x,n)
            z = rule22(y,n)
            a3 = rule22(z,n)
            a4 = rule22(a3,n)
            a5 = rule22(a4,n)
            a6 = rule22(a5,n)
            periodic6 += (a6 == x)
            periodic2 += (z == x)
            periodic1 += (y == x)
            periodic3 += (a3 == x)
        assert periodic3 == periodic1, (n,periodic3,periodic1)
        assert periodic6-periodic2 == count_expected(n), (n,periodic6,periodic2,count_expected(n))
        print('n=%2d Fix2=%d Fix6=%d least6_states=%d least6_orbits=%d' %
              (n,periodic2,periodic6,periodic6-periodic2,(periodic6-periodic2)//6))
    print('PASS: all 2^n input configurations at each n=3,...,20')

if __name__ == '__main__':
    main()
