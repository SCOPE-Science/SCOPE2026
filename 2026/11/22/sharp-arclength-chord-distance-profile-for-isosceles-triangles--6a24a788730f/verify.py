#!/usr/bin/env python3
"""Exact rational sign certificate for the isosceles-triangle boundary mean-distance profile.
No external dependencies. Derivative sign is established on a continuum of t values;
the finite loop checks rational interval enclosures, not sampled values.
"""
from fractions import Fraction as F
import hashlib
S=10**28
N=160

def ceildiv(a,b): return -((-a)//b)

def tail(z,kind):
    # Geometric bound for positive atanh series tail
    if kind=='K': return 2*z**(2*N)/((2*N+1)*(1-z*z))
    return 2*z**(2*N+1)/((2*N+1)*(1-z*z))

H_TAIL=ceildiv(tail(F(15,16),'H').numerator*S,tail(F(15,16),'H').denominator)
K_TAIL=ceildiv(tail(F(7,8),'K').numerator*S,tail(F(7,8),'K').denominator)

def series(z,kind):
    assert 0<=z<1
    p,q=z.numerator,z.denominator
    if kind=='H': lo=(S*p)//q;hi=ceildiv(S*p,q)
    else:lo=hi=S
    lower=upper=0
    for k in range(N):
        d=2*k+1
        lower+=(2*lo)//d
        upper+=ceildiv(2*hi,d)
        lo=(lo*p*p)//(q*q)
        hi=ceildiv(hi*p*p,q*q)
    upper += H_TAIL if kind=='H' else K_TAIL
    return (F(lower,S),F(upper,S))

def mul(U,V):
    z=[a*b for a in U for b in V]
    return min(z),max(z)
def neg(U):return(-U[1],-U[0])
def add(*v):return(sum(q[0] for q in v),sum(q[1] for q in v))
def A(t):return -t*(t+4)*(2*t*t-t-2)
def Q(t):return 2*t**3+9*t*t+3*t-6

def bracket(a,b):
    t=(a,b)
    # Includes all t in [a,b], even when 2*t^2-t-2 changes sign.
    AI=neg(mul(mul(t,(a+4,b+4)),(2*a*a-b-2,2*b*b-a-2)))
    QI=(Q(a),Q(b))
    wlo=F(0) if a<=1<=b else min(abs(a-1),abs(b-1))
    whi=max(abs(a-1),abs(b-1))
    KI=(series(wlo,'K')[0],series(whi,'K')[1])
    HI=(series(a/2,'H')[0],series(b/2,'H')[1])
    C=(-2*b*(2*b+7),-2*a*(2*a+7))
    return add(mul(AI,KI),mul(QI,HI),C)

def run():
    # For t in (0,1/8]: A/t >= 8, log((2+t)/t) > 8/3,
    # H <= t/(1-t^2/4) <= 256t/255 and C >= -14t:
    # F(t) > t*(64/3-1536/255-14) > 0.
    assert F(64,3)-F(1536,255)-14>0
    # For t in [15/8,2): A<0, L >= 2/(t+1),
    # H >= 2*sum_{k=0}^4 (15/16)^(2k+1)/(2k+1) >3,
    # B=t-6<=-4 and F<=(t-2)(11t+9)/(t+1)<0.
    assert sum(2*F(15,16)**(2*k+1)/F(2*k+1) for k in range(5))>3
    # The intermediate range checks G(t) = -F(t)/(t-1)>0 with a
    # continuous interval certificate, including t=1 where G extends smoothly.
    n=512; left=F(1,8);span=F(7,4)
    least=(F(10**10),None)
    for i in range(n):
        a=left+span*F(i,n);b=left+span*F(i+1,n)
        lo,hi=bracket(a,b)
        if lo<least[0]:least=(lo,i)
        if lo<=0:raise AssertionError(('nonpositive enclosure',i,a,b,lo,hi))
    print('PASSED: exact continuous monotonicity certificate')
    print('intervals',n,'lowest lower bound >',float(least[0]),'index',least[1])
    print('atanh series N',N,'scale',S,'H-tail upper',float(F(H_TAIL,S)),'K-tail upper',float(F(K_TAIL,S)))
    print('G(t)>0 on [1/8,15/8], plus analytic tails; F(t) sign is sign(1-t).')
if __name__=='__main__':run()
