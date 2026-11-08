#!/usr/bin/env python3
"""Separate genus-two Hasse-Witt calculation, plus a GF(49) point census."""
import sympy as S
x,t=S.symbols('x t')
f=(x**3-t)**2-4
coeff=lambda j:S.Poly(S.Poly(S.expand(f**3),x).coeff_monomial(x**j),t,modulus=7).as_expr()
B=S.Matrix([[coeff(6),coeff(5)],[coeff(13),coeff(12)]])
assert B == S.diag(t**4-2*t**2-1,t**2+2)
assert S.Poly(B[0,0]-(t*t+2)*(t*t+3),t,modulus=7).is_zero
print('GENUS2_QUOTIENT_HASSE_PASS',B.tolist())
# GF49=F7[i], i^2=-1: points at infinity for D=w^2=(v^3-t)^2-4
p=7; elements=[(a,b) for a in range(p) for b in range(p)]
def add(v,w):return ((v[0]+w[0])%p,(v[1]+w[1])%p)
def neg(v):return ((-v[0])%p,(-v[1])%p)
def mul(v,w):return ((v[0]*w[0]-v[1]*w[1])%p,(v[0]*w[1]+v[1]*w[0])%p)
def power(v,n):
  r=(1,0)
  for i in range(n):r=mul(r,v)
  return r
squares={mul(v,v) for v in elements}
# for a square RHS there are two y except at zero
zero=(0,0); four=(4,0)
def count_D(t):
 count=2 # even-degree hyperelliptic model: two points at infinity (leading square)
 for v in elements:
  rhs=add(mul(add(power(v,3),neg(t)),add(power(v,3),neg(t))),neg(four))
  count += (1 if rhs==zero else 2 if rhs in squares else 0)
 return count
critical=(0,3) # t=3*i has t^2=-2
other=(1,0)
assert power(critical,2)==(5,0)
assert count_D(critical)%7 == 1 and count_D(other)%7 != 1
print('GF49_QUOTIENT_POINTCHECK_PASS', 'nonordinary',count_D(critical),'ordinary',count_D(other))
