"""Exact rational checks for the adjacent-degree Bernstein Lipschitz theorem.

Only finite instances are checked; the all-degree assertion rests on the proof.
Run: python verify_bernstein.py
"""
from fractions import Fraction as Q
from math import comb


def vertices(n):
    return sorted(set(Q(j,n) for j in range(n+1)) | set(Q(k,n+1) for k in range(n+2)))


def spline(n):
    pts=vertices(n)
    values={Q(0):Q(0)}
    for a,b in zip(pts,pts[1:]):
        # Consecutive interlacing nodes; slope + from old node to new node, - back.
        # Detect which grid the interval begins at, treating endpoints canonically.
        slope=1 if a*n == int(a*n) else -1
        values[b]=values[a]+slope*(b-a)
    return pts,values


def bernstein(n,p,vals):
    return sum((Q(comb(n,k))*p**k*(1-p)**(n-k)*vals[Q(k,n)] for k in range(n+1)),Q(0))


def w1(n,p):
    pts=vertices(n)
    # W1 = integral of the difference of CDFs.
    cdfn=Q(0); cdfnext=Q(0); total=Q(0)
    for a,b in zip(pts,pts[1:]):
        if a*n == int(a*n):
            k=int(a*n)
            cdfn+=Q(comb(n,k))*p**k*(1-p)**(n-k)
        if a*(n+1)==int(a*(n+1)):
            k=int(a*(n+1))
            cdfnext+=Q(comb(n+1,k))*p**k*(1-p)**(n+1-k)
        total+=abs(cdfn-cdfnext)*(b-a)
    return total

count=0
for n in range(1,24):
    pts,v=spline(n)
    assert pts[0]==0 and pts[-1]==1
    for a,b in zip(pts,pts[1:]):
        assert abs(v[b]-v[a])==b-a
    for j in range(n+1):
        assert v[Q(j,n)]==Q(j*(n-j),n*(n+1))
    for j in range(n):
        assert v[Q(j+1,n+1)]==Q((j+1)*(n-j),n*(n+1))
    for num,den in ((0,1),(1,1),(1,2),(1,3),(2,3),(1,5),(4,5),(3,7)):
        p=Q(num,den)
        target=Q(2)*p*(1-p)/Q(n+1)
        assert bernstein(n+1,p,v)-bernstein(n,p,v)==target,(n,p)
        assert w1(n,p)==target,(n,p,'W1')
        count+=1
print('INTERLACED_SPLINE_SLOPES_AND_KNOT_VALUES_PASS_N1_TO23')
print('EXACT_ADJACENT_BERNSTEIN_DIFFERENCES_PASS',count)
print('INDEPENDENT_EXACT_CDF_WASSERSTEIN_CHECKS_PASS',count)
print('ALL_BERNSTEIN_INCREMENT_CHECKS_PASS')
