#!/usr/bin/env python3
"""Exact arithmetic checks for weighted-star noise-free leader placement."""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def inverse_trace(a):
    n = len(a)
    if n == 0: return F(0)
    mat = [list(row) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        p = next((i for i in range(j, n) if mat[i][j] != 0), None)
        assert p is not None
        mat[j], mat[p] = mat[p], mat[j]
        z = mat[j][j]
        mat[j] = [v / z for v in mat[j]]
        for i in range(n):
            if i != j:
                z = mat[i][j]
                mat[i] = [mat[i][t] - z * mat[j][t] for t in range(2*n)]
    return sum((mat[i][n+i] for i in range(n)), F(0))


def matrix_cost(w, leaders):
    m = len(w)
    L = [[F(0)] * (m + 1) for _ in range(m + 1)]
    for j, weight in enumerate(w, 1):
        L[0][0] += weight
        L[j][j] += weight
        L[0][j] -= weight
        L[j][0] -= weight
    followers = sorted(set(range(m+1)) - set(leaders))
    return inverse_trace([[L[i][j] for j in followers] for i in followers])


def formula_cost(w, leaders):
    m = len(w)
    if len(leaders) == m + 1: return F(0)
    remaining = sum((F(1)/v for j, v in enumerate(w,1) if j not in leaders), F(0))
    if 0 in leaders: return remaining
    led_w = sum((w[j-1] for j in leaders),F(0))
    return remaining + F(m-len(leaders)+1)/led_w


def theorem(w, k):
    m = len(w)
    assert 1 <= k <= m + 1
    if k == m + 1: return F(0), frozenset(range(m+1)), 'all'
    order = sorted(range(1,m+1), key=lambda j: (w[j-1],j))
    sorted_w = [w[j-1] for j in order]
    hub = frozenset((0,*order[:k-1]))
    leaves = frozenset(order[:k])
    P = sum(sorted_w[:k],F(0))
    threshold = (m-k+1)*sorted_w[k-1]
    choice = leaves if P >= threshold else hub
    return formula_cost(w,choice), choice, 'leaves' if P >= threshold else 'hub'


def main():
    r=Random(20261105)
    matrix_tests = 0
    exhaustive_tests = 0
    threshold_tests = 0
    for m in range(2,10):
        for trial in range(24):
            w=[F(r.randint(1,120),r.randint(1,80)) for i in range(m)]
            if trial % 3 == 0:
                w=[F(r.randint(1,6),r.randint(1,6)) for i in range(m)]
            for k in range(1,m+2):
                sets=[frozenset(s) for s in combinations(range(m+1),k)]
                val, selection, classification = theorem(w,k)
                opt=min(formula_cost(w,s) for s in sets)
                assert val == opt,(w,k,val,opt)
                exhaustive_tests += 1
                if k <= m:
                    sorted_w=sorted(w)
                    p=sum(sorted_w[:k],F(0))
                    c=m-k+1
                    assert (classification=='leaves') == (p >= c*sorted_w[k-1])
                    threshold_tests += 1
                checks = [sets[0],sets[len(sets)//2],sets[-1],selection]
                for leaders in checks:
                    assert matrix_cost(w, leaders) == formula_cost(w,leaders)
                    matrix_tests += 1
    w=[F(1)]*5 + [F(100)]*3
    exact=[]
    for k in (5,6,7):
        opt, leaders, classification = theorem(w,k)
        expected=('leaves','hub','leaves')[(5,6,7).index(k)]
        assert classification == expected
        exact.append(f'{k}:{classification}:{opt}')
    print('VERIFY_OK')
    print('exact exhausted all leader subsets:',exhaustive_tests)
    print('independent rational matrix inversions:',matrix_tests)
    print('budget threshold checks:',threshold_tests)
    print('reentrant eight-leaf example:', ' '.join(exact))

if __name__=='__main__':main()
