"""Exact verification of a multi-reversal network-diffusion construction.

Run: python corridor_verifier.py
Requires: sympy, numpy. The mathematical proof is independent of these checks.
"""

import sympy as sp
import numpy as np

J=sp.Matrix([[1,-5],[sp.Rational(39,4),-40]])
D=sp.diag(sp.Rational(1,10),10)
x=sp.symbols('x')
assert sp.simplify((J-x*D).det()-(x-sp.Rational(5,2))*(x-sp.Rational(7,2)))==0
assert (J-x*D).trace() == -39-sp.Rational(101,10)*x


def graph(k, r, s):
    """A central hub, k triads, r extra leaves; s sequential corridor additions."""
    n=3*k+r+1
    edges=[(0,j) for j in range(1,n)]
    for i in range(k):
        a,b,c=3*i+1,3*i+2,3*i+3
        if s>=2*i+1: edges.append((a,b))
        if s>=2*i+2: edges.append((a,c))
    return n,edges


def laplacian(n,edges):
    L=sp.zeros(n)
    for a,b in edges:
        L[a,a]+=1
        L[b,b]+=1
        L[a,b]-=1
        L[b,a]-=1
    return L


def expected(k,r,s):
    out=[0,3*k+r+1]+[1]*(k+r-1)
    for i in range(k):
        z=max(0,min(2,s-2*i))
        out.extend({0:[1,1],1:[1,3],2:[2,4]}[z])
    assert len(out)==3*k+r+1
    return sorted(out)


checks=0
full_checks=0
for k in range(1,5):
    for r in range(3):
        for s in range(2*k+1):
            n,edges=graph(k,r,s)
            L=laplacian(n,edges)
            actual=sp.Poly(L.charpoly(x).as_expr(),x)
            predicted=sp.Poly(sp.prod(x-t for t in expected(k,r,s)),x)
            assert actual==predicted, (k,r,s)
            numeric=sorted(np.linalg.eigvalsh(np.array(L,dtype=float)))
            assert max(abs(a-b) for a,b in zip(numeric,expected(k,r,s)))<1e-8
            unstable=sum(2.5<t<3.5 for t in expected(k,r,s))
            assert unstable==s%2
            checks+=1
            if k<=2:
                full=sp.kronecker_product(sp.eye(n),J)-sp.kronecker_product(L,D)
                eig=np.linalg.eigvals(np.array(full,dtype=float))
                assert (max(np.real(eig))>1e-10)==(s%2==1)
                full_checks+=1
print('PASS:',checks,'exact Laplacian characteristic polynomials;')
print('PASS:',full_checks,'independent full-Jacobian stability comparisons;')
print('PASS: modal Turing window (5/2, 7/2).')
