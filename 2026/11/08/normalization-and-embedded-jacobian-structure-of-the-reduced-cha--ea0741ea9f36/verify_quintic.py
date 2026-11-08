"""Exact characteristic-two verification of the monic-quintic discriminant model.
Uses polynomial arithmetic over GF(2) with SymPy, and direct field enumeration over GF(4).
"""
import sympy as s
from itertools import product
x,a,b,c,d,e,U,V,R=s.symbols('x a b c d e U V R')
f=x**5+a*x**4+b*x**3+c*x**2+d*x+e
Delta=s.Poly(s.discriminant(f,x),a,b,c,d,e,modulus=2).as_expr()
h=a*a*d*d+a*b*b*e+a*b*c*d+b*c*e+c*c*d+e*e
sq=s.Poly(h*h,a,b,c,d,e,modulus=2).as_expr()
assert s.Poly(Delta-sq,a,b,c,d,e,modulus=2).is_zero
coord=s.Poly(h.subs({c:V+a*b,e:U+a*d})-(U*U+b*U*V+d*V*V),a,b,d,U,V,modulus=2)
assert coord.is_zero
subst={d:R*R+b*R,U:R*V}
assert s.Poly((U*U+b*U*V+d*V*V).subs(subst),a,b,R,V,modulus=2).is_zero
assert s.Poly((R*R+b*R+d).subs(subst),a,b,R,V,modulus=2).is_zero
# Formal partials and Jacobian ideal in the new triangular chart.
Q=U*U+b*U*V+d*V*V
partial=[s.Poly(s.diff(Q,t),a,b,d,U,V,modulus=2).as_expr() for t in [a,b,d,U,V]]
assert partial==[0,U*V,V**2,b*V,b*U]
# GF(4)=GF(2)[w]/(w^2+w+1), bits representation 0,1,w,w+1.
def plus(x,y):return x^y
def mul(x,y):
 v=0
 for j in range(2):
  if (y>>j)&1:v^=x<<j
 if v&8:v^=(0b1110) # w^3 = w^2+w =1 => reduction of w^3 by shifted w^2+w+1
 if v&4:v^=0b111
 return v
assert all(mul(t,1)==t for t in range(4))
assert mul(2,2)==3 and mul(2,3)==1

def inv(y):
 if y==0:raise ZeroDivisionError
 return next(z for z in range(1,4) if mul(y,z)==1)
def strip(v):
 while v and not v[-1]:v.pop()
 return v
def rem(F,G):
 F=strip(F[:]);G=strip(G[:]); assert G
 while len(F)>=len(G):
  coef=mul(F[-1],inv(G[-1]));k=len(F)-len(G)
  for j in range(len(G)):F[k+j]^=mul(coef,G[j])
  strip(F)
 return F
def gcd(F,G):
 F=strip(F[:]);G=strip(G[:]);
 while G:F,G=G,rem(F,G)
 return F
n_squarefree=n_singular=n_normal_params=n_image=0
for aa,bb,cc,dd,ee in product(range(4),repeat=5):
 uu=ee^mul(aa,dd); vv=cc^mul(aa,bb)
 H=mul(uu,uu)^mul(bb,mul(uu,vv))^mul(dd,mul(vv,vv))
 ff=[ee,dd,cc,bb,aa,1]
 der=[dd,0,bb,0,1]
 rep= len(gcd(ff,der))>1
 assert (H==0)==rep, (aa,bb,cc,dd,ee)
 if not rep: n_squarefree+=1
 sing=(uu==0 and vv==0)
 deriv=[mul(uu,vv),mul(vv,vv),mul(bb,vv),mul(bb,uu)]
 assert sing==(H==0 and not any(deriv))
 n_singular+=sing
 if H==0:n_image+=1
for aa,bb,rr,vv in product(range(4),repeat=4):
 dd=mul(rr,rr)^mul(bb,rr); uu=mul(rr,vv)
 H=mul(uu,uu)^mul(bb,mul(uu,vv))^mul(dd,mul(vv,vv))
 assert H==0
 n_normal_params+=1
print('DISCRIMINANT_SQUARE_IDENTITY_PASSED')
print('TRIANGULAR_COORDINATE_NORMAL_FORM_PASSED')
print('NORMALIZATION_INTEGRAL_IDENTITY_PASSED')
print('SINGULAR_LOCUS_JACOBIAN_IDENTITY_PASSED')
print('GF4_QUINTICS',4**5,'SQUAREFREE',n_squarefree,'DISCRIMINANT_POINTS',n_image,'SINGULAR_REDUCED_POINTS',n_singular)
print('GF4_NORMALIZATION_PARAMETERS',n_normal_params)
print('ALL_CHECKS_PASSED')
