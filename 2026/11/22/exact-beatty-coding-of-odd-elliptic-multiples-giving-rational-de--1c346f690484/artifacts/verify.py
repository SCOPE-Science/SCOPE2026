"""Exact rational elliptic addition versus numerical Abel-coordinate coding.
Uses only the Python standard library; this verifies samples, not the theorem.
"""
from fractions import Fraction
from math import asin, floor, pi, sin, sqrt

def add(P,Q,A,B):
    if P is None: return Q
    if Q is None: return P
    x,y=P; z,v=Q
    if x==z and y==-v: return None
    if P==Q:
        if y==0: return None
        m=(3*x*x+2*A*x+B)/(2*y)
    else:
        m=(v-y)/(z-x)
    xx=m*m-A-x-z
    return xx,m*(x-xx)-y

def simpson(f,right,N=8192):
    h=right/N
    s=f(0)+f(right)
    for j in range(1,N):
        s+=(4 if j%2 else 2)*f(j*h)
    return h*s/3

def beta(a,b):
    u=a/b; length=(u+1)**2-u
    f=lambda z:1/sqrt(u+length*sin(z)**2)
    return simpson(f,asin(1/sqrt(length)))/simpson(f,pi/2)

tests=0
for a,b in [(2,1),(3,1),(3,2),(5,2),(11,10),(7,1),(4,3),(17,13)]:
    s=a+b; A=a*a*b*b+a*b*s*s; B=(a*b)**3*s*s
    P=(Fraction(-a*b*b*s),Fraction(a*a*b**3*s))
    assert P[1]**2 == P[0]**3 + A*P[0]**2 + B*P[0]
    step=add(P,P,A,B)
    Q=P; frequency=beta(a,b)
    assert 0 < frequency < 1
    for k in range(17):
        assert Q is not None
        w=Q[0]/Fraction(a*b)
        good=int(-b*s<w<-a*b)
        nearest_floor=(k+1)*frequency
        assert abs(nearest_floor-round(nearest_floor))>1e-7
        expected=floor((k+1)*frequency)-floor(k*frequency)
        assert good==expected,(a,b,k,float(w),good,expected)
        if Q[1]**2 != Q[0]**3 + A*Q[0]**2+B*Q[0]:
            raise AssertionError('point leaves elliptic curve')
        Q=add(Q,step,A,B)
        tests+=1
print('DELTA_BEATTY_RATIONAL_SAMPLE_OK',tests,'8 ratios')
