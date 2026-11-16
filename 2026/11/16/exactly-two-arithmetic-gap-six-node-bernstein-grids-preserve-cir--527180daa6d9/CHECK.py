#!/usr/bin/env python3
"""Exact rational-interval certificate for degree-five circle Bernstein grids.
Only Python standard library is required.  Bounds are proved by squaring
integer endpoints and by the classical rational estimates for pi.
"""
from fractions import Fraction as F

class I:
    def __init__(self,a,b=None):
        self.a=F(a);self.b=F(a if b is None else b)
        assert self.a<=self.b
    def __add__(self,other):
        other=as_i(other);return I(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,other):return self+(-as_i(other))
    def __rsub__(self,other):return as_i(other)+(-self)
    def __mul__(self,other):
        other=as_i(other);a=[x*y for x in (self.a,self.b) for y in (other.a,other.b)];return I(min(a),max(a))
    __rmul__=__mul__
    def __pow__(self,n):
        assert n in (1,2)
        if n==1:return self
        if self.a>=0:return I(self.a**2,self.b**2)
        if self.b<=0:return I(self.b**2,self.a**2)
        return I(0,max(self.a*self.a,self.b*self.b))
    def __truediv__(self,other):
        other=as_i(other)
        assert other.a>0 or other.b<0
        return self*I(1/other.b,1/other.a)
    def __repr__(self):return f'[{float(self.a):.6f},{float(self.b):.6f}]'

def as_i(x):return x if isinstance(x,I) else I(x)
def positive(x):return as_i(x).a>0
def negative(x):return as_i(x).b<0

# Machin identity pi=16 arctan(1/5)-4 arctan(1/239).
# Exact alternating finite series bounds prove 3.14159<pi<3.14160.
def atan_bounds(x,n):
    terms=[(-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n+2)]
    a=sum(terms[:n+1],F(0)); b=a+terms[n+1]
    return I(min(a,b),max(a,b))
pi_band=16*atan_bounds(F(1,5),9)-4*atan_bounds(F(1,239),3)
assert pi_band.a>F(314159,100000) and pi_band.b<F(314160,100000)
assert pi_band.a*pi_band.a>F(9869,1000)
assert pi_band.b*pi_band.b<F(9870,1000)
pisq=I(F(9869,1000),F(9870,1000))
s3=I(F(173205,100000),F(173206,100000))
s5=I(F(223606,100000),F(223607,100000))
assert s3.a*s3.a<3<s3.b*s3.b
assert s5.a*s5.a<5<s5.b*s5.b

def cosine(m,q):
    m%=2*q
    if m>q:m=2*q-m
    if q==5:
        a=(I(1)+s5)*F(1,4)
        b=(s5-I(1))*F(1,4)
        return [I(1),a,b,-b,-a,I(-1)][m]
    if q==6:
        v=s3*F(1,2)
        return [I(1),v,I(F(1,2)),I(0),I(F(-1,2)),-v,I(-1)][m]
    raise ValueError(q)

checks=0
for q in (5,6):
    for m in range(1,2*q+1):
        a=cosine(m,q); b=cosine(2*m,q)
        p1=5*(a-1)
        p3=60*(((-1)**m-3)*b+3*a-1)
        p5=I(0) if m%2==0 else 240*(-1+5*a-10*b)
        if m%2==0:
            mean=(1+a+b)*F(1,3)
            assert mean.a>=0, (q,m,'mean',mean)
            # For q=6, m=4,8 the mean is identically zero: cos= -1/2,-1/2.
            if q==6 and m in (4,8): assert mean.a==mean.b==0
            if m==2*q:
                assert p1.a==p1.b==p3.a==p3.b==p5.a==p5.b==0
            else:
                assert negative(p1*4*pisq-p3),(q,m,'even',p1*4*pisq-p3)
                assert p5.a==p5.b==0
            checks+=1
        else:
            assert p1.b<0,(q,m,'p1',p1)
            def P(T):return p1*T*T-p3*T+p5
            T1=pisq;T3=9*pisq
            assert negative(P(T1)),(q,m,'k1',P(T1))
            assert negative(P(T3)),(q,m,'k3',P(T3))
            assert negative(2*p1*T3-p3),(q,m,'derivative',2*p1*T3-p3)
            checks+=3
# The coefficient for m=1 and k=3 is -4 P(9*pi^2)/(9*pi^2)^3.
# At t<=pi/8 put a=cos(t)>=0.923. The following polynomial is P
# evaluated at b=cos(2t)=2*a*a-1, with T=9*pi^2.
T=9*pisq
a=I(F(923,1000))
Q=(480*T-4800)*a*a + (5*T*T-180*T+1200)*a -5*T*T-180*T+2160
# cos(pi/8)^2=(2+sqrt(2))/4, and sqrt(2)>1.414.
assert F(1414,1000)**2 < 2
assert (F(2)+F(1414,1000))/4 > F(923,1000)**2
assert positive(Q),('exclusion_small_t',Q)
# The derivative in a is positive for all a>=0.923 because both
# 480*T-4800 and 5*T^2-180*T+1200 are positive.
assert positive(480*T-4800)
assert positive(5*T*T-180*T+1200)
checks+=3
# t=2*pi/9, m=9 gives samples (1,1,1,-1,-1,-1),
# P(T)=120*T-1440. At k=3, T=9*pi^2>12.
assert positive(120*T-1440)
checks+=1
# For p=7, the negative zero mode has mean (1-cos(pi/7)-cos(3*pi/7))/3.
# Using cos(z)>1-z^2/2, pi^2<9.870 shows cos(pi/7)>1-pi^2/98,
# cos(2*pi/7)>1-2*pi^2/49. And
# cos(pi/7)+cos(3*pi/7)=2 cos(pi/7)cos(2*pi/7)>1.
u=I(1)-pisq*F(1,98)
v=I(1)-pisq*F(2,49)
assert positive(2*u*v-1),(u,v,2*u*v-1)
checks+=1
print('EXACT_RATIONAL_INTERVAL_CHECK_OK conditions=',checks, 'small_t_Plower=',float(Q.a))
