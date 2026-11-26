#!/usr/bin/env python3
"""Separate facet-determinant check for the two-pentagon 4-polytope.

Requirements: Python 3, numpy, sympy. Numerical diagonalization is a
consistency check; the exact proof of the spectrum is in RESULT.md.
"""
import math
import numpy as np
import sympy as sp

n=5
th=2*math.pi/n
s=math.sin(th)
E=[]; B=[]; T=[]
for i in range(n):
    c=math.cos(i*th); q=math.sin(i*th)
    E.append([c,q,0.,0.]); T.append([[ -q,c,0,0],[0,0,1,0],[0,0,0,1]])
for i in range(n):
    c=math.cos(i*th); q=math.sin(i*th)
    B.append([0.,0.,c,q]); T.append([[0,0,-q,c],[1,0,0,0],[0,1,0,0]])
p=np.array(E+B, dtype=float)
t=np.array(T, dtype=float)
facets=[(i,(i+1)%n,n+j,n+(j+1)%n) for i in range(n) for j in range(n)]

def det(a):
    return float(np.linalg.det(np.array(a)))

def signed_volume(points):
    return sum(det(points[list(f)]) for f in facets)/24

V0=signed_volume(p)
Vstar=25*(10+2*math.sqrt(5))/384
assert abs(V0-Vstar)<1e-13

# Analytic constrained Hessian, assembled from the 25 facet determinants.
H=np.zeros((30,30))
for f in facets:
    base=p[list(f)]
    db=det(base)
    for r,j in enumerate(f):
        for a in range(3):
            k=3*j+a
            H[k,k]+=db/24
    for r in range(4):
        for h in range(r+1,4):
            j=f[r]; l=f[h]
            for a in range(3):
                for b in range(3):
                    q=base.copy(); q[r]=t[j,a]; q[h]=t[l,b]
                    k=3*j+a; m=3*l+b
                    z=-det(q)/24
                    H[k,m]+=z; H[m,k]+=z
H=(H+H.T)/2
roots=np.linalg.eigvalsh(H/2)

sq5=sp.sqrt(5)
bands=[(sp.Integer(0),6), (sp.Rational(25,192),4),
       (5*(5+sq5)/192,12), (25*(3+sq5)/384,4),
       (5*(5+sq5)/96,4)]
assert sum(c for x,c in bands)==30
expected=sorted([float(x) for x,c in bands for _ in range(c)])
err=max(abs(x-y) for x,y in zip(roots,expected))
assert err < 1e-12,(err,roots,expected)

# Exact algebraic checks of the cyclic Laplacian eigenvalues and four bands.
s2=(5+sq5)/8
lam1=(5-sq5)/2; lam2=(5+sq5)/2
assert sp.simplify(5*s2*lam1/48-sp.Rational(25,192))==0
assert sp.simplify(5*s2*lam2/48-25*(3+sq5)/384)==0
assert sp.simplify(5*s2/24-5*(5+sq5)/192)==0
assert sp.simplify(5*s2/12-5*(5+sq5)/96)==0
assert all(float(x)>0 for x,c in bands if x!=0)

# Independent finite-difference check using direct (not Hessian) facet volume.
def chart(z):
    v=np.einsum('ij,ijk->ik',z.reshape(10,3),t)
    return (p+v)/np.sqrt(1+np.sum(v*v,axis=1))[:,None]

rng=np.random.default_rng(6171)
max_relative=0
for k in range(20):
    z=rng.normal(size=30)
    z/=np.linalg.norm(z)
    dt=1e-3
    fwd=signed_volume(chart(dt*z)); back=signed_volume(chart(-dt*z))
    predicted=float(z@H@z)/2
    observed=(2*V0-fwd-back)/(2*dt*dt)
    max_relative=max(max_relative,abs(predicted-observed)/(1+abs(predicted)))
assert max_relative<2e-6,max_relative

# Explicit sharp first-angular-harmonic perturbation.
z=np.zeros(30)
for i in range(5): z[3*i]=math.cos(i*th)
sharp=(z@H@z)/(2*z@z)
assert abs(sharp-25/192)<1e-13
print('PASS: 25 facets; volume',format(V0,'.14g'))
print('PASS: exact symbolic spectral band identities and multiplicities',[(str(x),c) for x,c in bands])
print('PASS: direct 30x30 constrained half-Hessian, max eigenvalue error',err)
print('PASS: 20 symmetric finite-difference checks, max normalized deviation',max_relative)
print('PASS: sharp first-harmonic quotient',sharp)
