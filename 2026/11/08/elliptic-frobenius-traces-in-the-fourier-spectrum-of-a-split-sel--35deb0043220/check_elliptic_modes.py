#!/usr/bin/env python3
"""Find exact smooth (2,2) examples with q+2 rational points over small primes."""
from itertools import product
from random import Random
import sympy as sp
r=Random(917)

def calc(q,record=False):
    x=sp.symbols('x')
    P1=[(1,t) for t in range(q)]+[(0,1)]
    for it in range(50000):
        z=[r.randrange(q) for _ in range(9)]
        if not any(z):continue
        A=z[0:3];B=z[3:6];C=z[6:9]
        def Q(K,s,t):return (K[0]*s*s+K[1]*s*t+K[2]*t*t)%q
        cnt=sum((Q(A,s,t)*u*u+Q(B,s,t)*u*v+Q(C,s,t)*v*v)%q==0 for s,t in P1 for u,v in P1)
        if cnt!=q+2:continue
        av=sum(A[j]*x**j for j in range(3))
        bv=sum(B[j]*x**j for j in range(3))
        cv=sum(C[j]*x**j for j in range(3))
        delta=sp.Poly(bv*bv-4*av*cv,x,modulus=q)
        if delta.is_zero or delta.degree()<3:continue
        if sp.gcd(delta,delta.diff()).degree()!=0:continue
        print('q',q,'coef A,B,C',A,B,C,'rational_points',cnt,'delta',str(delta.as_expr()),'squarefree',True,'attempt',it)
        return
    raise RuntimeError(q)
for q in [3,5,7]:calc(q)
print('ALL_SMOOTH_GENUS_ONE_EXAMPLES_VERIFIED')
