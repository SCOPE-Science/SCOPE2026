#!/usr/bin/env python3
"""Independent symbolic verification of genus-four hyperelliptic strata in characteristic five."""
import sympy as S
from collections import Counter
x,a,b=S.symbols('x a b')
f=x**10+x**7+a*x**4+b*x
coeff=S.Poly(S.expand(f**2), x)
B=S.Matrix([[coeff.nth(5*i-j) for j in range(1,5)] for i in range(1,5)])
w=a*a+2*b;u=2*a+1;v=2*a+2*b
expected=S.Matrix([[0,0,b*b,0],[0,w,0,0],[u,0,0,v],[0,0,2,0]])
assert B==expected, (B,expected)
# Discriminant test: f=x*g(x^3), g(T)=T^3+T^2+a*T+b.
t=S.symbols('t');g=t**3+t**2+a*t+b
D=S.discriminant(g,t)
assert S.Poly(D-(a*a+a**3+b+3*b*b+3*a*b),a,b,modulus=5).is_zero
# Cartier is 1/5-linear with coordinate matrix (c_{5i-j})^{1/5}.
# The composite C^2 has coordinate matrix (B^(5)*B)^(1/25),
# so the 2x2 stable block is governed by the polynomial below.
lam=u**5*b*b+2*v**5
assert S.Poly(lam-(2*a**5*b*b+b*b-a**5-b**5),a,b,modulus=5).is_zero
lam_on_w=S.Poly(S.expand(lam.subs(b,2*a*a)),a,modulus=5)
assert lam_on_w==S.Poly(-2*a**4*(a+1)*(a-2)**5,a,modulus=5)
D_on_w=S.Poly(S.expand(D.subs(b,2*a*a)),a,modulus=5)
assert D_on_w==S.Poly(2*a*a*(a-2)**2,a,modulus=5)
assert (int(lam.subs({a:4,b:2}))%5)==0
assert (int(D.subs({a:4,b:2}))%5)!=0
assert (int(w.subs({a:4,b:2}))%5)==0
# The rank-one Cartier block would require u=v=0: a=2,b=3,
# which is singular since the cubic g has discriminant zero.
assert int(u.subs(a,2))%5==0 and int(v.subs({a:2,b:3}))%5==0
assert int(D.subs({a:2,b:3}))%5==0
counts=Counter(); reps={}
for aa in range(5):
 for bb in range(5):
  dd=int(D.subs({a:aa,b:bb}))%5
  if bb==0 or dd==0: continue
  ww=int(w.subs({a:aa,b:bb}))%5
  ll=int(lam.subs({a:aa,b:bb}))%5
  prank=(2 if ll else 0)+(1 if ww else 0)
  anumber=2 if not ww else 1
  counts[(prank,anumber)]+=1
  reps.setdefault(prank,(aa,bb))
assert counts == Counter({(0,2):1,(1,1):2,(2,2):2,(3,1):12}),counts
assert reps=={1:(0,1),3:(0,2),2:(1,2),0:(4,2)},reps
print('GENUS4_P5_CARTIER_PASS',len(counts),sum(counts.values()), sorted(counts.items()),reps)
