"""Exact finite verification of the common-diagonal moment identities.

Run: python check.py
Standard library only. The analytic limit is established in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb, ceil, floor, sqrt, pi, exp, lgamma, log

checks = 0

def verify(statement):
    global checks
    if not statement:
        raise AssertionError(f"exact check {checks + 1} failed")
    checks += 1

@lru_cache(None)
def cat(m):
    assert m >= 0
    return comb(2*m, m) // (m + 1)

@lru_cache(None)
def triangulations(i, j):
    if j - i < 2:
        return (frozenset(),)
    out = []
    for k in range(i + 1, j):
        for left in triangulations(i, k):
            for right in triangulations(k, j):
                edges = set(left | right)
                if k - i > 1:
                    edges.add((i, k))
                if j - k > 1:
                    edges.add((k, j))
                out.append(frozenset(edges))
    return tuple(out)

def depth(edge, n):
    i, j = edge
    return min(j-i, n-(j-i))-1

def closed_moments(n, lo, hi):
    assert 1 <= lo <= hi and 2*hi+2 < n
    den = cat(n-2)**2
    mean = sum((Fraction(n * cat(r)**2 * cat(n-r-2)**2, den)
                for r in range(lo, hi+1)), Fraction(0))
    disjoint = sum((Fraction(n*(n-r-s-1) * cat(r)**2 * cat(s)**2
                             * cat(n-r-s-2)**2, den)
                    for r in range(lo, hi+1) for s in range(lo, hi+1)), Fraction(0))
    nested = sum((Fraction(2*n*(r-s+1)*cat(s)**2*cat(r-s)**2
                           * cat(n-r-2)**2, den)
                  for r in range(lo, hi+1) for s in range(lo, r)), Fraction(0))
    return mean, disjoint, nested

def brute_moments(n, lo, hi):
    trees = triangulations(0,n-1)
    verify(len(trees) == cat(n-2))
    verify(all(len(T) == n-3 for T in trees))
    counts = Counter()
    for A in trees:
        for B in trees:
            k = sum(lo <= depth(e,n) <= hi for e in A & B)
            counts[k] += 1
    total = len(trees)**2
    return (Fraction(sum(k*v for k,v in counts.items()), total),
            Fraction(sum(k*(k-1)*v for k,v in counts.items()), total),
            counts)

for n in range(5,10):
    for lo in range(1, (n-3)//2+1):
        for hi in range(lo, (n-3)//2+1):
            if not 2*hi+2 < n:
                continue
            m, factorial2, distribution = brute_moments(n,lo,hi)
            e,d,z = closed_moments(n,lo,hi)
            verify(m == e)
            verify(factorial2 == d+z)
            verify(sum(distribution.values()) == cat(n-2)**2)

# Nonconstant signed weights independently test the full covariance identity.
def finite_weighted(n, f, g):
    hi=(n-3)//2
    assert 2*hi+2<n
    R=range(1,hi+1)
    den=cat(n-2)**2
    one=lambda w:sum((Fraction(n*w(r)*cat(r)**2*cat(n-r-2)**2,den)
                       for r in R),Fraction(0))
    diagonal=sum((Fraction(n*f(r)*g(r)*cat(r)**2*cat(n-r-2)**2,den)
                  for r in R),Fraction(0))
    disjoint=sum((Fraction(n*(n-r-s-1)*f(r)*g(s)*cat(r)**2*cat(s)**2
                           *cat(n-r-s-2)**2,den)
                  for r in R for s in R),Fraction(0))
    nested=sum((Fraction(n*(r-s+1)*(f(r)*g(s)+f(s)*g(r))
                         *cat(s)**2*cat(r-s)**2*cat(n-r-2)**2,den)
                for r in R for s in R if s<r),Fraction(0))
    trees=triangulations(0,n-1)
    total=len(trees)**2
    cov_sum=0
    for A in trees:
        for B in trees:
            E={e for e in (A&B) if depth(e,n) in R}
            cov_sum+=sum(f(depth(e,n)) for e in E)*sum(g(depth(e,n)) for e in E)
    verify(Fraction(cov_sum,total)==diagonal+disjoint+nested)
    verify(one(f)==Fraction(sum(sum(f(depth(e,n)) for e in (A&B) if depth(e,n) in R)
                       for A in trees for B in trees),total))

for n in (7,8,9):
    finite_weighted(n,lambda r:r,lambda r:r*r+1)
    finite_weighted(n,lambda r:(-1)**r*r,lambda r:r*r-2*r)

# Exact pair events in small cells: the conditional probability of both
# independent triangulations retaining an immediately nested diagonal.
for r in range(2,25):
    q = Fraction(cat(r-1),cat(r))
    verify(Fraction(2*cat(r-1)**2,cat(r)**2) == 2*q*q)

# Check the convergent identity used to derive the universal constant.
partial = sum((d+1)*(cat(d)/(4.0**d))**2 for d in range(0,250))
verify(0 < 4/pi-partial < 2/(pi*249))

@lru_cache(None)
def logcat(k):
    return lgamma(2*k+1)-2*lgamma(k+1)-log(k+1)

def numeric_moments(n,a,b):
    interval=range(ceil(a*sqrt(n)),floor(b*sqrt(n))+1)
    z=logcat(n-2)
    q=lambda r: logcat(r)+logcat(n-r-2)-z
    m=sum(n*exp(2*q(r)) for r in interval)
    dis=sum(n*(n-r-s-1)*exp(2*(logcat(r)+logcat(s)+logcat(n-r-s-2)-z))
            for r in interval for s in interval)
    nest=sum(2*n*(r-s+1)*exp(2*(logcat(s)+logcat(r-s)+logcat(n-r-2)-z))
             for r in interval for s in interval if r>s)
    return m, m+dis+nest-m*m

expected_factor=8/pi-1
for n in [2000,10000,40000]:
    m,v=numeric_moments(n,0.7,1.6)
    print(f"n={n}: mean={m:.8f}, variance={v:.8f}, var/mean={v/m:.8f}")
print(f"limiting variance/mean={expected_factor:.10f}")
print(f"{checks} exact assertions passed; analytic asymptotics require the written proof")
