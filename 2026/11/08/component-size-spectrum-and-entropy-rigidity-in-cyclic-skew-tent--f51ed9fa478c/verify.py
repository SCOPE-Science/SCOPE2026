"""Exact finite verification of the twisted cyclic-label orbit census.
Only Python standard-library modules are required.
"""
from itertools import product
from math import gcd
from collections import Counter
from fractions import Fraction


def mobius(n):
    if n == 1:
        return 1
    mu, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            mu = -mu
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -mu if n > 1 else mu


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def coprime_part(n, k):
    a = n
    while gcd(a,k)>1:
        a //= gcd(a,k)
    return a


def twist(v,k):
    return v[1:] + ((v[0]+1)%k,)


def theoretical(k,n):
    a = coprime_part(n,k)
    b = n//a
    out = {}
    for d in divisors(a):
        primitive = sum(mobius(d//e) * k**(b*e) for e in divisors(d))
        assert primitive > 0
        assert primitive%(k*b*d)==0
        out[k*b*d] = primitive//(k*b*d)
    assert sum(length*c for length,c in out.items())==k**n
    return out


def exhaustive(k,n):
    todo = set(product(range(k), repeat=n))
    counts = Counter()
    while todo:
        initial = next(iter(todo))
        x = initial
        orbit=[]
        while x not in orbit:
            orbit.append(x)
            x=twist(x,k)
        assert x==initial
        for y in orbit:
            assert y in todo
            todo.remove(y)
        counts[len(orbit)] += 1
    return dict(counts)


def test():
    cases=0
    points=0
    for k in range(2,9):
        for n in range(2,9):
            if k**n>15000:
                continue
            got = exhaustive(k,n)
            expected=theoretical(k,n)
            assert got==expected, (k,n,got,expected)
            a=coprime_part(n,k)
            b=n//a
            total=Fraction(0)
            for d in divisors(a):
                length=k*b*d
                weight=Fraction(got[length]*length,k**n)
                expected_weight=Fraction(sum(mobius(d//e)*k**(b*e) for e in divisors(d)),k**n)
                assert weight==expected_weight
                total += weight
            assert total==1
            cases+=1
            points+=k**n
    assert theoretical(4,3)=={4:1,12:5}
    assert Fraction(4,4**3)==Fraction(1,16)
    assert theoretical(3,2)=={3:1,6:1}
    assert theoretical(10,6)=={20:5,60:16665}
    print(f'PASS: {cases} exhaustive (k,n) pairs, {points} labeled points; formulas, normalization, and examples verified')

if __name__ == '__main__':
    test()
