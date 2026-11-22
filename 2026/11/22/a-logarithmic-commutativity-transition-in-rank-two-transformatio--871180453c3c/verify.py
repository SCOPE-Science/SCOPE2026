#!/usr/bin/env python3
"""Independent exact checks for rank-two transformation-sandwich commutation."""
from itertools import product
from math import exp, log


def formula(n, k):
    assert n >= 2 and 1 <= k < n
    h = n - k
    return (
        n * (n*n)**(n-2)
        + n*(n-1) * (k*k+h*h)**(n-2)
        + 2*k*h * (2*k*h)**(n-2)
        + 2*(n-1) * (k*(n*k)**(n-2) + h*(n*h)**(n-2))
        + k*(k-1)*(k-2) * (k*k)**(n-2)
        + h*(h-1)*(h-2) * (h*h)**(n-2)
    )


def partitions(r):
    if r == 0:
        yield ()
    else:
        for p in partitions(r-1):
            for label in range(max(p)+2 if p else 1):
                yield p+(label,)


def fall(n, r):
    z=1
    for i in range(r):
        z*=n-i
    return z


def boundary_sum(n, k):
    h=n-k
    weights=(k,h)
    total=0
    cases=0
    for p in partitions(4):
        for cls in product((0, 1), repeat=max(p)+1):
            if any(p[cls[p[2+i]]] != p[2+cls[p[i]]] for i in range(2)):
                continue
            count = fall(k, sum(t==0 for t in cls))*fall(h, sum(t==1 for t in cls))
            K=sum(weights[i]*weights[j] for i in range(2) for j in range(2) if p[j]==p[2+i])
            total += count * K**(n-2)
            cases += 1
    assert cases == 18
    return total


def direct(n, k, placement=None):
    # The canonical sandwich is an idempotent with image {0,1},
    # with 0 in the first fiber and 1 in the second.
    first=set([0]+list(range(n-(k-1),n))) if placement is None else set(placement)
    assert len(first)==k and 0 in first and 1 not in first
    a=tuple(0 if i in first else 1 for i in range(n))
    maps=list(product(range(n), repeat=n))
    ans=0
    for x in maps:
        for y in maps:
            ans += all(x[a[y[t]]] == y[a[x[t]]] for t in range(n))
    return ans


def main():
    direct_cases=0
    for n in range(2, 5):
        for k in range(1, n):
            f=formula(n,k)
            b=boundary_sum(n,k)
            d=direct(n,k)
            assert f==b==d,(n,k,f,b,d)
            print(f"direct n={n} k={k}: {d} PASS")
            direct_cases += 1
    # Same fiber sizes but different placements of non-image points.
    assert direct(4,2,{0,2}) == direct(4,2,{0,3}) == formula(4,2)
    print('placement invariance n=4 k=2: PASS')
    symbolic_cases=0
    for n in range(2,13):
        for k in range(1,n):
            assert formula(n,k)==boundary_sum(n,k)
            symbolic_cases += 1
    print(f'18-case boundary partition formula: {symbolic_cases} profiles PASS')
    # Finite illustrations are NOT a proof of the asymptotic theorem.
    for n in (100,1000,10000):
        k=round(log(n))
        # Direct exact integer formula followed by floating-point normalization.
        ratio = formula(n,k)/n**(2*n-3)
        prediction=(1+exp(-(k-log(n))))**2
        print(f'window n={n} k={k}: n^3 P={ratio:.6f}; limit-profile={prediction:.6f}')
    print('ALL CHECKS PASS')

if __name__=='__main__':
    main()
