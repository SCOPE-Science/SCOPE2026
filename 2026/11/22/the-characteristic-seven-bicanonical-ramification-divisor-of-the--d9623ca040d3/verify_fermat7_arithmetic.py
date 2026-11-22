#!/usr/bin/env python3
"""Independent finite-field enumeration of ramification support over F7 and F49."""
from itertools import product
p=7
# t^2=3, irreducible over F7.
E=[(a,b) for a in range(p) for b in range(p)]
O=(1,0);Z=(0,0)
def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def mul(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def powf(x,n):
 r=O
 while n:
  if n&1:r=mul(r,x)
  x=mul(x,x);n//=2
 return r
def neg(x):return ((-x[0])%p,(-x[1])%p)
def is_curve(x,y):return add(add(powf(x,4),powf(y,4)),O)==Z

def simple_points(field):
 return {(x,y) for x,y in product(field,repeat=2)
         if x!=Z and y!=Z and is_curve(x,y)
         and powf(x,24)==O and powf(y,24)==O}
def hyper_points(field):
 # Projective points: affine x=0 or y=0, plus points at infinity (1:y:0).
 affine={(x,y, O) for x,y in product(field,repeat=2)
         if is_curve(x,y) and (x==Z or y==Z)}
 infinite={(O,y,Z) for y in field if add(O,powf(y,4))==Z}
 return affine|infinite
F7=[(a,0) for a in range(7)]
s7=simple_points(F7);s49=simple_points(E)
h7=hyper_points(F7);h49=hyper_points(E)
assert len(s7)==8 and len(s49)==80
assert len(h7)==0 and len(h49)==12
# GF(49) contains all fourth roots of GF(7)^*, and these are all geometric
# supports by the explicit equations; no higher-degree supports can occur.
assert all(sum(powf(v,4)==(u,0) for v in E)==4 for u in range(1,7))
assert len({v for v in E if powf(v,4)==O})==4
assert len(s49)+3*len(h49)==116
# Every Frobenius orbit in the reduced 92-point support has length one or two.
assert len(s7)+len(h7)==8
assert (len(s49)-len(s7))//2+(len(h49)-len(h7))//2==42
assert sum(is_curve(x,y) for x in F7 for y in F7)+sum(add(O,powf(y,4))==Z for y in F7)==8
assert sum(is_curve(x,y) for x in E for y in E)+sum(add(O,powf(y,4))==Z for y in E)==92
print('FERMAT7_ARITHMETIC_COUNTS_OK')
