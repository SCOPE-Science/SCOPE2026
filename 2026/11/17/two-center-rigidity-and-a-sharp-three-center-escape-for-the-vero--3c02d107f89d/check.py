#!/usr/bin/env python3
"""Independent finite checks for the two-to-three covering threshold of the Veronese surface.
Run with Python 3, NumPy and SciPy: python check.py.
Finite tests supplement, and do not replace, the all-directions argument in RESULT.md.
"""
import math
import numpy as np
from scipy.optimize import brentq

I = np.eye(3)
def p(u):
    u = np.asarray(u, dtype=float)
    return (np.outer(u,u)-I/3)/math.sqrt(2)
def matdot(A,B): return float(np.sum(A*B))
def random_sphere(rng, n):
    x = rng.normal(size=(n,3))
    return x/np.linalg.norm(x,axis=1)[:,None]

R2=1/3
threshold=21/64
v = np.array([[math.cos(j*math.pi/3),math.sin(j*math.pi/3),0.] for j in range(3)])
centers=np.array([-p(w)/8 for w in v])
assert np.allclose(np.linalg.norm(centers,axis=(1,2))**2,[1/192]*3)
for i in range(3):
    w=p(v[i]); d2=[matdot(w-c,w-c) for c in centers]
    assert abs(min(d2)-threshold)<1e-13,(i,d2)

rng=np.random.default_rng(106703)
units=random_sphere(rng, 40000)
check_count=0
for u in units:
    Pu=p(u)
    assert abs(matdot(Pu,Pu)-R2)<1e-13
    m2=min(matdot(Pu-c,Pu-c) for c in centers)
    assert m2<=threshold+2e-13,(u,m2)
    check_count+=2

# For any two traceless quadratic forms, the proof uses existence of a common
# isotropic projective line. Numerically verify random full-rank examples via
# the full connected null conic of the first form, using only finite sweeps.
for sample in range(60):
    A=rng.normal(size=(3,3)); A=(A+A.T)/2; A-=np.trace(A)*I/3
    B=rng.normal(size=(3,3)); B=(B+B.T)/2; B-=np.trace(B)*I/3
    eig,U=np.linalg.eigh(A)
    if sum(eig>0)==2:
        idxpos=np.where(eig>0)[0]; idxneg=np.where(eig<0)[0][0]
        neg=U[:,idxneg]; a,b=U[:,idxpos].T
        def uv(t):
            x=math.cos(t)*a+math.sin(t)*b
            lp=float(x@A@x); ln=float(neg@A@neg)
            return math.sqrt(-ln/(lp-ln))*x+math.sqrt(lp/(lp-ln))*neg
    else:
        idxneg=np.where(eig<0)[0]; idxpos=np.where(eig>0)[0][0]
        pos=U[:,idxpos]; a,b=U[:,idxneg].T
        def uv(t):
            x=math.cos(t)*a+math.sin(t)*b
            ln=float(x@A@x); lp=float(pos@A@pos)
            return math.sqrt(lp/(lp-ln))*x+math.sqrt(-ln/(lp-ln))*pos
    def g(t):
        u=uv(t)
        return float(u@B@u)
    grid=np.linspace(0,2*math.pi,4097)
    vals=[g(t) for t in grid]
    sign_brackets=[j for j in range(len(vals)-1) if vals[j]*vals[j+1]<=0]
    assert sign_brackets,('no sign crossing',sample,min(vals),max(vals))
    j=sign_brackets[0]
    root=brentq(g,grid[j],grid[j+1],xtol=1e-12)
    u=uv(root)
    assert abs(u@A@u)<1e-10 and abs(u@B@u)<1e-10
    assert abs(np.linalg.norm(u)-1)<1e-10
    check_count+=3

# Exact rational identities used in the analytical certificate.
from fractions import Fraction as F
assert F(1,3)+F(1,64*3)-F(1,96)==F(21,64)
assert F(1,3)-F(21,64)==F(1,192)
assert F(1,3)-F(1,4)==F(1,12)
check_count+=3
print(f'PASS {check_count} finite checks; exact squared three-center radius 21/64')
