"""Exact checks for tetrahedral orbit tomography; Python 3 and SymPy required.
Run: python verify.py
"""
from itertools import product
from sympy import (Matrix, Rational, I, sqrt, eye, zeros, simplify,
                   symbols, factor, conjugate)

def group():
    out=[]
    for perm in ((0,1,2),(1,2,0),(2,0,1)):
        for signs in product((-1,1), repeat=3):
            if signs[0]*signs[1]*signs[2]!=1:continue
            g=zeros(3)
            for i,j in enumerate(perm):g[i,j]=signs[i]
            out.append(g)
    assert len(out)==12
    assert {tuple((g*h)) for g in out for h in out}=={tuple(g) for g in out}
    return out
G=group()

def normalize(x):
    return Matrix(x)/sqrt(sum(z*conjugate(z) for z in x))

def projector_orbit(x):
    x=normalize(x);P=x*x.conjugate().T
    return [g*P*g.T for g in G], x

def invariant(x):
    p=[simplify(z*conjugate(z)) for z in x]
    d=simplify(sum(z*z for z in p))
    c=simplify((x[1]*conjugate(x[2]))**2 +
               (x[2]*conjugate(x[0]))**2 +
               (x[0]*conjugate(x[1]))**2)
    return d,c

def T_on(E,Q):
    return sum((((P*E).trace())*P for P in Q), zeros(3))

# Verify the explicit optimal vector, every one of nine complex matrix units.
Q,x=projector_orbit([2,2,-sqrt(7)-3*I])
assert simplify((x.conjugate().T*x)[0]-1)==0
D,C=invariant(x)
assert simplify(D-Rational(1,2))==0 and simplify(C)==0
assert simplify(sum(Q,zeros(3))-4*eye(3))==zeros(3)
for i in range(3):
    for j in range(3):
        E=zeros(3);E[i,j]=1
        assert simplify(T_on(E,Q)-E-(E.trace())*eye(3))==zeros(3)
print('PASS: exact optimized design and reconstruction identity on 9 complex matrix units')

# Independent randomized spectral tests of the closed formula.
import numpy as np
rng=np.random.default_rng(514217)
groups=[np.array(g).astype(float) for g in G]
HB=[]
for j in range(3):
    E=np.zeros((3,3),complex);E[j,j]=1;HB.append(E)
for i,j in ((0,1),(1,2),(2,0)):
    E=np.zeros((3,3),complex);E[i,j]=E[j,i]=1/np.sqrt(2);HB.append(E)
    E=np.zeros((3,3),complex);E[i,j]=-1j/np.sqrt(2);E[j,i]=1j/np.sqrt(2);HB.append(E)
for trial in range(50):
    z=rng.normal(size=3)+1j*rng.normal(size=3)
    z=z/np.linalg.norm(z)
    orbit=np.array([g@z for g in groups])
    projectors=np.array([np.outer(q,q.conj()) for q in orbit])
    M=np.array([[np.trace(E@P).real for E in HB] for P in projectors])
    numeric=np.linalg.eigvalsh(M.T@M)
    p=np.abs(z)**2
    d=np.sum(p**2)
    c=(z[1]*z[2].conjugate())**2+(z[2]*z[0].conjugate())**2+(z[0]*z[1].conjugate())**2
    predicted=sorted([4]+[6*d-2]*2+[2*(1-d)+4*abs(c)]*3+[2*(1-d)-4*abs(c)]*3)
    assert np.allclose(numeric,predicted,atol=5e-13,rtol=5e-13),(trial,numeric,predicted)
print('PASS: 50 independent randomized spectral tests of the nine eigenvalue formula')
