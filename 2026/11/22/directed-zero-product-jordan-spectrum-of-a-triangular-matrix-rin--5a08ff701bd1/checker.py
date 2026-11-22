"""Standalone verification of the directed zero-product graph for UT_2(F_q).
Run: python checker.py (requires sympy >=1.12). This tests finite cases only.
"""
import sympy as sp


def add(x,y,q):
    if q==4: return x^y
    return (x+y)%q

def mul(x,y,q):
    if q==4:
        p=0
        for i in range(2):
            for j in range(2):
                if ((x>>i)&1) and ((y>>j)&1):p ^= 1<<(i+j)
        if p&8:p^=0b1100 # x^3=x^2+x=1 (mod x^2+x+1), but x,y <4 gives max x^2, no bit3
        if p&4:p^=0b111 # x^2=x+1
        return p
    return (x*y)%q

def zero_pair(x,y,q):
    a,b,c=x;d,e,f=y
    return mul(a,d,q)==0 and add(mul(a,e,q),mul(b,f,q),q)==0 and mul(c,f,q)==0

def graph(q):
    V=[(a,b,c) for a in range(q) for b in range(q) for c in range(q) if (a,b,c)!=(0,0,0) and (a==0 or c==0)]
    A=sp.Matrix([[int(x!=y and zero_pair(x,y,q)) for y in V] for x in V])
    return V,A

def expected_poly(q,z):
    k=q-1
    cubic=z**3-(q-2)*z**2-q*k*k*(z+1)
    return sp.expand(z**(2*q*k-2)*(z+1)**(q-2)*cubic)

for q in (2,3,4,5):
    V,A=graph(q)
    N=len(V)
    assert N==(2*q+1)*(q-1)
    actual=sp.expand(A.charpoly().as_expr().subs(A.charpoly().gen,sp.Symbol('z')))
    assert sp.expand(actual-expected_poly(q,sp.Symbol('z')))==0
    assert A.rank()==2*q
    zero_nullity=N-2*q
    assert N-A.nullspace().__len__()==2*q
    # Zero-eigenvalue Jordan 2-block count equals dim(kernel A^2)-dim(kernel A),
    # since nonzero-eigenvalue blocks have invertible A.
    null_A2=N-(A*A).rank()
    assert null_A2-zero_nullity==q-1
    # -1 multiplicity from eigenspace C-mean-zero
    assert (A+sp.eye(N)).nullspace().__len__()==q-2
    print('PASS',{'q':q,'vertices':N,'rank':A.rank(),'zero_jordan2':null_A2-zero_nullity,'minus_one':q-2,'charpoly':'verified'})
print('All tests passed.')
