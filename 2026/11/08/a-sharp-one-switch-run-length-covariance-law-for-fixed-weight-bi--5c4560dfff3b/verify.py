"""Exact checks for cyclic fixed-weight binary runs; standard-library only."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def falling(a, r):
    product = 1
    for j in range(r):
        product *= a - j
    return product


def formula(n, k, ell):
    """Covariance of total proper one-runs and exactly ell-long one-runs."""
    assert n >= 3 and 1 <= k <= n - 1 and ell >= 1
    if ell > k or n - k == 1:
        return Fraction(0)
    if n == ell + 2:  # necessarily k == ell when the statistic is nonzero
        assert k == ell
        return Fraction(2 * (1 - ell), (ell + 1)**2)
    assert n >= ell + 3 and k >= ell and n - k >= 2
    mean_exact = Fraction(n * falling(k, ell) * falling(n-k, 2), falling(n, ell+2))
    multiplier = Fraction((n-k-1)*((ell+1)*k-(ell-1)*n-2), (n-1)*(n-ell-2))
    return mean_exact * multiplier


def exact_enumeration(n,k):
    """Enumerate cyclic binary words from position sets; no use of formula()."""
    counts = defaultdict(lambda: [0,0,0])
    for subset in combinations(range(n),k):
        x = [False] * n
        for j in subset:
            x[j] = True
        starts = [i for i in range(n) if x[i] and not x[(i-1) % n]]
        r = len(starts)
        lengths = []
        for i in starts:
            j = i
            count = 0
            while x[j]:
                count += 1
                j = (j + 1) % n
            lengths.append(count)
        for ell in range(1,n):
            e = sum(1 for t in lengths if t == ell)
            counts[ell][0] += r
            counts[ell][1] += e
            counts[ell][2] += r*e
    denom=comb(n,k)
    return {ell:Fraction(denom*z - x*y,denom*denom) for ell,(x,y,z) in counts.items()}


def check():
    num = 0
    for n in range(3,15):
        for k in range(1,n):
            measured = exact_enumeration(n,k)
            for ell in range(1,n):
                assert measured[ell] == formula(n,k,ell), (n,k,ell,measured[ell],formula(n,k,ell))
                num += 1
    # Nondegenerate phases including exact zero at interior density.
    for n,k,ell,sgn in [(8,2,2,-1),(8,5,2,1),(13,5,2,0),(10,4,2,0),
                         (9,3,3,-1),(10,6,3,1),(9,7,7,-1),(9,7,6,1)]:
        cov = formula(n,k,ell)
        assert (cov > 0) - (cov < 0) == sgn, (n,k,ell,cov,sgn)
        num += 1
    for n in range(4,150):
        for k in range(2,n-1):
            profile = [formula(n,k,ell) for ell in range(1,k+1)]
            # Strictly positive near singletons; strictly negative at all-ones run.
            assert profile[0] > 0 and profile[-1] < 0, (n,k)
            # Signs nonincreasing, and zero occupies at most one rank.
            signs = [(v>0) - (v<0) for v in profile]
            assert signs == sorted(signs,reverse=True) and signs.count(0)<=1, (n,k,signs)
            num += 2
    print(f'PASS: {num} exact rational assertions; enumeration all n=3..14; all-length phase law n=4..149.')

if __name__ == '__main__':
    check()
