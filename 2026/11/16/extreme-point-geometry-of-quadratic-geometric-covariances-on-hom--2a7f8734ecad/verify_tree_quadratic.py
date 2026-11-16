"""Exact algebraic checks for a quadratic radial covariance on a regular tree.

Run: python verify_tree_quadratic.py
Requires: sympy, numpy. Finite Gram tests supplement the proof, not certify it.
"""
import sympy as S
import numpy as np

q,r,a,b,x=S.symbols('q r a b x',real=True)
u=1-r*r
D=1+q*r*r-r*x
E=2*q*r-x
f=u/D
N=S.expand(u*D*D+a*r*(-2*r*D-u*E)*D+
    b*r*r*(-D*D+2*r*D*E-q*u*D+u*E*E))
assert S.simplify(D**3*(f+a*r*S.diff(f,r)+b*r*r*S.diff(f,r,2)/2)-N)==0
assert S.degree(N,x)<=2

Q=4;R=S.Rational(1,4)
N0=S.factor(N.subs({q:Q,r:R,a:S.Rational(285,164),b:S.Rational(225,164)}))
Ne=S.factor(N.subs({q:Q,r:R,a:S.Rational(195,236),b:-S.Rational(225,236)}))
assert S.simplify(N0-S.Rational(1215,41984)*x*x)==0
assert S.simplify(Ne-S.Rational(3375,60416)*(16-x*x))==0
# The three first distance coefficients form the intended normalized basis.
for n in (0,1,2):
    v=r**n*(1+a*n+b*n*(n-1)/2)
    if n==0: assert v==1
    if n==1: assert S.simplify(v-r*(1+a))==0
    if n==2: assert S.simplify(v-r*r*(1+2*a+b))==0
# Positive samples (finite radius-two ball of a 5-regular tree), not an infinity proof.
parents=[-1]
for j in range(5): parents.append(0)
for j in range(1,6):
    for k in range(4): parents.append(j)
assert len(parents)==26

def path(i):
    p=[]
    while i!=-1:
        p.append(i);i=parents[i]
    return p

def distance(i,j):
    p=path(i);s=set(path(j))
    return p.index(next(t for t in p if t in s))+path(j).index(next(t for t in p if t in s))

for A,B in [(0,0),(285/164,225/164),(195/236,-225/236)]:
    M=np.array([[(.25)**distance(i,j)*(1+A*distance(i,j)+B*distance(i,j)*(distance(i,j)-1)/2)
        for j in range(26)] for i in range(26)],dtype=float)
    lam=np.linalg.eigvalsh(M)
    assert lam[0]>1e-8, (A,B,lam[0])
print('PASS: exact symbolic multiplier, exact rational extreme points, 3 finite Gram corroborations')
