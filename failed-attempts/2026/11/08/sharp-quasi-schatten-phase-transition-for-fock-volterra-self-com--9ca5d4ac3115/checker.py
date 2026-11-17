#!/usr/bin/env python3
"""Standalone finite tests of Fock Volterra self-commutator coefficient formulae.

Run: python3 checker.py. Uses the Python standard library only.
Finite tests corroborate identities; they are not proofs of infinite assertions.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

# Square moduli of the diagonal and off-diagonal coefficients, with |a|^2=A,
# |b|^2=B, and |a*conj(b)|^2=A*B. Exact fractions for nonnegative indices.
def d(n, A, B):
    if n == 0:
        return 2*A+B
    return F(8*A,n*(n+2))-F(B,n*(n+1))

def t2(n, A, B):
    if n == 0:
        return A*B
    return F(4*A*B,(n+2)**2*(n+1))

# Independent products from the two-diagonal operator: calculate finite-
# support Gram matrix elements without the claimed closed forms.
def weight(n,a,b):
    return ((n+1,b/sqrt(n+1)), (n+2,2*a*sqrt((n+1)/(n+2))))

def gram_at(i,j,a,b,adjoint_first):
    if adjoint_first:  # (V*V)_{j,i}
        wi=dict(weight(i,a,b)); wj=dict(weight(j,a,b))
        return sum(wi[k]*wj[k].conjugate() for k in wi.keys() & wj.keys())
    # (VV*)_{j,i}; the rows of V at output i,j
    wi={m:v for m in range(max(0,i-2),i+1) for k,v in weight(m,a,b) if k==i}
    wj={m:v for m in range(max(0,j-2),j+1) for k,v in weight(m,a,b) if k==j}
    return sum(wj[k]*wi[k].conjugate() for k in wi.keys() & wj.keys())

for a,b in [(1+2j,-2+3j), (0,1+2j), (3-1j,0),(0,0),(2+0j,3+0j)]:
    A=round(abs(a)**2); B=round(abs(b)**2)
    for n in range(70):
        actual = gram_at(n,n,a,b,True)-gram_at(n,n,a,b,False)
        assert abs(actual-float(d(n,A,B)))<2e-12, (n,a,b,actual,d(n,A,B))
        checks+=1
        off=gram_at(n,n+1,a,b,True)-gram_at(n,n+1,a,b,False)
        expected=(a*b.conjugate() if n==0 else -2*a*b.conjugate()/((n+2)*sqrt(n+1)))
        assert abs(off-expected)<2e-12, (n,a,b,off,expected)
        checks+=1
        assert abs(abs(off)**2-float(t2(n,A,B)))<4e-12
        checks+=1

for A,B in [(1,0),(0,1),(1,1),(9,25)]:
    for N in range(1,500):
        partial=sum((d(n,A,B) for n in range(N+1)), F(0))
        edge=4*A*F(N+1,N+2)+4*A*F(N,N+1)+F(B,N+1)
        assert partial == edge, (A,B,N,partial,edge)
        checks+=1
        for n in [1,2,3,7,11,23,49,99,125]:
            assert t2(n,A,B) == F(4*A*B,(n+2)**2*(n+1))
            checks+=1

print('EXACT_FOCK_VOLTERRA_COMMUTATOR_OK', checks)
