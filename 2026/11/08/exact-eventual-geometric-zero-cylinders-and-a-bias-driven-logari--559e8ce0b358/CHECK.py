"""Finite, exact-rational cross-checks for zero-cylinder formulas.

Standard-library only. The analytic theorem is established by the written proof;
finite experiments do not certify unrestricted parameters or limits.
"""
from fractions import Fraction as F


def cutoff(a):
    j = 0
    while a * 2**j < 1:
        j += 1
    return j


def coefficient(a, p):
    j = cutoff(a)
    q = 1-p
    c = a / 2
    b = [min(F(1, 2), c * 2**k) for k in range(j+1)]
    integral = a + sum((b[k]-b[k-1])*(p**k+q**k)
                       for k in range(1, j+1))
    return 2*integral/(1+a)


def direct_integral(a, p, n):
    """Independent partition of each n-word cylinder, exact rational integration."""
    c = a / 2
    e = F(1, 2**n)
    cuts = {-e, e, F(0)}
    for k in range(n):
        for x in (-c/2**k, c/2**k, -F(1,2)/2**k, F(1,2)/2**k):
            if -e < x < e:
                cuts.add(x)
    cuts = sorted(cuts)
    mass = F(0)
    for left, right in zip(cuts, cuts[1:]):
        midpoint = (left+right)/2
        weight = F(1)
        for k in range(n):
            y = midpoint*2**k
            if abs(y) > F(1,2):
                weight = F(0)
                break
            if y > c:
                weight *= p
            elif y < -c:
                weight *= 1-p
        mass += (right-left)*weight
    return mass/(1+a)


def checks():
    count = 0
    for a in [F(1,64), F(1,32), F(1,10), F(1,4), F(2,5), F(1,2), F(3,4), F(1)]:
        for p in [F(1,8), F(1,3), F(1,2), F(3,4), F(7,8)]:
            j = cutoff(a)
            c = coefficient(a,p)
            assert F(0) < c <= 1
            assert (c == 1) == (a >= F(1,2))
            count += 2
            for n in range(max(1,j),max(1,j)+8):
                assert direct_integral(a,p,n) == c / 2**n
                count += 1
            if p == F(1,2):
                theta = 2**j*a
                assert c == a/(1+a)*(j+2/theta)
                count += 1
            if a >= F(1,2):
                assert c == 1
                count += 1
    print(f"PASS: {count} exact rational identities/inequalities")


if __name__ == '__main__':
    checks()
