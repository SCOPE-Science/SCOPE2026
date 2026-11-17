#!/usr/bin/env python3
"""Exact finite local-rank verification for path 2-graph polytope geometry.

No random seeds, numerical approximations, or external packages. All possible
relative orders on at most nine sites are enumerated and averaged exactly.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial

WINDOWS = ((-1, 0), (0, 1), (-2, -1, 0), (-1, 0, 1), (0, 1, 2))
C = (F(56,15), -F(173,90), -F(3,20), F(11,60), F(1,45))
D = (F(2114,225), -F(187,75), -F(8173,6300), F(2147,6300), F(421,3150))

def local_count(ranks, center):
    return sum(all(ranks[center] > ranks[center + j] for j in w if j)
               for w in WINDOWS)

def test_local_moments():
    for lag in range(5):
        m = 5 + lag
        s1 = s2 = s12 = ss12 = 0
        for ranks in permutations(range(m)):
            u = local_count(ranks, 2)
            v = local_count(ranks, 2 + lag)
            a = (u - 2)**2
            b = (v - 2)**2
            s1 += u
            s2 += v
            s12 += u*v
            ss12 += a*b
        count = factorial(m)
        assert F(s1,count) == F(2) and F(s2,count) == F(2)
        cov = F(s12,count) - F(4)
        quad_cov = F(ss12,count) - F(56,15)**2
        assert cov == C[lag], (lag,cov,C[lag])
        assert quad_cov == D[lag], (lag,quad_cov,D[lag])
        print('lag',lag,'permutations',count,'cov',str(cov),'quadratic_cov',str(quad_cov))

def global_vertex(order):
    n = len(order)
    result = [0]*n
    for width in (2,3):
        for lo in range(n-width+1):
            winner = max(range(lo,lo+width), key=lambda i: order[i])
            result[winner] += 1
    return tuple(result)

def test_global():
    for n in range(5,9):
        center = tuple(F(5,6) if i in (0,n-1)
                       else F(5,3) if i in (1,n-2) else F(2)
                       for i in range(n))
        assert sum(center) == 2*n - 3
        sumv = [0]*n
        sumvv = [0]*n
        for order in permutations(range(n)):
            v = global_vertex(order)
            assert sum(v)== 2*n-3
            for i in range(n):
                sumv[i]+=v[i]
                sumvv[i]+=v[i]*v[i]
        cnt = factorial(n)
        assert all(F(sumv[i],cnt) == center[i] for i in range(n))
        total_var = sum(F(sumvv[i],cnt)-center[i]**2 for i in range(n))
        target = F(56,15)*n-F(739,90)
        assert total_var == target, (n,total_var,target)
        print('n',n,'exposed_permutations',cnt,'exact_inertia',str(total_var))

if __name__=='__main__':
    test_local_moments()
    assert C[0]+2*sum(C[1:]) == 0
    assert D[0]+2*sum(D[1:]) == F(4352,1575)
    test_global()
    print('PATH2_GAUSSIAN_EXPOSURE_PASS local_rank_orders=409080 global_rank_orders=46200 sigma2=4352/1575')
