"""Exact-arithmetic checks for two-level uniform-spacing exceedance covariance.
Run: python3 covariance_check.py
No external dependencies.
"""
from fractions import Fraction as F
from itertools import product


def prob_tail(n, thresholds):
    return max(F(0), F(1)-sum(thresholds, F(0))) ** (n-1)


def covariance(n,a,b):
    return n * ((1-b)**(n-1)+(n-1)*prob_tail(n,(a,b)) - n*(1-a)**(n-1)*(1-b)**(n-1))


def clipped(poly,A,B,C):
    if not poly: return []
    out=[]
    def v(p): return A*p[0]+B*p[1]+C
    for P,Q in zip(poly,poly[1:]+poly[:1]):
        u,w=v(P),v(Q)
        if u>=0: out.append(P)
        if (u<0<w) or (u>0>w):
            lam=u/(u-w)
            out.append((P[0]+lam*(Q[0]-P[0]),P[1]+lam*(Q[1]-P[1])))
    return out


def poly_area(poly):
    if not poly:return F(0)
    return abs(sum((p[0]*q[1]-q[0]*p[1] for p,q in zip(poly,poly[1:]+poly[:1])),F(0)))/2


def probability_simplex3(events):
    poly=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
    for idx,t in events:
        if idx==0: halfplane=(F(1),F(0),-t)
        elif idx==1: halfplane=(F(0),F(1),-t)
        else: halfplane=(F(-1),F(-1),F(1)-t)
        poly=clipped(poly,*halfplane)
    return 2*poly_area(poly)


def probability_simplex2(events):
    # X_1=u, X_2=1-u for u uniform on [0,1]
    lo,hi=F(0),F(1)
    for idx,t in events:
        if idx==0: lo=max(lo,t)
        else: hi=min(hi,F(1)-t)
    return max(F(0),hi-lo)


def geometric_cov(n,a,b):
    geom=probability_simplex2 if n==2 else probability_simplex3
    ea=sum((geom([(i,a)]) for i in range(n)),F(0))
    eb=sum((geom([(i,b)]) for i in range(n)),F(0))
    eab=sum((geom([(i,a),(j,b)]) for i in range(n) for j in range(n)),F(0))
    return eab-ea*eb


def sign(x):return (x>0)-(x<0)

checks=0
for n in (2,3):
    for ia in range(1,12):
        for ib in range(ia,16):
            a,b=F(ia,20),F(ib,20)
            if a+b>=1:continue
            assert geometric_cov(n,a,b)==covariance(n,a,b),(n,a,b)
            checks+=1

# The example's integer transition is precisely between 5/6 and 13/14.
a,b=F(3,20),F(1,4)
for n in range(2,121):
    expected=1 if (n<=5 or n>=14) else -1
    assert sign(covariance(n,a,b))==expected,n
    checks+=1
for n in (5,6,13,14):
    factor=F(1)+(n-1)*F(4,5)**(n-1)-n*F(17,20)**(n-1)
    assert covariance(n,a,b)==n*F(3,4)**(n-1)*factor
    print(f'n={n}, normalized sign certificate={factor}, sign={sign(factor)}')
    checks+=1

# Numerical diagnostic only: log-concavity of g sampled away from zero.
from math import log, exp
for ia,ib in product(range(1,8),range(1,10)):
    a,b=F(ia,20),F(ib,20)
    if a>b or a+b>=1:continue
    s=1-float(a); t=(1-float(a+b))/(1-float(b))
    alpha=-log(s); delta=log(s/t)
    for x in (0.1,0.3,1,2,5,10,30,100):
        # In the analytic proof, 1/(2*sinh(y/2)) < 1/y.
        import math
        correction=(alpha/(2*math.sinh(alpha*x/2)))**2
        assert correction < 1/x**2
        checks+=1
print('PASS',checks,'exact assertions or diagnostic inequalities')
