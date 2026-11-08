"""Exact finite checks for fixed-point / consecutive-pattern dependence.

Run with Python 3, standard library only. The combinatorial proofs in RESULT.md
establish the assertions for all allowed parameters; finite checks are independent
small-instance corroboration.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def fall(n, k):
    out = 1
    for a in range(k):
        out *= n-a
    return out


def rank_pattern(window):
    return tuple(1 + sum(x < y for x in window) for y in window)


def local_prob(n, m, sigma, j, i):
    """Conditional pattern probability given a fixed point at i; 1-indexed."""
    if not (j <= i < j+m):
        return Fraction(1, factorial(m))
    k = sigma[i-j]
    return Fraction(choose(i-1, k-1)*choose(n-i, m-k), fall(n-1, m-1))


def boundary_penalty(n, m, r, k):
    return (sum(choose(i-1,k-1)*choose(n-i,m-k) for i in range(1,r))
          + sum(choose(i-1,k-1)*choose(n-i,m-k) for i in range(n-m+r+1,n+1)))


def boundary_cov(n, sigma):
    m = len(sigma)
    b = sum(boundary_penalty(n,m,r,k) for r,k in enumerate(sigma, 1))
    return Fraction(m-1, n*factorial(m-1)) - Fraction(b, n*fall(n-1,m-1))


def test_all():
    checks = 0
    # Independent sample-space enumeration of aggregate covariances, both linear and cyclic.
    for n in range(2, 8):
        seq = list(permutations(range(1,n+1)))
        N = factorial(n)
        for m in range(2, min(n,4)+1):
            vals = defaultdict(lambda: [0,0,0,0])
            for p in seq:
                F = sum(p[i] == i+1 for i in range(n))
                for j in range(n-m+1):
                    pattern = rank_pattern(p[j:j+m])
                    vals[pattern][0] += 1
                    vals[pattern][1] += F
                for j in range(n):
                    pattern = rank_pattern(tuple(p[(j+h)%n] for h in range(m)))
                    vals[pattern][2] += 1
                    vals[pattern][3] += F
            for sigma in permutations(range(1,m+1)):
                A,B,C,D = vals[sigma]
                assert Fraction(B-A,N) == boundary_cov(n,sigma), (n,m,sigma,'linear')
                assert D == C, (n,m,sigma,'cyclic')
                assert boundary_cov(n,sigma) <= Fraction(m-1,n*factorial(m-1))
                assert (boundary_cov(n,sigma) == Fraction(m-1,n*factorial(m-1))) == (sigma == tuple(range(1,m+1)))
                checks += 4
    # Independent indicator-level checks for every fixed-point / window pair.
    for n in range(2, 7):
        seq=list(permutations(range(1,n+1)))
        for m in range(2,min(n,4)+1):
            for j in range(1,n-m+2):
                for i in range(1,n+1):
                    observed=defaultdict(int)
                    for p in seq:
                        if p[i-1] == i:
                            observed[rank_pattern(p[j-1:j-1+m])] += 1
                    for sigma in permutations(range(1,m+1)):
                        assert Fraction(observed[sigma],factorial(n-1)) == local_prob(n,m,sigma,j,i), (n,m,j,i,sigma)
                        checks += 1
    # Vandermonde and strict-boundary equalities on a wider parameter grid.
    for n in range(2,25):
        for m in range(2,min(n,8)+1):
            for r in range(1,m+1):
                for k in range(1,m+1):
                    full = sum(choose(i-1,k-1)*choose(n-i,m-k) for i in range(1,n+1))
                    inner = sum(choose(i-1,k-1)*choose(n-i,m-k) for i in range(r,n-m+r+1))
                    assert full == choose(n,m)
                    assert full-inner == boundary_penalty(n,m,r,k)
                    assert (boundary_penalty(n,m,r,k) == 0) == (r==k)
                    checks += 3
    # Closed six-pattern table and finite-order minimizing-pattern switch.
    for n in range(3,25):
        formulas = {(1,2,3):Fraction(1,n),
                    (1,3,2):Fraction(n-3,2*n*(n-1)),
                    (2,1,3):Fraction(n-3,2*n*(n-1)),
                    (2,3,1):-Fraction(1,2*n),
                    (3,1,2):-Fraction(1,2*n),
                    (3,2,1):-Fraction(n-3,n*(n-1))}
        for sigma,v in formulas.items():
            assert boundary_cov(n,sigma)==v
            checks+=1
        worst=min(formulas.values())
        minimizers={sigma for sigma,v in formulas.items() if v==worst}
        expected = ({(2,3,1),(3,1,2)} if n<=4 else
                    {(2,3,1),(3,1,2),(3,2,1)} if n==5 else {(3,2,1)})
        assert minimizers == expected,(n,minimizers)
        checks+=1
    print(f'PASS: {checks} exact assertions; enumeration n=2..7, all length-2..4 patterns, both windows and fixed locations')

if __name__=='__main__':
    test_all()
