#!/usr/bin/env python3
"""Exact transfer verification for primitive-two majority states on a cycle with one leaf.
All computations use integer matrices and exact polynomial arithmetic.
"""
import itertools
import sympy as sp

states=list(itertools.product((0,1),repeat=2))
pairs=list(itertools.product(states,repeat=2))
index={v:i for i,v in enumerate(pairs)}

def maj(a,b,c):
    return a if a==b else c

def matrix(leaf):
    A=sp.zeros(16)
    for row,(left,center) in enumerate(pairs):
        l0,l1=left
        a,b=center
        for right in states:
            r0,r1=right
            if leaf:
                okay=(b==maj(l0,r0,b) and a==maj(l1,r1,a))
            else:
                okay=(b==maj(l0,r0,a) and a==maj(l1,r1,b))
            if okay:A[row,index[(center,right)]]=1
    return A

A=matrix(False); B=matrix(True)
x=sp.symbols('x')
p=(x-1)*(x+1)*(x*x-x-1)*(x*x-x+1)
identity=sp.zeros(16)
for (k,),v in sp.Poly(sp.expand(p),x).terms():
    identity+=v*A**k
assert (A*A*identity).is_zero_matrix
print('EXACT_MATRIX_IDENTITY: A^2 (A^6 -2A^5 +2A^3 -2A^2 +I) = 0')
print('charpoly(A):',sp.factor(A.charpoly(x).as_expr()))
print('charpoly(B):',sp.factor(B.charpoly(x).as_expr()))

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def C(n):return [4,2,2,-2,0,0][n%6]

def cos6(n):return [2,1,-1,-2,-1,1][n%6]

# B is inserted at exactly one cycle site and A at all others.
for n in range(3,9):
    twostep=(B*A**(n-1)).trace()
    lucas=fib(n-1)+fib(n+1)
    fixed=lucas+cos6(n)
    expected=fixed+2*fib(n-2)+C(n)
    assert twostep==expected,(n,twostep,expected)
    print(f'n={n}: Fix(M^2)={twostep}, Fix(M)={fixed}, primitive2={twostep-fixed}')

# A^2 p(A)=0 implies the same order-six recurrence for all
# traces tr(B A^(n-1)), n>=3, proving extension of the six seeds.
# The proposed explicit sequence is a sum of terms with roots among
# {phi, -1/phi, e^{+/-i*pi/3}, 1, -1}, all roots of p(x).
print('SYMBOLIC_CHECK_PASS')
