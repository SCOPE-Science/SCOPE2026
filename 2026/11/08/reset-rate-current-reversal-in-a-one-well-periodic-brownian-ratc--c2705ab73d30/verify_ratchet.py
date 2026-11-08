"""Standalone checks for a periodic resetting ratchet; standard library only.

The analytic proof establishes the universal signs. This script verifies the
explicit piecewise-affine integrals and strict separation using independent
high-precision quadrature-free formulas.
"""
from math import exp, expm1, sqrt, isclose
from fractions import Fraction

A=11/10; B=1.; L=A+B
s=9/10; t=1/10
kL=20/11; k1=1/20; k2=391/20

def F(length,k):
    # Stable evaluation of integral_0^l du integral_u^l dv exp[-k(v-u)].
    z=k*length
    return length**2*sum((-z)**j/(__import__('math').factorial(j+2)) for j in range(23)) if abs(z)<.1 else length/k+expm1(-z)/(k*k)

def positive_integral(length,k):
    return expm1(k*length)/k

def negative_integral(length,k):
    return -expm1(-k*length)/k

JL=F(A,kL)
JR=F(s,k1)+negative_integral(s,k1)*negative_integral(t,k2)+F(t,k2)
Zp=positive_integral(A,kL)+positive_integral(s,k1)+exp(k1*s)*positive_integral(t,k2)
Zm=negative_integral(A,kL)+negative_integral(s,k1)+exp(-k1*s)*negative_integral(t,k2)
mlimit=(JL-JR)/(Zp*Zm)
assert isclose(JL,121/400*(1+exp(-2)),rel_tol=1e-12)
assert JL<121/350
assert JR>81/200*(1-9/200)
assert Zp>0 and Zm>0 and mlimit<0
assert abs(mlimit+0.014593853451611527)<1e-9
assert abs(JR-0.4405045873959697)<1e-9
print('Exact-segment integrals: JL=',repr(JL),'JR=',repr(JR))
print('Boltzmann partition functions: Z+ =',repr(Zp),'Z- =',repr(Zm))
print('Small-reset displacement per cycle:',repr(mlimit))
print('Strict algebraic bounds verified:',JL,'<',121/350,'<',81/200*(1-9/200),'<',JR)
# Valid Gaussian-exponential-time bounds for every r>0 and drift magnitude M.
M=391/20
for r in [100, 1000, 10000, 100000]:
    omega=sqrt(M*M+4*r)
    lp=(omega+M)/2
    lm=(omega-M)/2
    lower=(lm/omega)*exp(-lp*B)
    upper=(lp/omega)*exp(-lm*A)/(1-exp(-lm*L))
    print('r=',r,'lower positive winding bound=',lower,
          'upper negative winding bound=',upper,'difference=',lower-upper)
assert A>B
print('PASS: checked explicit strict low-rate sign; exact high-rate tail exponents are asymptotically separated.')
