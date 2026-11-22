"""Exact finite-dimensional consistency checks of a Hermitian matrix logistic equilibrium theorem.
Finite tests supplement, rather than replace, the dimension-independent proof.
"""
from fractions import Fraction as F
from itertools import product

def mul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def minus(A,B):
    return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]
def phi(B,X):
    return mul(mul(mul(B,X),minus(eye(len(X)),X)),B)
def diag(v):
    return [[u if i==j else F(0) for j,u in enumerate(v)] for i in range(len(v))]

# All spectral-subset fixed points for a strictly nondegenerate three-mode coupling.
b=[F(3,2),F(6,5),F(4,5)]
B=diag(b)
for mask in product((0,1), repeat=2):
    x=[mask[i]*(1-F(1)/(b[i]*b[i])) for i in range(2)]+[F(0)]
    X=diag(x)
    assert phi(B,X)==X
    multipliers=[b[i]*b[j]*(1-x[i]-x[j]) for i in range(3) for j in range(i,3)]
    if mask==(1,1): assert all(-1<v<1 for v in multipliers)
    else: assert any(v>1 for v in multipliers)

# Non-diagonal fixed matrices EXIST when B has a repeated eigenvalue.
b=F(3,2)
B=diag([b,b])
P=[[F(9,25),F(12,25)],[F(12,25),F(16,25)]]
assert mul(P,P)==P
X=[[t*(1-F(1)/b**2) for t in row] for row in P]
assert X[0][1]!=0
assert phi(B,X)==X

# Exact sharp diagonal multiplier threshold and endpoint behavior.
for b,side in [(F(17,10),True),(F(7,4),False)]:
    x=1-1/b**2
    lam=b*b*(1-2*x)
    assert (abs(lam)<1)==side

# Check the two-active-mode bound at a rational grid within (1,sqrt(3)).
from math import isqrt
for k in range(11,17):
    a=F(k,10)
    for m in range(11,17):
        b=F(m,10)
        lam=(a*a+b*b-a*a*b*b)/(a*b)
        assert -1<lam<1
print('PASS: spectral subsets, off-diagonal degenerate fixed states, stability and sharp boundary')
