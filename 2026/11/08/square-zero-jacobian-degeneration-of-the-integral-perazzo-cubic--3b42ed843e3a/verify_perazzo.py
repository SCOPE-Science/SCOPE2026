#!/usr/bin/env python3
"""Exact verification of Jacobian scheme identities for an integral Perazzo cubic."""
from itertools import product
from math import comb
import sympy as s

x0,x1,x2,u,v=s.symbols('x0 x1 x2 u v')
z=(x0,x1,x2,u,v)
f=x0*u*u+x1*u*v+x2*v*v
grad=[s.diff(f,t) for t in z]
assert grad==[u**2,u*v,v**2,2*u*x0+v*x1,u*x1+2*v*x2]
L=s.Matrix([[2*x0,x1],[x1,2*x2]])
assert s.expand(L.det())==4*x0*x2-x1*x1

def monomials(total,n):
 if n==1:
  yield (total,)
 else:
  for i in range(total+1):
   for q in monomials(total-i,n-1):yield (i,)+q

def check_mod(p):
 G=s.groebner(grad+[f],*z,order='grevlex',modulus=p)
 lead=[tuple(q.LM(order='grevlex')) for q in G.polys]
 def hf(m):
  return sum(not any(all(e>=k for e,k in zip(exp,lm)) for lm in lead) for exp in monomials(m,5))
 actual=[hf(m) for m in range(9)]
 expect=[comb(m+2,2)+2*m for m in range(9)]
 assert actual==expect,(p,actual,expect,lead)
 if p==2:
  assert s.groebner([u*u,u*v,v*v,x1*u,x1*v],*z,order='grevlex',modulus=2)==G
  assert [s.Poly(q,*z,modulus=2).as_expr() for q in grad]==[u*u,u*v,v*v,v*x1,u*x1]
  assert s.Poly(L.det(),*z,modulus=2).as_expr()==x1*x1
 else:
  assert s.Poly(L.det(),*z,modulus=p).as_expr()==s.Poly(4*x0*x2-x1*x1,*z,modulus=p).as_expr()
 print('characteristic',p,'GROEBNER_OK','Hilbert function degrees 0..8:',','.join(map(str,actual)),'initial_generator_count',len(lead))

for prime in [2,3,5,7,11]:check_mod(prime)
print('EXACT_JACOBIAN_AND_HILBERT_CHECKS_OK')
