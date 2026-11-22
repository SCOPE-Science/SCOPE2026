"""Finite diagnostics for the double-star spectral-moment theorem.

Requires NumPy. Run `python verify.py`.
Finite diagnostics supplement, not replace, the analytic all-size proof.
"""
from fractions import Fraction as Q
from itertools import combinations
import math
import numpy as np


def laplacian(p, q, t, dtype=float):
    n = p + q + 2
    a = [[Q(0) for _ in range(n)] for _ in range(n)]
    def edge(i, j, w):
        a[i][i] += w
        a[j][j] += w
        a[i][j] -= w
        a[j][i] -= w
    edge(0, 1, t)
    for i in range(p):
        edge(0, 2 + i, Q(1))
    for j in range(q):
        edge(1, 2 + p + j, Q(1))
    return a if dtype is Q else np.array(a, dtype=float)


def exact_inverse(a):
    n = len(a)
    b = [list(a[i]) + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if b[i][j])
        b[j], b[pivot] = b[pivot], b[j]
        d = b[j][j]
        b[j] = [v / d for v in b[j]]
        for i in range(n):
            if i != j:
                d = b[i][j]
                if d:
                    b[i] = [v - d * w for v, w in zip(b[i], b[j])]
    return [row[n:] for row in b]


def inverse_square_trace(a, pair):
    f = [i for i in range(len(a)) if i not in pair]
    g = [[a[i][j] for j in f] for i in f]
    inv = exact_inverse(g)
    return sum(v * v for row in inv for v in row)


def two_special(m, t):
    s = t + 1.0
    h = 1.0 + m / s
    d = math.sqrt(h * h - 4.0 / s)
    return (h + d) / 2.0, (h - d) / 2.0


def all_orders_formula(p, q, t, r):
    m = min(p, q)
    a, b = two_special(m, t)
    return p + q - 2 + min(2.0, a**r + b**r)


def exact_tests():
    instances = orbits = 0
    for p in range(2, 5):
        for q in range(2, 5):
            for t in [Q(1, 2), Q(1), Q(2), Q(5, 2), Q(7)]:
                a = laplacian(p, q, t, dtype=Q)
                s = t + 1
                m = min(p, q)
                best_formula = min(Q(p+q), Q(p+q-1) + 2*Q(m-1)/s + Q(m*m)/(s*s))
                found = []
                for pair in combinations(range(p+q+2), 2):
                    cost = inverse_square_trace(a, pair)
                    found.append(cost)
                    assert cost >= best_formula, (p,q,t,pair,cost,best_formula)
                    orbits += 1
                assert min(found) == best_formula
                instances += 1
    return instances, orbits


def continuous_tests():
    instances = checked_sets = 0
    for p in range(2, 6):
        for q in range(2, 6):
            for t in [0.15,0.5,1.0,1.4,2.0,3.0,5.0,8.0,20.0,100.0]:
                a = laplacian(p, q, Q(str(t)))
                cache=[]
                for pair in combinations(range(p+q+2),2):
                    f=[i for i in range(p+q+2) if i not in pair]
                    eig=np.linalg.eigvalsh(a[np.ix_(f,f)])
                    assert np.min(eig)>0
                    cache.append(eig)
                for r in [1.0,1.1,1.5,2.0,3.0,6.0,10.0,30.0]:
                    theorem=all_orders_formula(p,q,t,r)
                    actual=min(float(np.sum(eig**(-r))) for eig in cache)
                    assert abs(actual-theorem)<2e-7*max(1.0,actual,theorem), (p,q,t,r,actual,theorem)
                    instances+=1
                checked_sets+=len(cache)
    return instances,checked_sets


def threshold_tests():
    count=0
    for m in range(2, 14):
        def threshold(r):
            lo=0.0; hi=1.0
            def f(t):
                a,b=two_special(m,t)
                return a**r+b**r-2
            while f(hi)>0:hi*=2
            for _ in range(75):
                mid=(lo+hi)/2
                if f(mid)>0:lo=mid
                else:hi=mid
            return (lo+hi)/2
        r=[1.0,1.5,2.0,3.0,4.0,8.0,16.0,64.0]
        v=[threshold(x) for x in r]
        assert all(x<y for x,y in zip(v,v[1:])),(m,v)
        assert abs(v[0]-(m-1))<1e-9
        closed=m-2+math.sqrt((m-1)**2+m*m)
        assert abs(v[2]-closed)<1e-9
        count+=len(r)
    return count


if __name__=='__main__':
    e,o=exact_tests()
    c,s=continuous_tests()
    h=threshold_tests()
    print(f'VERIFY_OK exact_parameter_instances={e} exact_pair_inversions={o} continuous_parameter_order_instances={c} leader_sets={s} threshold_checks={h}')
