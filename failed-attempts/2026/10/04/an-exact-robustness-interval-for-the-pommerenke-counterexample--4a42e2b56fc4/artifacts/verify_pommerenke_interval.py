#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

def z(a=0, b=0):
    return (F(a), F(b))

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def sub(x, y):
    return (x[0]-y[0], x[1]-y[1])

def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def scale(c, x):
    return (c*x[0], c*x[1])

def conj(x):
    return (x[0], -x[1])

def real_mul_conj(x, y):
    return mul(x, conj(y))[0]

def inv(x):
    d = x[0]*x[0] + x[1]*x[1]
    return (x[0]/d, -x[1]/d)

q = (F(1,3), -F(1,6))
q2 = mul(q,q)
q3 = mul(q2,q)
w = sub(z(1,0), q3)
r2 = F(399,400)**2
alpha = (F(8,9), F(4,9))

Fp = sub(z(1,0), scale(r2,alpha))
Gp = q2
FC = add(z(1,0), scale(r2,alpha))
GC = sub(scale(F(2), inv(q)), q2)

# D(lambda)=Gp+lambda(Fp-Gp), N(lambda)=GC+lambda(FC-GC)
d0, d1 = Gp, sub(Fp,Gp)
n0, n1 = GC, sub(FC,GC)

p0 = real_mul_conj(n0,d0)
p1 = real_mul_conj(n1,d0) + real_mul_conj(n0,d1)
p2 = real_mul_conj(n1,d1)
q0 = real_mul_conj(d0,d0)
q1 = 2*real_mul_conj(d1,d0)
q2c = real_mul_conj(d1,d1)

common = F(1,25920000000)
assert (p0,p1,p2) == tuple(common*x for x in (2956000000,-17772056000,15391097599))
assert (q0,q1,q2c) == tuple(common*x for x in (500000000,2046392000,2868678401))

A = 15391097599
B = -17772056000
C = 2956000000
disc = B*B - 4*A*C
assert disc == 133861636456560000000
assert disc == 36000**2 * 103288299735

# Source specialization lambda=3/5.
lam = F(3,5)
P = A*lam*lam + B*lam + C
Q = 2868678401*lam*lam + 2046392000*lam + 500000000
assert P/Q == -F(54160961609,69013985609)

getcontext().prec = 60
sd = Decimal(103288299735).sqrt()
den = Decimal(15391097599)
center = Decimal(8886028000)/den
rad = Decimal(18000)*sd/den
lo, hi = center-rad, center+rad
assert Decimal("0.201486508538006") < lo < Decimal("0.201486508538008")
assert Decimal("0.953210606835667") < hi < Decimal("0.953210606835670")
assert lo < Decimal(3)/Decimal(5) < hi

print("VERIFY_OK")
print("lambda_minus =", lo)
print("lambda_plus  =", hi)
print("interval_length =", hi-lo)
print("source_curvature =", Decimal(-54160961609)/Decimal(69013985609))
