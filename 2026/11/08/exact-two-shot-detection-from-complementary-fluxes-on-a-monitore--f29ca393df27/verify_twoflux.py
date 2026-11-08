"""Finite and exact checks for complementary-flux monitored triangle.

Requires Python 3, NumPy, SymPy and SciPy. All conventions and matrices
are defined locally; the mathematical proof is independent of sampling.
"""
from math import pi, sqrt
import numpy as np
import sympy as sp
from scipy.linalg import expm

J = 1.0
T = np.zeros((3,3), dtype=complex)
T[0,1] = T[1,2] = T[2,0] = 1
Q = np.diag([0.,1.,1.]).astype(complex)
P = np.diag([1.,0.,0.]).astype(complex)

def hamiltonian(flux):
    return -(np.exp(1j*flux)*T + np.exp(-1j*flux)*T.conj().T)

def two_step(tau):
    u0 = expm(-1j*hamiltonian(0)*tau)
    u1 = expm(-1j*hamiltonian(pi/3)*tau)
    a = (Q@u0@Q)[1:,1:]
    b = (Q@u1@Q)[1:,1:]
    return a, b

def exact_norm(tau):
    t = (5+4*np.cos(3*tau))/9
    return (np.sqrt(16*t+(1-t)**2)+1-t)/4

# Exact Gram/projection calculation at the optimal phase.
s3 = sp.sqrt(3)
w = (-1+sp.I*s3)/2
u0=sp.Matrix([1,1])/sp.sqrt(2)
u1=sp.Matrix([w,w**2])/sp.sqrt(2)
p0=sp.simplify(u0*u0.conjugate().T)
p1=sp.simplify(u1*u1.conjugate().T)
assert sp.simplify(p0*p0-p0) == sp.zeros(2)
assert sp.simplify(p1*p1-p1) == sp.zeros(2)
assert sp.simplify((u0.conjugate().T*u1)[0]+sp.Rational(1,2)) == 0
A=sp.eye(2)-sp.Rational(4,3)*p0
B=sp.eye(2)-sp.Rational(4,3)*p1
C=sp.simplify(B*A)
assert sp.simplify(sp.trace(C)+sp.Rational(2,9))==0
assert sp.simplify(C.det()-sp.Rational(1,9))==0
char=sp.expand(C.charpoly().as_expr())
x=C.charpoly().gen
assert sp.simplify(char-(x*x+sp.Rational(2,9)*x+sp.Rational(1,9)))==0
G=sp.simplify(C.conjugate().T*C)
y=sp.symbols('y')
assert sp.simplify(G.trace()-sp.Rational(2,9)-sp.Rational(16,81))==0
assert sp.simplify(G.det()-sp.Rational(1,81))==0
lamhi=((sp.sqrt(13)+2)/9)**2
lamlo=((sp.sqrt(13)-2)/9)**2
assert sp.simplify(lamhi+lamlo-G.trace())==0
assert sp.simplify(lamhi*lamlo-G.det())==0
# Strict derivative of p+(t) on (0,1):
t=sp.symbols('t',real=True)
F=(sp.sqrt(16*t+(1-t)**2)+(1-t))/4
derivative=sp.simplify(sp.diff(F,t))
assert sp.simplify(derivative-((7+t)/sp.sqrt(1+14*t+t*t)-1)/4)==0
assert sp.expand((7+t)**2-(1+14*t+t*t))==48

# Independent 3x3 exponential versus 2x2 analytic formula.
count=0
for tau in np.linspace(0.015, 2*pi/3-0.015, 1001):
    a,b=two_step(float(tau))
    z=np.exp(3j*tau)
    aa=(1+2*z)/3
    bb=np.conj(aa)
    o=np.exp(2j*pi/3)
    v0=np.array([1,1],complex)/sqrt(2)
    v1=np.array([o,o**2],complex)/sqrt(2)
    formula_a=np.eye(2)+(aa-1)*np.outer(v0,np.conj(v0))
    formula_b=np.eye(2)+(bb-1)*np.outer(v1,np.conj(v1))
    assert np.linalg.norm(a*np.exp(1j*tau)-formula_a)<1e-12
    assert np.linalg.norm(b*np.exp(-1j*tau)-formula_b)<1e-12
    sing=np.linalg.svd(b@a,compute_uv=False)
    assert abs(sing[0]-exact_norm(tau))<2e-12
    assert sing[0] < 1
    assert abs(np.prod(sing)-(5+4*np.cos(3*tau))/9)<2e-12
    count+=1

# Zero switching threshold and exact optimum.
for m in range(1,5):
    a,b=two_step(2*pi*m/3)
    assert abs(np.linalg.svd(b@a,compute_uv=False)[0]-1)<1e-12
    count+=1
for m in range(4):
    tau=(2*m+1)*pi/3
    a,b=two_step(tau)
    c=b@a
    assert abs(np.linalg.svd(c,compute_uv=False)[0]-(2+sqrt(13))/9)<1e-12
    assert abs(max(abs(np.linalg.eigvals(c)))-1/3)<1e-12
    count+=1

# Exact single-flux dark components and asymptotic survival.
ket1=np.array([0,1,0],complex)
for flux in (0.,pi/3):
    for tau in (0.15,0.48,1.04):
        u=expm(-1j*hamiltonian(flux)*tau)
        s=Q@u@Q
        rem=np.linalg.matrix_power(s,1000)@ket1
        assert abs(np.vdot(rem,rem).real-0.5)<1e-10
        count+=1

# Two-flux repeated monitoring: universal exact contraction bound.
for tau in (0.19,0.7,pi/3,1.67):
    a,b=two_step(tau)
    c=b@a
    for n in range(1,15):
        sn=np.linalg.norm(np.linalg.matrix_power(c,n),2)
        assert sn <= exact_norm(tau)**n+2e-12
        count+=1

print('PASS: exact symbolic identities and',count,'independent finite checks')
print('two-probe amplitude minimax:',(2+sqrt(13))/9)
print('guaranteed two-probe detection:',1-((2+sqrt(13))/9)**2)
print('optimal cycle spectral radius:',1/3)
