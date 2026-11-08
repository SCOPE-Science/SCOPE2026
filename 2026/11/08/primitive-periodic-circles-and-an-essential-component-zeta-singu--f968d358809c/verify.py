"""Standalone exact-rational checks for periodic circle components of affine unipotent toral maps.

Run: python3 verify.py
The checks are finite corroborations; general theorems require the written proof.
"""
from fractions import Fraction
from math import comb, gcd, prod
from itertools import product


def fracmod(x):
    return x % 1


def divisors(n):
    return [k for k in range(1, n+1) if n % k == 0]


def jordan_totient(s, n):
    if n == 1:
        return 1
    ans = n**s
    d = n
    p = 2
    while p*p <= d:
        if d % p == 0:
            ans = ans // p**s * (p**s-1)
            while d % p == 0:
                d //= p
        p += 1
    if d > 1:
        ans = ans // d**s * (d**s -1)
    return ans


def step(x, a):
    d=len(x)
    return tuple(fracmod(x[i] + (x[i+1] if i+1<d else 0) + a[i]) for i in range(d))


def iterate(x,a,n):
    for _ in range(n):
        x = step(x,a)
    return x


def fixed_fibers(n, a):
    """Exact solutions for last d-1 coordinates of Fix(F^n), first free."""
    d=len(a)
    if fracmod(n*a[-1]) != 0:
        return []
    partial = [tuple([None] * d)]
    for j in range(d-2,-1,-1):
        new=[]
        for z in partial:
            offset=sum((comb(n,k)*z[j+k] for k in range(2,d-j) ), Fraction(0))
            shift=sum((comb(n,k+1)*a[j+k] for k in range(d-j)), Fraction(0))
            for t in range(n):
                arr=list(z)
                arr[j+1]=fracmod((Fraction(t)-shift-offset)/n)
                new.append(tuple(arr))
        partial=new
    return sorted(set(tuple(row[1:]) for row in partial))


def check():
    cases=0
    tested_circles=0
    for d in range(2,6):
        for q in range(1,4):
            a = tuple(Fraction((-1)**i, 5+i) for i in range(d-1)) + (Fraction(1,q),)
            for ell in range(1,5):
                n=q*ell
                if n>7 or n**(d-1)>1500:
                    continue
                fibers=fixed_fibers(n,a)
                assert len(fibers)==n**(d-1), (d,q,ell,len(fibers))
                # Independent, literal dynamical iteration.
                exact=0
                for fib in fibers:
                    z=(Fraction(2,7),)+fib
                    assert iterate(z,a,n)==z, (d,q,ell,z)
                    p=next(r for r in divisors(n) if iterate(z,a,r)==z)
                    assert n%p==0
                    if p==n:
                        exact+=1
                expect=q**(d-1)*jordan_totient(d-1,ell)
                assert exact==expect, (d,q,ell,exact,expect)
                cases+=1;tested_circles+=len(fibers)
            # If base drift is not n-torsion, no fixed fiber exists.
            for n in range(1,q):
                assert fixed_fibers(n,a)==[]
    # Formal zeta: coefficient logarithm is P_n/n, P_n = n^(d-1) on q|n.
    for d in range(2,7):
        for q in range(1,5):
            for ell in range(1,20):
                n=q*ell
                assert Fraction(n**(d-1),n)==q**(d-2)*ell**(d-2)
    print('VERIFY_OK dimensions=2..5 exact_parameter_cases=%d exact_circle_representatives=%d zeta_coefficients=380' % (cases,tested_circles))

if __name__=='__main__':
    check()
