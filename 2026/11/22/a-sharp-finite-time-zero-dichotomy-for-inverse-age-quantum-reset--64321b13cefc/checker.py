"""Reproduce finite-horizon identities for inverse-age reset coherence.

Requires Python 3, NumPy, and SymPy. Numerical tests are finite diagnostics,
not substitutes for the analytic unit-circle spectral argument.
"""
from fractions import Fraction as F
from math import cos, sin, pi, factorial, sqrt
from itertools import product
import numpy as np
import sympy as sp

checks = 0

def verify(condition, description):
    global checks
    assert condition, description
    checks += 1

def rising(x, n):
    out = F(1)
    for k in range(n):
        out *= x + k
    return out

def coefficients(gamma, t):
    a, b = 1 - gamma, gamma
    return [rising(a, k) * rising(b, t-k) /
            (factorial(k) * factorial(t-k)) for k in range(t+1)]

def direct_age_recursion(gamma, t):
    p = [F(1)]
    for _ in range(t):
        q = [F(0)] * (len(p) + 1)
        for age, weight in enumerate(p):
            r = gamma / (age+1)
            q[0] += weight*r
            q[age+1] += weight*(1-r)
        p = q
    return p

def poly_add(A, B, factor=F(1)):
    C = [F(0)] * max(len(A), len(B))
    for i, v in enumerate(A): C[i] += v
    for i, v in enumerate(B): C[i] += factor*v
    return C

def poly_from_recurrence(gamma, t):
    a,b=1-gamma,gamma
    if t==0: return [F(1)]
    p0, p1 = [F(1)], [b,a]
    for n in range(1,t):
        zprod=[F(0)] + p1
        new=poly_add(p1,zprod,n+a)
        new=poly_add(new,p1,n+b-1) # (n+b)P + (n+a)z P
        new=poly_add(new,[F(0)]+p0,-n)
        p0,p1=p1,[v/(n+1) for v in new]
    return p1

# Exact rational age/normalization, recurrence and reciprocal identity checks.
for gamma in (F(1,7), F(1,3), F(1,2), F(2,3), F(5,6)):
    for t in range(0,19):
        c=coefficients(gamma,t)
        verify(sum(c)==1, 'normalization')
        verify(c==direct_age_recursion(gamma,t), 'age Markov recursion')
        verify(c==poly_from_recurrence(gamma,t), 'generating ODE recurrence')
        verify(c==list(reversed(coefficients(1-gamma,t))), 'reciprocity')

# Check that tridiagonal real-and-imaginary pencil gives the polynomial on
# the unit circle. This is independent of root extraction.
for gamma in (F(1,5),F(2,5),F(1,2),F(3,5),F(4,5)):
    delta = float(1 - 2*gamma)
    for t in range(1,14):
        for theta in (0.22,0.77,1.55,2.40):
            x,y=cos(theta),sin(theta)
            Q=sum(float(w)*np.exp(1j*(2*k-t)*theta) for k,w in enumerate(coefficients(gamma,t)))
            D=np.diag([1/(2*j+1) for j in range(t)])
            J=np.zeros((t,t))
            for j in range(1,t):
                val=j/sqrt(4*j*j-1)
                J[j-1,j]=J[j,j-1]=val
            matrix=x*np.eye(t)-J+1j*delta*y*D
            scale=np.prod([(2*j+1)/(j+1) for j in range(t)])
            verify(abs(Q-scale*np.linalg.det(matrix))<2e-8, 'tridiagonal determinant')

# Independent numerical root locations in each strict regime.
for gamma in (F(1,10),F(1,4),F(2,5),F(1,2),F(3,5),F(3,4),F(9,10)):
    for t in range(1,16):
        p=coefficients(gamma,t)
        roots=np.roots(list(reversed([float(v) for v in p])))
        if gamma < F(1,2):
            verify(max(abs(roots)) < 1-1e-7, 'inside circle')
        elif gamma > F(1,2):
            verify(min(abs(roots)) > 1+1e-7, 'outside circle')
        else:
            verify(max(abs(abs(roots)-1)) < 2e-6, 'on circle')

# At the boundary the unit-circle coherence matches exact Legendre values.
for t in range(0,18):
    for theta in (0.12,0.73,1.51,2.12,2.8):
        value=sum(float(w)*np.exp(1j*(2*k-t)*theta) for k,w in enumerate(coefficients(F(1,2),t)))
        leg=float(sp.legendre(t,sp.Symbol('u')).evalf(subs={'u':cos(theta)}))
        verify(abs(value-leg)<1e-9, 'Legendre expression')

print(f'PASS: {checks} checks (exact rational recursions, determinant, roots, Legendre).')
