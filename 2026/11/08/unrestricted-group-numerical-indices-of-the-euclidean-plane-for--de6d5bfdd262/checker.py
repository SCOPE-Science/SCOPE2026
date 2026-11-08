"""Finite diagnostics for planar orthogonal-group numerical indices.
Run: python checker.py. Infinity assertions in the accompanying mathematical proof
are not delegated to this finite script.
"""
import cmath
import math
import random
import numpy as np

RNG = random.Random(1729)
checks = 0

def check(test, message=''):
    global checks
    assert test, message
    checks += 1

def real_matrix(a,b):
    return np.array([[ (a+b).real, -(a-b).imag],
                     [ (a+b).imag, (a-b).real]], dtype=float)

def rotations(m):
    return [np.array([[math.cos(2*math.pi*k/m), -math.sin(2*math.pi*k/m)],
                     [math.sin(2*math.pi*k/m),  math.cos(2*math.pi*k/m)]]) for k in range(m)]

def symmetric_top(M):
    return float(np.linalg.eigvalsh((M+M.T)/2)[-1])

def h(a,m):
    return max((a*cmath.exp(2j*math.pi*k/m)).real for k in range(m))

def vg_exact(a,b,m,dihedral):
    first = abs(b)+h(a,m)
    return max(first,abs(a)+h(b,m)) if dihedral else first

def vg_matrix(a,b,m,dihedral):
    T=real_matrix(a,b)
    refl=np.diag([1.,-1.])
    mats=rotations(m)
    if dihedral: mats += [g@refl for g in mats]
    return max(symmetric_top(T@g) for g in mats)

for m in range(1,14):
    c=math.cos(math.pi/m)
    z=cmath.exp(1j*math.pi/m)
    for dihedral in (False,True):
        # Genuine equality cases for full index, including m=1.
        if dihedral:
            a=b=z/2
            n=(1+c)/2
        else:
            a=z; b=0j
            n=c
        check(abs(vg_exact(a,b,m,dihedral)-n)<1e-12,('min',m,dihedral))
        check(abs(vg_matrix(a,b,m,dihedral)-n)<1e-11,('matrix_min',m,dihedral))
        for t in range(120):
            a=complex(RNG.uniform(-2,2), RNG.uniform(-2,2))
            b=complex(RNG.uniform(-2,2), RNG.uniform(-2,2))
            ex=vg_exact(a,b,m,dihedral)
            direct=vg_matrix(a,b,m,dihedral)
            norm=abs(a)+abs(b)
            check(abs(ex-direct)<2e-11,('direct',m,dihedral,t,ex,direct))
            check(ex>=n*norm-2e-11,('bound',m,dihedral,t))
            check(abs(np.linalg.norm(real_matrix(a,b),2)-norm)<2e-11,('opnorm',m,dihedral,t))
            if dihedral:
                check(ex >= n*norm+(1-c)*abs(abs(a)-abs(b))/2-1e-11)
        # rank-one infimum already known; included to test overlap boundary.
        a=z/2; b=z/2
        check(abs(vg_exact(a,b,m,dihedral)-(1+c)/2)<1e-12)

# Every finite nonzero rank-one 2x2 matrix has conformal / anticonformal
# coefficients of equal modulus, hence same minimizing rank-one index.
for t in range(500):
    u=np.array([math.cos(RNG.random()*2*math.pi),math.sin(RNG.random()*2*math.pi)])
    v=np.array([math.cos(RNG.random()*2*math.pi),math.sin(RNG.random()*2*math.pi)])
    M=np.outer(u,v)
    a=(M[0,0]+M[1,1]+1j*(M[1,0]-M[0,1]))/2
    b=(M[0,0]-M[1,1]+1j*(M[1,0]+M[0,1]))/2
    check(abs(abs(a)-abs(b))<1e-13)
    check(np.allclose(real_matrix(a,b),M,atol=1e-13))

print(f'PASS: {checks} finite algebraic, norm, and equality diagnostics')
