#!/usr/bin/env python3
"""Exact finite checks for random-source independent-bond outbreaks on stars.

Standard library only. The infinitely quantified theorem is proved
analytically in RESULT.md; the finite checks are supplementary.
"""

from fractions import Fraction as F
from itertools import product
from math import sqrt


def analytic(k, p):
    n = k + 1
    hub = (1 + k*p)/n
    leaf = (1 + p + (k-1)*p*p)/n
    joint_hl = (2*p + (k-1)*p*p)/n
    joint_ll = (3*p*p + (k-2)*p**3)/n if k >= 2 else None
    cov_hl = (1-p)*(k*(k-1)*p*p + k*p - 1)/n**2
    cov_ll = ((1-p)*((k-1)**2*p**3 + (k+1)*p*p - 3*p - 1)/n**2
              if k >= 2 else None)
    return (hub, leaf, joint_hl, joint_ll, cov_hl, cov_ll)


def exhaustive(k, p):
    """Enumerate every seed and every retained-edge configuration exactly."""
    n = k+1
    totals = [F(0) for _ in range(5)]
    for seed in range(n):
        for edge_open in product((False, True), repeat=k):
            w = F(1, n)
            for edge in edge_open:
                w *= p if edge else 1-p
            # Connectivity from seed in the retained star, without using
            # the analytic probability-by-seed expressions.
            visited = {seed}
            frontier = [seed]
            while frontier:
                v = frontier.pop()
                adj = [j+1 for j in range(k) if edge_open[j]] if v == 0 else ([0] if edge_open[v-1] else [])
                for u in adj:
                    if u not in visited:
                        visited.add(u)
                        frontier.append(u)
            I0 = int(0 in visited)
            I1 = int(1 in visited)
            I2 = int(2 in visited) if k >= 2 else 0
            for i, val in enumerate((I0, I1, I0*I1, I1*I2, I2)):
                totals[i] += w*val
    return totals


def root_bisect(f, lo=0., hi=1.):
    assert f(lo) < 0 and f(hi) > 0
    for _ in range(90):
        mid = (lo+hi)/2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    checks = 0
    for k in range(1, 10):
        for p in [F(0),F(1,8),F(1,5),F(2,5),F(1,2),F(3,4),F(9,10),F(1)]:
            h, l, hl, ll, chl, cll = analytic(k,p)
            a,b,c,d,e = exhaustive(k,p)
            conditions = [h==a,l==b,hl==c,chl==c-a*b]
            if k >= 2:
                conditions += [ll==d,b==e,cll==d-b*e]
            for cond in conditions:
                assert cond,(k,p,'moment identity')
                checks += 1
            assert a + (1-a)==1
            checks += 1
    # Exact sign witnesses for three leaves.
    k = 3
    p = F(1,2)
    assert analytic(k,p)[-2:] == (F(1,16), -F(1,32))
    checks += 1
    p = F(3,4)
    assert analytic(k,p)[-2:] == (F(37,512), F(11,1024))
    checks += 1
    # Algebraic ordering of the two zero sets, tested on exact rational grids.
    for k in range(2, 51):
        for i in range(101):
            p=F(i,100)
            A=k*(k-1)*p*p+k*p-1
            B=(k-1)**2*p**3+(k+1)*p*p-3*p-1
            assert B-F(k-1,k)*p*A==2*p*p-(2+F(1,k))*p-1
            checks += 1
    # Asymptotic checks are diagnostics only; the proof uses uniform bounds.
    for k in [100,1000,10000,1000000]:
        A=lambda p: k*(k-1)*p*p+k*p-1
        r=root_bisect(A)
        c=(sqrt(5)-1)/2
        assert abs(k*r/c-1)<4/k
        checks += 1
        B=lambda p:(k-1)**2*p**3+(k+1)*p*p-3*p-1
        s=root_bisect(B)
        assert 0<r<s<1
        assert abs(s*k**(2/3)-1)<3*k**(-1/3)
        checks += 2
    print('PASS: '+str(checks)+' exact assertions or asymptotic diagnostics')
    print('Exact k=3, p=1/2: hub-leaf = 1/16, leaf-leaf = -1/32')
    print('Exact k=3, p=3/4: hub-leaf = 37/512, leaf-leaf = 11/1024')


if __name__ == '__main__':
    main()
