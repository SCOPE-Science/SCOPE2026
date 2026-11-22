"""Reproducible exact checks for the geometric-minification count-chain theorem.

Requires Python 3 and SymPy. This is a finite symbolic verification of
identities used in the analytic proof, not a replacement for that proof.
"""
from fractions import Fraction
import sympy as sp

q,r,s,t=sp.symbols('q r s t', positive=True)
K=(1-r)/(1-q*r)
B=lambda z: K*(1-q*r*z)/(1-r*z)
G=lambda z: (1-r)/(1-r*z)
F=B(t)*((1-q)*G(s)+q*(1-t)*G(s*q*t))/(1-q*t)
Fshock=(1-q*r)*B(s)*B(t)/(1-q*r*s*t)
assert sp.factor(F-Fshock)==0, 'joint PGF factorization'
assert sp.factor(Fshock-Fshock.xreplace({s:t,t:s}))==0, 'symmetry'
assert sp.factor(Fshock.subs({s:1})-G(t))==0, 'second marginal'
assert sp.factor(Fshock.subs({t:1})-G(s))==0, 'first marginal'

# General exact low-cell formulas in symbolic parameters.
p0=(1-q*r)*K**2
p01=p0*(1-q)*r
p11=p0*((1-q)**2*r**2+q*r)
p02=r*p01
p12=r*(p11-(1-q*r)*K**2*q*(q*r))
M00=sp.factor(p0*p11-p01*p01)
M01=sp.factor(p01*p12-p11*p02)
assert sp.factor(M00-q*r*(1-r)**4/(1-q*r)**2)==0
assert sp.factor(M01+q**2*(1-q)*r**3*(1-r)**4/(1-q*r)**2)==0

# Exact discrete case checks, including one-step transition and arbitrary
# finite cutoffs for all three minor bands.
Q,R=Fraction(2,5),Fraction(3,7)
Kv=(1-R)/(1-Q*R)
def e(n):
    return Kv if n==0 else Kv*(1-Q)*R**n
def joint(i,j):
    return sum((1-Q*R)*(Q*R)**k*e(i-k)*e(j-k)
               for k in range(min(i,j)+1))
def transition(x,y):
    return sum((Q**x if z==x else (1-Q)*Q**z)*e(y-z)
               for z in range(min(x,y)+1))
for i in range(16):
    for j in range(16):
        assert joint(i,j)==joint(j,i)
        assert joint(i,j)==(1-R)*R**i*transition(i,j)
for i in range(12):
    for j in range(12):
        minor=joint(i,j)*joint(i+1,j+1)-joint(i+1,j)*joint(i,j+1)
        target=1 if i==j else (-1 if abs(i-j)==1 else 0)
        sign=(minor>0)-(minor<0)
        assert sign==target,(i,j,minor,target)
print('PASS: PGF identities, symmetry, marginals, signed minors and transitions')
