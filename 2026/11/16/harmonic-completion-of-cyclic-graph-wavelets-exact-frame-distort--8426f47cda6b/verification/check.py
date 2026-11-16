#!/usr/bin/env python3
"""Independent finite tests of the formulas in RESULT.md; not an infinite proof."""
import math
import numpy as np
from fractions import Fraction

def cycle_laplacian(L):
    out = 2 * np.eye(L)
    for i in range(L):
        out[i,(i+1)%L] -= 1
        out[i,(i-1)%L] -= 1
    return out

def harmonic_path(n):
    m=n-1; L=2*m
    E=np.zeros((L,n))
    E[:n,:]=np.eye(n)
    for j in range(1,m):
        E[m+j,0]=j/m
        E[m+j,m]=1-j/m
    return E

checks=0
for n in range(3,101):
    m=n-1; L=2*m
    E=harmonic_path(n)
    Lap=cycle_laplacian(L)
    assert np.allclose(Lap[n:,n:]@E[n:,:],-Lap[n:,:n],atol=1e-11)
    checks+=1
    expected=sorted([1.]*(n-2)+[n*(n+1)/(6*(n-1)),n/2])
    assert np.allclose(np.linalg.eigvalsh(E.T@E),expected,atol=1e-10)
    checks+=1
    spec=sorted(2-2*math.cos(math.pi*j/m) for j in range(1,m))
    assert np.allclose(np.linalg.eigvalsh(Lap[n:,n:]),spec,atol=1e-10)
    checks+=1
    assert abs((spec[-1]/spec[0])/(1/math.tan(math.pi/(2*m))**2)-1)<1e-10
    checks+=1
# Direct frame check: take host Fourier ONB (it is a Parseval family).
for n in range(3,41):
    m=n-1; L=2*m
    E=harmonic_path(n)
    F=np.exp(2j*np.pi*np.outer(np.arange(L),np.arange(L))/L)/np.sqrt(L)
    A=F.conj().T@E
    assert np.allclose(A.conj().T@A,E.T@E,atol=1e-11)
    checks+=1
# Exact rational matrices: no rounding in endpoint Gram arithmetic.
for n in range(3,41):
    m=n-1
    a=sum(Fraction(j*j,m*m) for j in range(1,m))
    b=sum(Fraction(j*(m-j),m*m) for j in range(1,m))
    assert 1+a+b==Fraction(n,2)
    assert 1+a-b==Fraction(n*(n+1),6*(n-1))
    checks+=2
# Multidimensional lower and upper condition estimates for small grids.
for d in (2,3):
    for n in range(3,7):
        m=n-1; L=2*m
        Lap=cycle_laplacian(L)
        import functools
        Gamma=sum(np.kron(np.kron(np.eye(L**a),Lap),np.eye(L**(d-a-1))) for a in range(d))
        import itertools
        I=[sum(k[a]*L**(d-1-a) for a in range(d)) for k in itertools.product(range(L),repeat=d) if any(j>=n for j in k)]
        sub=Gamma[np.ix_(I,I)]
        lo,hi=np.linalg.eigvalsh(sub)[[0,-1]]
        eps=(n/L)**d
        lower_lam=eps*4*math.sin(math.pi/L)**2
        upper_lam=2*d*(1-math.cos(math.pi/m))
        assert lo>=lower_lam-1e-10, (d,n,lo,lower_lam)
        assert lo<=upper_lam+1e-10, (d,n,lo,upper_lam)
        assert 2*d-1e-10<=hi<=4*d+1e-10
        checks+=3
# Exact integer Krylov rank: the endpoint-forcing CG instance has full minimal polynomial.
from sympy import Matrix
for n in range(3,17):
    l=n-2
    A=Matrix(l,l,lambda i,j: 2 if i==j else (-1 if abs(i-j)==1 else 0))
    e=Matrix([1]+[0]*(l-1))
    columns=[e]
    for j in range(1,l):
        columns.append(A*columns[-1])
    assert Matrix.hstack(*columns).rank()==l
    checks+=1
print('PASS',checks,'deterministic path/frame/Dirichlet/multidimensional/Krylov checks')
