#!/usr/bin/env python3
"""Exact algebra and high-precision checks for a scalar exponential-AVF root theorem."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import comb

# Polynomial coefficients indexed by nonnegative ascending power.
P=[F(4),F(-27),F(88),F(-170),F(200),F(-128),F(32)]
q=[F(1),F(-2),F(2)]

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c

def power(a,k):
    ans=[F(1)]
    for _ in range(k):ans=mul(ans,a)
    return ans

def add(a,b):
    res=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):res[i]+=v
    for i,v in enumerate(b):res[i]+=v
    return res

def mobius(a,b):
    # (1+u)^6 * P((a+b*u)/(1+u))
    out=[F(0)]*7
    for k,coeff in enumerate(P):
        sub=mul(power([a,b],k),power([F(1),F(1)],6-k))
        out=add(out,[coeff*v for v in sub])
    return out

def derivative(a):
    return [F(k)*a[k] for k in range(1,len(a))]

def sub(a,b):
    return add(a,[-v for v in b])

# Exact rational identities for the critical derivative calculation.
N=[F(-1),F(4),F(-8),F(4)]
den=mul(mul([F(0)]*4+[F(3)],[F(-1),F(1)]),q)
numprime=sub(mul(derivative(N),den),mul(N,derivative(den)))
assert numprime==[F(0)]*3+[-3*v for v in P]
assert N==sub(mul([F(0),F(-1),F(1)],derivative(q)),q)

left=mobius(F(0),F(3,4))
right=mobius(F(3,4),F(1))
assert list(reversed(left))==list(map(F,['17/128','57/32','21/8','121/32','33/4','15/4','4']))
assert list(reversed(right))==list(map(F,['-1','-15/4','-41/8','-91/32','-1/8','15/32','17/128']))
assert sum(P[k]*F(3,4)**k for k in range(7))==F(17,128)
assert sum(P)==-1
assert F(447,340)*F(1357,1600)==F(606579,544000)>1
# Numerically bracket G_20(z)=1 in the three analytically established intervals.
with localcontext() as ctx:
    ctx.prec=190
    t=Decimal(20)
    one=Decimal(1)
    def G(z):
        qz=one-2*z+2*z*z
        return (t*z*qz/(2*(one-z)))*(-Decimal(3)*t*t*z**4/4).exp()
    def root(a,b,ga_positive):
        # Low endpoint has G<1 if ga_positive=False; high opposite.
        assert (G(a)>one)==ga_positive
        assert (G(b)>one)!=ga_positive
        for _ in range(600):
            c=(a+b)/2
            if c==a or c==b:break
            if (G(c)>one)==ga_positive:a=c
            else:b=c
        return (a+b)/2
    z1=root(Decimal('0.01'),Decimal('0.15'),False)
    z2=root(Decimal('0.15'),Decimal('0.5'),True)
    z3=root(one-Decimal('1e-128'),one-Decimal('1e-131'),False)
    assert abs(z1-Decimal('0.11808268774461565'))<Decimal('1e-16')
    assert abs(z2-Decimal('0.20866477291248409'))<Decimal('1e-16')
    assert abs((one-z3)-Decimal('5.148200222412e-130'))<Decimal('1e-140')
    print('All rational identities and precision-190 root brackets passed.')
    print('z1=',str(z1)[:28], 'z2=',str(z2)[:28], '1-z3=',str(one-z3)[:29])
