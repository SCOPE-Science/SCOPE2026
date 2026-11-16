"""Supplementary finite consistency tests for half-density tent Gabor bounds.

Uses direct finite Zak sums and exact rational endpoint arithmetic where possible;
finite sampling is not a proof of the continuous optimization.
"""
from fractions import Fraction as Q
from math import cos, sin, pi, sqrt, isclose
import cmath

def tent(t):
    return max(0.0,1.0-abs(t-1.0))

def zak(t,phase,L):
    return sum(tent(t+k*L)*cmath.exp(1j*k*phase) for k in range(-4,5))

def predicted(b):
    L=1/b
    a=L/2
    if b<=0.25:
        return 0,None
    if b<=0.5:
        return a*(2-a)**2, 2*a
    d=1-a
    return L*min((1+d)**2/2,4/5),L*(1+4*d*d)

def fast_scalar(x,phase,b):
    L=1/b
    a=L/2
    return L*(abs(zak(x,phase,L))**2+abs(zak(x+a,phase,L))**2)

def exact_low(d):
    d=Q(d)
    return Q(2)*(1-d)*min((1+d)**2/Q(2),Q(4,5))
def exact_up(d):
    d=Q(d)
    return Q(2)*(1-d)*(1+4*d*d)

count=0
for b in (0.27,0.30,0.375,0.49,0.5,0.51,0.6,2/3,0.7,0.75):
    A,B=predicted(b)
    assert A>0 and B>=A
    a=1/(2*b)
    aa=100000
    mm=-100000
    d=1-a
    xs=[a*j/500 for j in range(501)]
    xs.extend(x for x in (0,a,d,2*d,(1+d)/2,d-0.2,d+0.2,a/2) if 0<=x<=a)
    for x in xs:
        for theta in (0,pi/2,pi):
            v=fast_scalar(x,theta,b)
            if v<aa:aa=v
            if v>mm:mm=v
            assert v>A-1e-10,(b,x,theta,v,A)
            assert v<B+1e-10,(b,x,theta,v,B)
            count+=2
    # sample mesh dense enough to see analytic extrema within ~.001
    assert abs(aa-A)<0.00005,(b,aa,A)
    assert abs(mm-B)<0.00005,(b,mm,B)
    count+=2

# Confirm all three optimization benchmarks exactly against rational neighborhoods.
d=Q(1,4)
assert exact_low(d)==Q(75,64)
assert exact_up(d)==Q(15,8)
assert exact_up(d)/exact_low(d)==Q(8,5)
assert exact_up(Q(1,6))==Q(50,27)
for k in range(1,330):
    dd=Q(k,1000)
    assert exact_up(dd)/exact_low(dd)>=Q(8,5)
    assert exact_up(dd)>=Q(50,27)
    count+=2
# For d below sqrt(8/5)-1, lower bound is (1-d)(1+d)^2.
# At the crossover the derivative switches from positive to negative.
dstar=sqrt(8/5)-1
Astar=(8/5)*(1-dstar)
for k in range(0,334):
    dd=k/1000
    if dd>1/3:continue
    Alow=2*(1-dd)*min((1+dd)**2/2,4/5)
    assert Alow<=Astar+1e-12
    count+=1
print('PASS',count,'finite numerical and exact-rational checks', 'Amax',Astar, 'dstar',dstar)
