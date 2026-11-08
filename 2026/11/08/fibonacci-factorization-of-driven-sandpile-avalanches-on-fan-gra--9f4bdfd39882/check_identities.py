"""Independent integer and exact-algebra tests for the fan avalanche formulas.

Only Python standard library. Run: python check_identities.py
"""
from fractions import Fraction
from math import sqrt


def fib(n):
    u, v = 0, 1
    for _ in range(n): u, v = v, u+v
    return u


def w(m):
    return 1 if m == 0 else fib(2*m)


def det_tridiagonal_fan(n):
    # Continuant for the path-plus-sink reduced Laplacian.
    a0, a1 = 1, 2
    for k in range(2,n+1):
        d = 2 if k == n else 3
        a0, a1 = a1, d*a1-a0
    return a1


def exact_case(n,j):
    total = fib(2*n)
    assert det_tridiagonal_fan(n) == total
    weights = []
    for L in range(1,j+1):
        for R in range(j,n+1):
            weights.append((L,R,w(L-1)*w(n-R)))
    active = sum(v for _,_,v in weights)
    assert active == fib(2*j-1)*fib(2*(n-j)+1)
    assert total >= active
    assert sum((R-L+1)*v for L,R,v in weights) == total
    for m in range(j):
        observed = sum(v for L,R,v in weights if L==j-m)
        assert observed == w(j-m-1)*fib(2*(n-j)+1)
    for m in range(n-j+1):
        observed = sum(v for L,R,v in weights if R==j+m)
        assert observed == w(n-j-m)*fib(2*j-1)
    return Fraction(active,total)


def run():
    pairs=0
    for n in range(2,101):
        for j in set((1,2, n//2, (n+1)//2, n-1, n)):
            if 1 <= j <= n:
                exact_case(n,j)
                pairs+=1
    # Check a two-sided bulk approximation and the mass function.
    phi = (1+sqrt(5))/2
    q=phi**-2
    n=200
    j=n//2
    for ell in range(5):
        for r in range(5):
            exact = float(Fraction(w(j-ell-1)*w(n-j-r),fib(2*n)))
            limit = q**(ell+r+1)/sqrt(5)
            assert abs(exact-limit)<1e-13, (ell,r,exact,limit)
    positive=float(exact_case(n,j))
    assert abs(positive-1/sqrt(5))<1e-13
    assert abs(q/(1-q)**2-1)<1e-14
    assert abs((1/sqrt(5))*(1+q)/(1-q)-1)<1e-14
    print('PASS: %d exact n,j finite identities, determinant recurrence, factorization and mean.' % pairs)
    print('PASS: 25 bulk local probabilities and normalization/moment limits at n=200.')


if __name__ == '__main__': run()
