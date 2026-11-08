"""Exact rational verification of isolated-vertex variance in site percolation.

Run with Python 3.9 or later; standard library only.
"""
from fractions import Fraction as Q
from itertools import combinations

CHECKS = 0

def check(condition):
    global CHECKS
    assert condition
    CHECKS += 1


def graph(a, b):
    assert a >= 0 and b >= 0 and a + b >= 1
    n = a+b+2
    E = {(0, 1)}
    E.update((0, i) for i in range(2, 2+a))
    E.update((1, i) for i in range(2+a, n))
    return n, E


def direct_variance(n, E):
    # Exhaustive independent vertex retention with probability exactly 1/2.
    q = Q(1, 2**n)
    s = Q(0); ss = Q(0)
    for mask in range(1 << n):
        x = [(mask >> v) & 1 for v in range(n)]
        neighbors = [set() for _ in range(n)]
        for u, v in E:
            neighbors[u].add(v); neighbors[v].add(u)
        z = sum(x[v] and all(not x[u] for u in neighbors[v]) for v in range(n))
        s += q*z; ss += q*z*z
    return ss - s*s


def pair_variance(n, E):
    neighbors = [set() for _ in range(n)]
    for u, v in E:
        neighbors[u].add(v); neighbors[v].add(u)
    r = [Q(1, 2**(len(neighbors[v])+1)) for v in range(n)]
    s = sum((t*(1-t) for t in r), Q(0))
    for u in range(n):
        for v in range(u+1, n):
            if v in neighbors[u]:
                s -= 2*r[u]*r[v]
            elif neighbors[u].intersection(neighbors[v]):
                s += 2*r[u]*r[v]
    return s


def closed_variance(a,b):
    A=Q(1,2**(a+2)); B=Q(1,2**(b+2))
    return (Q(a*a+b*b+2*a+2*b,16)
        +(1+Q(b-a,2))*A+(1+Q(a-b,2))*B-(A+B)**2)


def transfer_gap(a,b):
    assert 1<=a<=b
    d=b-a;A=Q(1,2**(a+2));B=Q(1,2**(b+2))
    return (Q(d+1,8)+(3+Q(d,2))*A+(Q(d,4)-1)*B
        -3*A*A+Q(3,4)*B*B)

# Independent enumeration and covariance calculations: all diameter-at-most-three trees through n=12.
for n in range(4,13):
    for a in range(0,n-1):
        b=n-2-a
        N,E=graph(a,b)
        check(direct_variance(N,E)==pair_variance(N,E))
        check(closed_variance(a,b)==pair_variance(N,E))
        check(closed_variance(a,b)==closed_variance(b,a))
# Exact transfer comparison and the quantitative lower bound on a wide finite grid.
for a in range(1,41):
    for b in range(a,81):
        diff=closed_variance(a-1,b+1)-closed_variance(a,b)
        check(diff==transfer_gap(a,b))
        check(diff>Q(b-a+1,8))
# Verify explicit extremizers for all n up to 120.
for n in range(4,121):
    values=[(closed_variance(a,n-2-a),a) for a in range(0,n-1)]
    vmin=min(t[0] for t in values); vmax=max(t[0] for t in values)
    check(all(a in {(n-2)//2,(n-1)//2} for v,a in values if v==vmin))
    check(all(a in {0,n-2} for v,a in values if v==vmax))
print('VERIFY_OK',CHECKS)
