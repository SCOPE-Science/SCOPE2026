"""Self-contained finite-action numerical and exact algebra corroborations.

Run: python check_finite_action.py. The mathematical proof is analytical;
these checks test normalization, the rank-one singular-value formula,
and small symmetric/dihedral examples.
"""
from itertools import permutations
from math import cos, pi, sqrt
from fractions import Fraction
import numpy as np
import sympy as sp

s, c, z = sp.symbols('s c z', real=True)
M = sp.Matrix([[1+s*c, 0], [s*sp.sqrt(1-c*c), 1]])
B = M.T*M
assert sp.simplify(sp.trace(B)-(2+2*s*c+s*s)) == 0
assert sp.simplify(B.det()-(1+s*c)**2) == 0
assert sp.factor((sp.trace(B)**2-4*B.det())-s*s*(s*s+4+4*s*c)) == 0

checks = 3

def psi(t, x):
    return sqrt(1+t*x+t*t/2+(t/2)*sqrt(t*t+4+4*t*x))

for n in range(3, 8):
    u = np.array([n-1]+[-1]*(n-1),dtype=float)
    u /= np.linalg.norm(u)
    v = -u
    orbit = {tuple(u[list(perm)]) for perm in permutations(range(n))}
    vals = [float(np.dot(np.array(w),v)) for w in orbit]
    assert len(orbit) == n
    assert abs(max(vals)-1/(n-1)) < 1e-12
    assert abs(sum(vals)/len(vals)) < 1e-12
    assert abs(sum(t*t for t in vals)/len(vals)-1/(n-1)) < 1e-12
    checks += 4
    for t in [0.1,0.7,1.0,3.5]:
        w = np.eye(n)+t*np.outer(u,v)
        # Permutations of output vector generate the orbit with maximum overlap.
        opt = max(np.linalg.norm(np.eye(n)+t*np.outer(np.array(p),v),2) for p in orbit)
        assert abs(opt-psi(t,1/(n-1))) < 1e-11
        checks += 1

for m in range(1, 12):
    theta = [2*pi*j/m for j in range(m)]
    a = np.array([1.0,0.0])
    v = np.array([cos(pi/m),-__import__('math').sin(pi/m)])
    vals = [np.dot([cos(z),__import__('math').sin(z)],v) for z in theta]
    assert abs(max(vals)-cos(pi/m)) < 1e-11
    checks += 1
    for t in [0.3,1.,2.,3.]:
        actual = max(np.linalg.norm(np.eye(2)+t*np.outer([cos(z),__import__('math').sin(z)],v),2) for z in theta)
        assert abs(actual-psi(t,cos(pi/m))) < 1e-11
        checks += 1

for d in [2,3,4,8,20]:
    orbit = [np.eye(d+1)[k]-(1/(d+1))*np.ones(d+1) for k in range(d+1)]
    orbit = [x/np.linalg.norm(x) for x in orbit]
    for i in range(d+1):
        for j in range(d+1):
            assert abs(float(np.dot(orbit[i],orbit[j]))-(1 if i==j else -1/d)) < 1e-12
            checks += 1

print('FINITE_ORTHOGONAL_ACTION_CHECKS_OK',checks)

from itertools import product
for n in range(2,6):
    u=np.zeros(n);u[0]=1
    v=np.ones(n)/sqrt(n)
    vals=[]
    for perm in permutations(range(n)):
        for signs in product((-1.,1.),repeat=n):
            w=np.array(u[list(perm)])*np.array(signs)
            vals.append(float(np.dot(w,v)))
    assert abs(max(vals)-1/sqrt(n))<1e-12
    checks+=1
    for t in [0.25,1.,4.]:
        assert abs(max(np.linalg.norm(np.eye(n)+t*np.outer(np.array(u[list(perm)])*np.array(signs),v),2) for perm in permutations(range(n)) for signs in product((-1.,1.),repeat=n))-psi(t,1/sqrt(n)))<1e-11
        checks+=1
print('SIGNED_PERMUTATION_ACTION_CHECKS_OK',checks)
