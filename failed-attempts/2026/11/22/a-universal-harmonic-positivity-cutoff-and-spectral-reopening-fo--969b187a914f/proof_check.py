"""Exact checks for harmonic modulation of positive Poisson mixtures.

Run: python circle_mixture_checker.py
No external packages required.
"""
from fractions import Fraction as Q
from itertools import combinations

checks = 0

def verify(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1


def coeff(rs,ws,n):
    return sum((w*r**abs(n) for r,w in zip(rs,ws)),Q(0))


def check(rs,ws,k,maxn=75):
    A=lambda n:coeff(rs,ws,n)
    denom=A(0)+A(2*k)
    c=A(k)/denom
    verify(0 < c < Q(1,2),'critical coefficient range')
    last=None
    for n in range(maxn+1):
        B=A(n)-c*(A(abs(n-k))+A(n+k))
        R=(A(abs(n-k))+A(n+k))/A(n)
        Rk=denom/A(k)
        verify(R<=Rk,'global ratio maximum')
        if n==k:
            verify(B==0,'critical notch')
        elif n<k or len(set(rs))>1:
            verify(B>0,'other modes positive')
        else:
            verify(B==0,'pure Poisson high tail collapse')
        if n>=k and last is not None:
            verify(R<=last,'high ratio monotonicity')
        if n>=k: last=R
        if len(rs)==2 and n>k:
            r,s=rs
            u,v=ws
            formula=u*v*(s**k-r**k)*(1-(r*s)**k)*(s**(n-k)-r**(n-k))/denom
            verify(B==formula,'two-rate spectral reopening identity')
    verify(A(k)+(-2*c)*denom/2==0,'sharp negative boundary')
    verify(A(k)+(-2*c-Q(1,10000))*denom/2<0,'boundary violation')
    return c

rs=[Q(1,3),Q(2,3)]
ws=[Q(1,2),Q(1,2)]
verify(check(rs,ws,1)==Q(9,23),'explicit example exact critical parameter')
for k in range(1,9):
    for r in [Q(1,4),Q(1,3),Q(1,2),Q(3,4)]:
        check([r],[Q(1)],k)
for k in range(1,9):
    for r,s in combinations([Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(4,5)],2):
        for u in [Q(1,5),Q(1,2),Q(4,5)]:
            check([r,s],[u,1-u],k)
for k in range(1,7):
    check([Q(1,6),Q(2,5),Q(3,4)], [Q(1,5),Q(3,10),Q(1,2)],k)
# A positive log-convex coefficient sequence need not have the critical facet at k.
r,s=Q(1,3),Q(2,3)
a=lambda n: r**n if n<=4 else r**4*s**(n-4)
verify(all(a(n+1)*a(n-1)>=a(n)**2 for n in range(1,15)),'log convex boundary example')
R1=(a(0)+a(2))/a(1)
R4=(a(3)+a(5))/a(4)
verify(R1==Q(10,3) and R4==Q(11,3),'counterexample ratios')
verify(a(4)-Q(3,10)*(a(3)+a(5))<0,'counterexample n4 negative')
print('PASS:', checks,'exact rational assertions')
