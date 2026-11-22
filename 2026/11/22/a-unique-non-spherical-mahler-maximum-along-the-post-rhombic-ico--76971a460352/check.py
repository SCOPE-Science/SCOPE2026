#!/usr/bin/env python3
"""Exact sign brackets and numerical display for a radial icosahedral volume product.
Standard library only. The mathematical proof is in RESULT.md.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext

# Literal integer square comparison for rational enclosures of sqrt(5).
lo=Q(2236067977,1000000000)
hi=Q(2236067978,1000000000)
assert lo*lo < 5 < hi*hi
# Since b=1-1/sqrt(5), bounds reverse under inversion.
blo=1-Q(1,1)/lo
bhi=1-Q(1,1)/hi
assert blo > 0 and bhi < Q(4,7)
q=lambda s,b:Q(1)-9*s*s+6*b*s*s*s
assert q(Q(1,3),blo)>0
assert q(Q(9,25),bhi)<0
# Square identity: (1-9b/25)^2-h^2=(958-386sqrt(5))/9375 >0.
assert Q(958)-386*hi>0
# h<1-9b/25, hence the optimizer is beyond the unit-radius configuration.
with localcontext() as ctx:
 ctx.prec=70
 r=Decimal(5).sqrt()
 b=1-1/r
 h=((5+2*r)/15).sqrt()
 S_lo=Decimal(1)/3
 S_hi=Decimal(9)/25
 def f(s):return 1-9*s*s+6*b*s*s*s
 for _ in range(280):
  m=(S_lo+S_hi)/2
  if f(m)>0:S_lo=m
  else:S_hi=m
 s=(S_lo+S_hi)/2
 tau=(1-b*s)/h
 tau1=(1-h)/b
 import math
 sin72=Decimal(str(math.sin(2*math.pi/5)))
 Vi=Decimal(8)/3*sin72
 Vpolar=10*(1-h*h)/(h*h)*sin72
 B=Vi*Vpolar
 F=lambda z:(1-3*b*z**3)/(1-b*z)
 vmax=B*F(s)
 vunit=B*F(tau1)
 assert Decimal(1)/3<s<Decimal(9)/25
 assert tau>1
 assert vmax>vunit
 print('certified rational signs and ordering: PASS')
 print('s*:',s)
 print('tau*:',tau)
 print('volume-product maximum:',vmax)
 print('volume product at tau=1:',vunit)
 print('strict gap:',vmax-vunit)
