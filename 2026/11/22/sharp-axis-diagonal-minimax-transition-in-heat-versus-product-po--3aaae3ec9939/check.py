"""Self-contained finite checks of sharp heat versus product-Poisson calibration.
No assertion in this script replaces the analytic proof.
"""
import math
from itertools import product

def roots(a):
    def h(u):
        return math.log(2*u/a)+a*u-u*u
    lo, hi = 1e-14, a
    assert h(lo)<0<h(hi)
    for _ in range(90):
        mid=(lo+hi)/2
        if h(mid)<0: lo=mid
        else: hi=mid
    um=(lo+hi)/2
    lo, hi = a, max(2*a+3, 8.0)
    while h(hi)>0: hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if h(mid)>0: lo=mid
        else: hi=mid
    up=(lo+hi)/2
    return um,up

def wings(a):
    m,p=roots(a)
    return math.exp(-m*m)-math.exp(-a*m), math.exp(-a*p)-math.exp(-p*p)

def calibration(d):
    def gap(c):
        return wings(c*math.sqrt(d))[0]-wings(c)[1]
    lo,hi=.001,8.
    assert gap(lo)<0<gap(hi)
    for _ in range(90):
        m=(lo+hi)/2
        if gap(m)<0: lo=m
        else: hi=m
    c=(lo+hi)/2
    A=wings(c*math.sqrt(d))[0]
    B=wings(c)[1]
    assert abs(A-B)<1e-13
    return c,A

cs=[]
for d in (1,2,3,4,8,16):
    c,E=calibration(d)
    cs.append((d,c,E))
    assert 0<E<1
    um=roots(c*math.sqrt(d))[0]
    up=roots(c)[1]
    assert abs((math.exp(-um*um)-math.exp(-c*math.sqrt(d)*um))-E)<1e-12
    assert abs((math.exp(-c*up)-math.exp(-up*up))-E)<1e-12
for (_,c1,e1),(_,c2,e2) in zip(cs,cs[1:]):
    assert c2<c1 and e2>e1

# Finite Fourier-grid checks (not a proof of any infinite claim).
for d,t,N in [(2,.004,80),(2,.001,140),(3,.008,24)]:
    c,E=calibration(d)
    for mult in (.93,1,1.07):
        cc=c*mult
        observed=0.
        for k in product(range(N+1),repeat=d):
            s2=sum(a*a for a in k)
            s1=sum(k)
            observed=max(observed,abs(math.exp(-t*s2)-math.exp(-cc*math.sqrt(t)*s1)))
        theory=max(wings(cc*math.sqrt(d))[0], wings(cc)[1])
        assert 0<=theory-observed<.025, (d,t,cc,theory,observed)
    print('grid dimension',d,'t',t,'calibration',c,'limit',E)
print('passed: analytic critical-equation residuals, monotone dimension trends, and 9 finite grid comparisons')
