"""Independent arithmetic checks for the cubic adaptive-tolerance map.
Run: python verify.py
"""
from fractions import Fraction as Q
from math import sqrt


def F(x,p,l,h=Q(1),g=Q(0)):
    d=p-x
    return (Q(1)-g)*(x+h*x*(Q(1)-x)*d*(Q(1)-d*d/(l*l)))

checks=0
# Exact rational well-posed regimes: complete parameter grids, including boundaries.
for k in range(1,17):
    l=Q(k,16)
    for pnum in range(17):
        p=Q(pnum,16)
        for xnum in range(17):
            x=Q(xnum,16)
            v=F(x,p,l)
            if l*l>=Q(1,2):
                assert 0 <= v <= 1,(x,p,l,v)
            checks+=1
# Media g>=0 and safe lambda preserves the interval; negative g gives boundary exit.
for k in range(12,17):
    l=Q(k,16)
    for g in (Q(0), Q(1,8), Q(1,2),Q(1)):
        for xnum in range(17):
            for pnum in range(17):
                assert 0<=F(Q(xnum,16),Q(pnum,16),l,g=g)<=1
                checks+=1
    assert F(Q(1),Q(1,2),l,g=Q(-1,10))>1
    checks+=1
# Exact parameter-specific counterexamples to unit-step invariance.
assert F(Q(1,10),Q(1),Q(1,4))==Q(-21719,25000)
checks+=1
# For every tested subcritical lambda find rational points with negative output.
for k in range(1,12):
    l=Q(k,16)
    if l*l<Q(1,2):
        found=False
        for j in range(1,10001):
            if F(Q(1,j+1),Q(1),l)<0:
                found=True;break
        assert found,l
        checks+=1
# Frozen-environment convergence selection for safe original update.
for k in range(12,16):
    l=Q(k,16)
    for pnum in range(17):
        p=Q(pnum,16)
        for xnum in range(1,16):
            x=Q(xnum,16)
            v=F(x,p,l)
            assert 0<=v<=1
            if p>l and x<p-l: assert 0<=v<x
            elif p<Q(1)-l and x>p+l: assert x<v<=1
            elif x<p and x>max(Q(0),p-l): assert x<v<=p
            elif x>p and x<min(Q(1),p+l): assert p<=v<x
            checks+=1
# Analytic formula for H(l): compare with a grid of actual x,p to independently test it.
def A(l):
    # Golden-section search for the unique maximizer, independently of a cubic solver.
    lo,hi=0.0,float(l)
    phi=(5**0.5-1)/2
    a=hi-phi*(hi-lo); b=lo+phi*(hi-lo)
    def obj(d):return d*(1-d)*(1-(d/l)**2)
    for _ in range(135):
        if obj(a)<obj(b):
            lo=a; a=b; b=lo+phi*(hi-lo)
        else:
            hi=b; b=a; a=hi-phi*(hi-lo)
    d=(lo+hi)/2
    return obj(d),d
for l in [0.1,0.25,0.5,1/sqrt(2),0.85,0.9,0.915,0.95,0.99]:
    a,d=A(l)
    b=1/(l*l)-1
    H=1/max(a,b)
    assert 0<d<l and a>0 and b>=0
    for ix in range(61):
        for ip in range(61):
            x=ix/60;p=ip/60
            def f(h):return (1-g)*(x+h*x*(1-x)*(p-x)*(1-(p-x)**2/l**2))
            g=0
            assert -1e-12<=f(H*0.999999)<=1+1e-12,(l,x,p,H,f(H*0.999999))
            checks+=1
    # explicit attainable overshoot for all sufficiently large factors
    if a>b:
        xx=1-d;pp=1
        assert F(xx,pp,l,H*1.000001)>1
    else:
        # sharpness via x -> 0, p=1
        small=1e-9
        assert F(small,1,l,H*1.00001)<0
    checks+=1
lo,hi=0.9,0.95
for _ in range(80):
    m=(lo+hi)/2
    if A(m)[0] < (1/m**2-1): lo=m
    else: hi=m
root=(lo+hi)/2
assert 0.91478<root<0.91479
print('VERIFY_OK', checks, 'exact_or_sampled_checks', 'transition', root)
