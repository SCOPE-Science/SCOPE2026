"""Exact-rational checks of the two-state high-value occupancy envelope.

All arithmetic in this checker is rational. Finite checks independently
supplement the analytic argument in RESULT.md; they are not its proof.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement

def h(p):
    p = Q(p)
    return p*p / (1-p+p*p)

def lower(g, mean):
    mean = Q(mean)
    a = g//2
    if mean <= Q(a,g):
        j = min(a-1, int(g*mean))
        lo,hi = Q(j,g),Q(j+1,g)
        frac = (mean-lo)*g
        return (1-frac)*h(lo)+frac*h(hi)
    u=Q(a,g)
    return 1-(1-mean)/(1-u+u*u)

def main():
    total=0
    for g in range(2,81):
        a=g//2
        points=[Q(k,g) for k in range(g+1)]
        vals=[h(p) for p in points]
        # Strict below of every lattice H, and correct upper bound.
        for p,v in zip(points, vals):
            assert lower(g,p)<=v<=p,(g,p,lower(g,p),v)
            total+=1
        # Convex slopes of the proposed piecewise envelope.
        slopes=[g*(vals[k+1]-vals[k]) for k in range(a)]
        slopes.append((1-vals[a])/(1-points[a]))
        assert all(slopes[i]<=slopes[i+1] for i in range(len(slopes)-1)),(g,slopes)
        if g%2:
            assert vals[a+1]==1-(1-points[a+1])/(1-points[a]+points[a]*points[a])
        # Stationary identity for every cooperator count, including endpoints.
        for p in points:
            q=h(p)
            assert q==q*p+(1-q)*p*p
    print('exact shape/stationarity tests:',total,'lattice points, g=2..80: PASS')
    num=0
    for g in range(2,9):
        for groups in range(1,6):
            for ks in combinations_with_replacement(range(g+1),groups):
                m=Q(sum(ks),groups*g)
                y=sum((h(Q(k,g)) for k in ks),Q(0))/groups
                assert lower(g,m)<=y<=m,(g,groups,ks,lower(g,m),y,m)
                num+=1
    print('exact exhaustive multi-group profiles:',num,': PASS')
    assert (h(Q(1,4)),h(Q(3,4)),lower(4,Q(3,4)))==(Q(1,13),Q(9,13),Q(2,3))
    low=(2*h(Q(1,2))+2*h(Q(1,1)))/4
    high=(3*h(Q(1,1))+h(Q(0,1)))/4
    uni=h(Q(3,4))
    assert (low,uni,high)==(Q(2,3),Q(9,13),Q(3,4))
    print('four-person group witnesses:',low,uni,high,': PASS')

if __name__=='__main__': main()
