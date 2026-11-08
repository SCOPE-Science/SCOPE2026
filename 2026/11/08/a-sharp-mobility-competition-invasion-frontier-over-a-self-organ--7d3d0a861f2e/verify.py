"""Reproduce exact Fourier and invasion-frontier coefficients.
Run: python verify.py. Analytical existence and infinite-dimensional estimates are in RESULT.md.
"""
from fractions import Fraction
import sympy as s

pi=s.pi
kap=-s.Rational(2,3)/pi
Dc=-kap/9
A0=-kap/2
A6=s.Rational(1,8)
C=s.simplify(-A0*(1+kap)-kap*A6/2)
d2=s.simplify(C/9)

def plus(a,b):
    d=a.copy()
    for n,z in b.items(): d[n]=s.expand(d.get(n,0)+z)
    return d

def multiply(a,b):
    d={}
    for n,x in a.items():
        for m,y in b.items(): d[n+m]=s.expand(d.get(n+m,0)+x*y)
    return d

def K(a):
    def k(n):
        if n==0: return s.S.One
        if n%2==0:return s.S.Zero
        # sin(n*pi/2)/(n*pi/2)
        return s.simplify(2*s.sin(n*pi/2)/(n*pi))
    return {n:s.simplify(z*k(n)) for n,z in a.items()}

U0={0:s.S.One}
U1={3:s.Rational(1,2),-3:s.Rational(1,2)}
U2={0:A0,6:A6/2,-6:A6/2}
# Coefficient at t^2: D_c U_2'' - K U_2 - U_1 K U_1
F2={n:s.simplify((-Dc*n*n)*z) for n,z in U2.items()}
F2=plus(F2,{n:-z for n,z in K(U2).items()})
F2=plus(F2,{n:-z for n,z in multiply(U1,K(U1)).items()})
assert all(s.simplify(z)==0 for z in F2.values()),F2
# At t^3, the sole resonant part is -9*d2*U1 - U1*K(U2) - U2*K(U1)
F3=plus({n:s.simplify(-9*d2*z) for n,z in U1.items()},
        {n:-z for n,z in multiply(U1,K(U2)).items()})
F3=plus(F3,{n:-z for n,z in multiply(U2,K(U1)).items()})
assert s.simplify(F3[3])==0 and s.simplify(F3[-3])==0
assert s.simplify(Dc-2/(27*pi))==0
assert s.simplify(C-(16-21*pi)/(72*pi**2))==0
assert C.evalf()<0 and d2.evalf()<0
# For every integer n>=1 except n=3: the spectrum -D_c*n^2 - sin(n*pi/2)/(n*pi/2) is strictly negative.
# n even: -Dc*n^2<0; n=4j+1: multiplier positive; n=4j+3>=7: 1/n<n^2/27.
for n in range(1,1000):
    if n==3:continue
    eigen=-Dc*n*n-s.simplify(2*s.sin(n*pi/2)/(n*pi))
    assert eigen.evalf()<0,(n,eigen)
# Second-order invasion-threshold coefficient a2(d) = -A0+kap**2/(18*d).
d=s.symbols('d',positive=True)
a2=-A0+kap**2/(18*d)
assert s.simplify(a2.subs(d,Dc))==0
assert s.simplify(s.diff(a2,d).subs(d,Dc)+s.Rational(9,2))==0
assert s.simplify(a2-(2/(81*pi**2*d)-1/(3*pi)))==0
# zero-diffusion and infinite-diffusion endpoints have positive/negative first corrections.
assert s.simplify(-kap-2/(3*pi))==0
assert A0>0
print('VERIFY_OK', 'Dc=',Dc,'C=',C,'D(t) quadratic=',d2,'a2(d)=',a2)
