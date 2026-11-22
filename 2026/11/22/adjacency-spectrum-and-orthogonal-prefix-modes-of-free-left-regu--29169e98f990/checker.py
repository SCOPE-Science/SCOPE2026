#!/usr/bin/env python3
"""Independent finite tests for a commuting graph spectral factorization."""
from itertools import permutations
from math import factorial
import sympy as sp
z=sp.symbols('z')

def words(n):
    return [()] + [w for k in range(1,n+1) for w in permutations(range(n),k)]

def product(u,v):
    return u+tuple(a for a in v if a not in u)

def H(k):
    return sp.Matrix(k+1,k+1,lambda i,j: (0 if i==j else (1 if i>j else factorial(k-i)//factorial(k-j))))

def factorized(n):
    p=sp.Poly(1,z)
    for k in range(1,n):
        p*=sp.Poly(H(k).charpoly(z).as_expr(),z)**(k*factorial(n)//factorial(k+1))
    p*=sp.Poly(H(n).charpoly(z).as_expr(),z)
    return p

def test(n):
    W=words(n)
    for u in W:
        for v in W:
            lhs=(product(u,v)==product(v,u))
            rhs=(u==v[:len(u)] or v==u[:len(v)])
            assert lhs==rhs, ('product/prefix mismatch',n,u,v)
    A=sp.Matrix(len(W),len(W),lambda i,j: int(i!=j and (product(W[i],W[j])==product(W[j],W[i]))))
    actual=sp.Poly(A.charpoly(z).as_expr(),z)
    pred=factorized(n)
    assert actual==pred,(n,actual,pred)
    assert actual.LC()==1
    # standard commuting graph: remove the central identity, compare n identical components
    if n>=2:
        noncen=sp.Poly(A[1:,1:].charpoly(z).as_expr(),z)
        assert noncen==factorized(n-1)**n
    m=0; t=actual
    while t.eval(-1)==0:
        t=t.exquo(sp.Poly(z+1,z)); m+=1
    assert m==factorial(n), ('minus-one multiplicity',n,m)
    print('DIRECT_ALL_PRODUCTS_AND_FULL_CHARPOLY_PASS n=%d vertices=%d'%(n,len(W)))

for n in range(1,5): test(n)
for k in range(1,11):
    p=H(k).charpoly(z).as_expr()
    assert p.subs(z,-1)==0
    assert sp.diff(p,z).subs(z,-1)==-2*factorial(k-1)
    M=H(k)+sp.eye(k+1)
    assert M[:k,:k].det()==(-1)**(k-1)*factorial(k-1)
print('RADIAL_MINUS_ONE_SIMPLE_AND_MINOR_PASS k=1..10')
for n in range(1,16):
    e=1+sum(k*factorial(n)//factorial(k+1) for k in range(1,n))
    assert e==factorial(n)
    deg=(n+1)+sum((k+1)*k*factorial(n)//factorial(k+1) for k in range(1,n))
    size=sum(factorial(n)//factorial(n-d) for d in range(n+1))
    assert deg==size
print('DEGREE_AND_MULTIPLICITY_IDENTITIES_PASS n=1..15')
