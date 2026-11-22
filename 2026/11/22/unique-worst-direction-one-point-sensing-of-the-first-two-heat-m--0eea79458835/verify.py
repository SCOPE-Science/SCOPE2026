"""Independent algebraic and numerical checks for a two-mode heat sensor design.

Run: python verify.py   (requires sympy 1.14 or compatible version).
This is a supplementary finite checker; the continuum theorem is proved in RESULT.md.
"""
import math
import random
import sympy as sp

z = sp.symbols('z', real=True)
a, c, b = sp.Rational(1,2), sp.Rational(1,8), sp.Rational(1,5)
Delta = a*c-b*b
assert Delta == sp.Rational(9,400)
S=(1-z)*(a+4*c*z)
P=4*z*(1-z)**2*Delta
# At an interior stationary eigenvalue, F=lambda**2-S*lambda+P=0,
# F_z=-S_z*lambda+P_z=0; eliminate lambda.
E=sp.factor(sp.diff(P,z)**2-S*sp.diff(P,z)*sp.diff(S,z)+P*sp.diff(S,z)**2)
poly=50*z**3+19*z**2+4*z-9
assert sp.simplify(E/(Delta*(1-z)**2)+poly/25)==0, E
assert sp.simplify(sp.diff(poly,z)-(150*z*z+38*z+4))==0

T = sp.symbols('T', positive=True)
A=(1-sp.exp(-2*T))/2
B=(1-sp.exp(-5*T))/5
C=(1-sp.exp(-8*T))/8
assert sp.limit((A*C-B*B)/T**4,T,0)==sp.Rational(3,4)
assert set(sp.solve(sp.diff(3*z*(1-z)/(1+4*z),z),z))=={(-1-sp.sqrt(5))/4,(-1+sp.sqrt(5))/4}

def abc(t):
    return -math.expm1(-2*t)/2, -math.expm1(-5*t)/5, -math.expm1(-8*t)/8

def e_min(u,t):
    aa,bb,cc=abc(t)
    trace=(1-u)*(aa+4*cc*u)
    det=4*u*(1-u)**2*(aa*cc-bb*bb)
    return 2*det/(trace+math.sqrt(max(0,trace*trace-4*det)))

def e_inv(u,t):
    aa,bb,cc=abc(t)
    Delta=aa*cc-bb*bb
    trace=(cc+aa/(4*u))/((1-u)*Delta)
    discriminant=((cc-aa/(4*u))**2+bb*bb/u)**.5/((1-u)*Delta)
    return .5*(trace+discriminant)

def golden(f, lo=1e-6, hi=1-1e-6):
    k=(math.sqrt(5)-1)/2
    a0,b0=hi-k*(hi-lo),lo+k*(hi-lo)
    fa,fb=f(a0),f(b0)
    for i in range(105):
        if fa>fb: lo=a0; a0=b0;fa=fb;b0=lo+k*(hi-lo);fb=f(b0)
        else: hi=b0;b0=a0;fb=fa;a0=hi-k*(hi-lo);fa=f(a0)
    return (lo+hi)/2

random.seed(2031)
checks=0
# Direct Gramian and inverse agreement, and global numerical comparison.
for t in [0.002,0.005,0.01,.03,.1,.3,1,3,10,100]:
    ustar=golden(lambda u: e_inv(u,t))
    mm=e_min(ustar,t)
    assert 0<ustar<1 and mm>0
    for j in range(1000):
        u=1e-5+(1-2e-5)*random.random()
        assert e_min(u,t) <= mm + 3e-11*max(1,mm)
        assert abs(e_min(u,t)*e_inv(u,t)-1)<8e-7
        checks+=2
    # sampled second-order strict convexity in logit u: log rho = log inverse E-eigenvalue
    for j in range(-30,31):
        x=j/5
        def phi(y):
            return math.log(e_inv(1/(1+math.exp(-y)),t))
        assert phi(x) < .5*(phi(x-.2)+phi(x+.2))
        checks+=1

# Limits at small and large observation horizons.
small=(math.sqrt(5)-1)/4
# nroots returns positive first for this polynomial on current SymPy, avoid ordering dependence
infroot=next(float(sp.re(r)) for r in sp.nroots(poly) if abs(float(sp.im(r)))<1e-11 and 0<float(sp.re(r))<1)
assert abs(golden(lambda u:e_inv(u,.002))-small)<.001
assert abs(golden(lambda u:e_inv(u,100))-infroot)<1e-8
print('PASS',checks,'supplementary tests; u_short',small,'u_infinite',infroot)
