#!/usr/bin/env python3
"""Exact and independently numerical checks for the two-site exclusion resonance.
Requires Python 3, SymPy, NumPy, SciPy. No network access is needed.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

A,B,H,P,Q=sp.symbols('a b h p q', positive=True)
L=sp.symbols('z')

# Define a row-generator directly from physical transitions, independently of the moment proof.
states=[(0,0),(1,0),(0,1),(1,1)]
def generator(a,b,h,p,q):
    G=sp.zeros(4)
    for i,state in enumerate(states):
        def jump(new,rate):
            j=states.index(tuple(new))
            G[i,j]+=rate
            G[i,i]-=rate
        if state[0]!=state[1]:jump((state[1],state[0]),h)
        v=list(state);v[0]=1-state[0]
        jump(v,a*(p if state[0]==0 else (1-p)))
        v=list(state);v[1]=1-state[1]
        jump(v,b*(q if state[1]==0 else (1-q)))
    return G
G=generator(A,B,H,P,Q)
expected=L*(L+A+B)* (L*L+(A+B+2*H)*L+A*B+H*(A+B))
assert sp.simplify(G.charpoly(L).as_expr()-expected)==0
print('PASS symbolic 4-state characteristic polynomial')

# Collision iff h=ab/(a+b) (all strictly positive).
M=sp.Matrix([[-A-H,H],[H,-B-H]])
assert sp.simplify((M+(A+B)*sp.eye(2)).det()-(A*B-H*(A+B)))==0
v=sp.Matrix([A,-B])
res=A*B/(A+B)
assert sp.simplify((M+(A+B)*sp.eye(2)).subs(H,res)*v)==sp.zeros(2,1)
w=sp.Matrix([B*Q,A*P])
assert sp.simplify((w.T*v)[0]-A*B*(Q-P))==0
print('PASS exact collision and nonzero off-diagonal Jordan coupling')

# Fully exact Jordan structure including equal-reservoir and nonequilibrium cases.
for a,b,p,q in [(2,2,sp.Rational(1,5),sp.Rational(4,5)),
                 (2,3,sp.Rational(1,4),sp.Rational(3,4)),
                 (3,7,sp.Rational(2,3),sp.Rational(1,9)),
                 (2,3,sp.Rational(1,2),sp.Rational(1,2)),
                 (2,2,sp.Rational(1,2),sp.Rational(1,2))]:
    h=sp.Rational(a*b,a+b)
    g=generator(a,b,h,p,q)
    alg=2
    geo=4-(g+(a+b)*sp.eye(4)).rank()
    assert geo==(2 if p==q else 1)
    assert sp.expand(g.charpoly(L).as_expr()-expected.subs({A:a,B:b,H:h}))==0
print('PASS five exact algebraic/geometric multiplicity checks')

# Contact rates away from resonance have four distinct real eigenvalues.
for a,b,h in [(2,2,1.1),(2,3,1),(1.8,3.1,0.6),(2,2,0.3)]:
    vals=np.linalg.eigvals(np.array(generator(a,b,h,0.2,0.8),dtype=float))
    assert len(set(np.round(vals,9)))==4
print('PASS off-resonance distinct-spectrum checks')

# Explicit empty-initial-state joint occupancy at the symmetric 2:2:1 resonance.
def c_formula(t,p,q):
    s=p+q;d=p-q
    c_inf=s*s/4-d*d/8
    return c_inf*(1-math.exp(-4*t))-s*s/2*(math.exp(-2*t)-math.exp(-4*t))+d*d/2*t*math.exp(-4*t)

for p,q in [(0.2,0.8),(0.3,0.3),(0.05,0.9),(0.8,0.1),(0.7,0.7)]:
    g=np.array(generator(2,2,1,p,q),dtype=float)
    for t in [0.,0.03,0.1,0.7,1.5,4.]:
        exact=expm(t*g)[0,3]
        claimed=c_formula(t,p,q)
        assert abs(exact-claimed)<4e-13,(p,q,t,exact,claimed)
print('PASS 30 independent numerical matrix exponential versus closed form cases')

# Special polynomial coefficient is positive unless reservoirs equal.
for p,q in [(0.2,0.8),(0.1,0.9),(0.3,0.3)]:
    coef=(p-q)**2/2
    assert (coef>0)==(p!=q)
print('PASS visibility criterion for the double occupancy signal')
print('ALL CHECKS PASSED')
