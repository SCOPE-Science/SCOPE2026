"""Exact checks for weighted-path rooted Krylov resultants and D-optimal ties.

Requires Python 3, SymPy, NumPy and SciPy. Run: python verify.py
Computational checks supplement, but do not replace, the all-size proof.
"""
import math
from functools import reduce
from operator import mul
import sympy as sp
import numpy as np
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss

z = sp.Symbol('z')
checks = 0

def laplacian(weights):
    n = len(weights)+1
    L = sp.zeros(n)
    for i, w in enumerate(weights):
        L[i,i] += w
        L[i+1,i+1] += w
        L[i,i+1] -= w
        L[i+1,i] -= w
    return L

def krylov(L,j):
    n = L.rows
    x = sp.eye(n)[:,j]
    cols=[]
    for i in range(n):
        cols.append(x)
        x = L*x
    return sp.Matrix.hstack(*cols)

def root_factor(L,weights,j):
    n=L.rows
    a = j
    b = n-j-1
    left = L[:j,:j].charpoly(z).as_expr() if a else sp.Integer(1)
    right = L[j+1:,j+1:].charpoly(z).as_expr() if b else sp.Integer(1)
    resultant=sp.resultant(left,right,z) if a and b else sp.Integer(1)
    pref = sp.prod(weights[i]**(i+1) for i in range(j))*sp.prod(weights[i]**(n-i-1) for i in range(j,n-1))
    return sp.expand(pref*resultant)

patterns = [
    lambda n:[sp.Integer(1)]*(n-1),
    lambda n:[sp.Integer((3*i+1)%7+1) for i in range(n-1)],
    lambda n:[sp.Rational((2*i+3)%7+1, (i%3)+1) for i in range(n-1)],
]
for n in range(2,9):
    for gen in patterns:
        weights=gen(n)
        L=laplacian(weights)
        for j in range(n):
            got=krylov(L,j).det(method='domain-ge')
            expected=root_factor(L,weights,j)
            assert sp.simplify(got**2-expected**2)==0, (n,weights,j,got,expected)
            checks+=1

for n in range(2,13):
    L=laplacian([sp.Integer(1)]*(n-1))
    for j in range(n):
        d=krylov(L,j).det(method='domain-ge')
        expected=1 if math.gcd(2*(j+1)-1,n)==1 else 0
        assert abs(d)==expected, (n,j,d,expected)
        checks+=1

# Five-site mirror-symmetric weighted family: exact parametric phase factors.
a,b=sp.symbols('a b', positive=True)
w5=[a,b,b,a]
L5=laplacian(w5)
targets=[a**5*b**5, a**4*b**5*(a-2*b), sp.Integer(0), a**4*b**5*(a-2*b), a**5*b**5]
for j in range(5):
    factor=root_factor(L5,w5,j)
    assert sp.factor(factor**2-targets[j]**2)==0, (j, factor)
    checks+=1
for aa,bb,optimal in [(3,2,{0,4}),(2,2,{0,1,3,4}),(2,3,{1,3})]:
    vals=[abs(root_factor(laplacian([aa,bb,bb,aa]),[aa,bb,bb,aa],j)) for j in range(5)]
    opt={j for j,v in enumerate(vals) if v==max(vals)}
    assert opt==optimal,(aa,bb,opt)
    checks+=1

# Independently integrate the heat-response outer product by 80-point
# Gauss–Legendre quadrature, and compare with the exact spectral factor.
n=4
weights=[sp.Integer(1),sp.Integer(2),sp.Integer(3)]
L=laplacian(weights)
A=np.asarray(L, dtype=float)+0.3*np.eye(n)
alpha=np.linalg.eigvalsh(A)
T=4.0
H=np.array([[(1-math.exp(-(x+y)*T))/(x+y) for y in alpha] for x in alpha])
Delta=math.prod(alpha[l]-alpha[k] for k in range(n) for l in range(k+1,n))
nodes,quad_weights=leggauss(80)
for j in range(n):
    G=np.zeros((n,n))
    for x, wt in zip(nodes,quad_weights):
        t=T*(x+1)/2
        v=expm(-A*t)[:,j]
        G+=(T/2)*wt*np.outer(v,v)
    got=np.linalg.det(G)
    factor=float(root_factor(L,weights,j))
    expected=(factor/Delta)**2*np.linalg.det(H)
    assert math.isclose(got,expected,rel_tol=0.002,abs_tol=2e-17),(j,got,expected)
    checks+=1

# Infinite-time Cauchy formula and trace monotonicity for the unit path.
for n in range(3,9):
    w=[sp.Integer(1)]*(n-1)
    L=laplacian(w)
    mu=sp.Integer(2)
    inv=(L+mu*sp.eye(n)).inv()
    vals=[inv[i,i]/2 for i in range(n)]
    assert vals==vals[::-1]
    assert all(vals[i]>vals[i+1] for i in range((n-1)//2))
    checks+=1

print('PASS: %d exact and numerical checks.'%checks)
