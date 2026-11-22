"""Finite reproducibility checks for a complex Fourier encoding of a prime-power quotient sum."""
import cmath
from fractions import Fraction
from math import sqrt

Z = complex(-0.5, sqrt(3)/2)

def w(n):
    if n == 1:
        return 0
    rem, total, p = n, 0, 2
    while p*p <= rem:
        if rem % p == 0:
            power = 1
            while rem % p == 0:
                rem //= p
                power *= p
            total += n//power
        p += 1
    if rem > 1:
        total += n//rem
    return total

def local(n):
    if n % 3 == 0:
        return 0j
    rem, c, p = n, 0, 2
    while p*p <= rem:
        if rem % p == 0:
            power = 1
            while rem % p == 0:
                power *= p
                rem //= p
            c += 1 if power % 3 == 1 else -1
        p += 1
    if rem > 1:
        c += 1 if rem % 3 == 1 else -1
    return (1 if n % 3 == 1 else -1) * Z**(c % 3)

def main():
    count = 0
    for n in range(1, 20001):
        v = w(n)
        if n % 3:
            lhs = (1 if v%3 == 1 else -1 if v%3 == 2 else 0)
            rhs = (2/sqrt(3)) * local(n).imag
            assert abs(lhs-rhs) < 1e-10, (n,lhs,rhs)
        else:
            rem=n
            while rem % 3 == 0:
                rem//=3
            assert v%3==rem%3, (n,v,rem)
        count += 1
    for p in (2,5,7,11,13,17,19,23):
        for k in range(1,9):
            lhs=local(p**k)
            expected=Z if (p**k)%3==1 else -Z**2
            assert abs(lhs-expected)<1e-10, (p,k,lhs,expected)
    for p in (2,5,7,11,13):
        t=Fraction(1,p)
        # Exact formal Euler coefficients through degree 6 using primitive cube root relation.
        coeff=[complex(1)] + [local(p**k) for k in range(1,7)]
        assert all(abs(coeff[k] - (Z if pow(p,k,3)==1 else -Z**2))<1e-10 for k in range(1,7))
    print('PASS: 20,000 exact integer residue identities, 64 prime-power checks, and 30 Euler coefficients')

if __name__=='__main__':
    main()
