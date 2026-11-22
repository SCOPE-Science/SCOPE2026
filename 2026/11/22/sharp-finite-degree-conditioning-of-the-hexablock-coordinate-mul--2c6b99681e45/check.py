"""Numerical sanity checks for exact finite-degree hexablock compression formulas.
The theorem and equality cases are proved analytically in RESULT.md."""
from math import sin, pi
from scipy.special import roots_jacobi
import numpy as np
checks=0
for n in range(0,41):
    eigs=[]
    for i in range(n+1):
        for b in range(n-i+1):
            for c in range(n-i-b+1):
                m=min(b,c); delta=abs(b-c)
                z=roots_jacobi(m+1,delta-.5,i-.5)[0]
                eigs.extend((1+z)/2)
    val=min(eigs)
    expected=sin(pi/(2*(n+2)))**2
    assert abs(val-expected)<2e-12,(n,val,expected)
    checks+=1
    at=sum(abs(v-expected)<2e-12 for v in eigs)
    assert at==(1 if n%2==0 else 2),(n,at)
    checks+=1
    # Tridiagonal eigenvector and characteristic equation.
    theta=pi/(n+2)
    u=np.sin(np.arange(1,n+2)*theta)
    T=np.diag(np.full(n+1,0.5))
    if n:
        T+=np.diag(np.full(n,-.25),1)+np.diag(np.full(n,-.25),-1)
    assert np.linalg.norm(T@u-expected*u)<1e-12
    checks+=1
print('HEXABLOCK_FINITE_CUTOFF_DIAGNOSTIC_OK',checks)
