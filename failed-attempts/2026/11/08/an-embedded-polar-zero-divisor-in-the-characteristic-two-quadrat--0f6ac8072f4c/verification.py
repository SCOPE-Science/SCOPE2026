#!/usr/bin/env python3
"""Exact symbolic verification of the binary quadratic resultant singular scheme in characteristic two."""
import sympy as S
from itertools import product

V=(a,b,c,d,e,f)=S.symbols('a b c d e f')
X=S.symbols('X')
F=a*X**2+b*X+c
G=d*X**2+e*X+f
R=S.expand(S.resultant(F,G,X))
P=a*f-c*d
Q=a*e-b*d
T=b*f-c*e

def reduced(z):
    return S.Poly(S.expand(z),*V,modulus=2).as_expr()

def zero(z):
    return S.Poly(S.expand(z),*V,modulus=2).is_zero

assert zero(R-(P**2-Q*T)), 'universal resultant identity'
partial=[reduced(S.diff(R,v)) for v in V]
expected=[e*T,e*P,e*Q,b*T,b*P,b*Q]
assert all(zero(u-v) for u,v in zip(partial,expected)), 'all six derivatives'

I=[P,Q,T]
H=[b,e,P]
jac=[R]+partial
product_generators=[u*v for u,v in product(I,H)]
# Bidirectional Groebner membership proves ideal equality, not just equal radicals.
Jgb=S.groebner([reduced(z) for z in jac], *V,order='grevlex',modulus=2)
Pgb=S.groebner([reduced(z) for z in product_generators], *V,order='grevlex',modulus=2)
assert all(zero(Jgb.reduce(reduced(z))[1]) for z in product_generators)
assert all(zero(Pgb.reduce(reduced(z))[1]) for z in jac)

# The dense affine chart a=1 gives the exact local equation and Jacobian.
t,x,y,r,s=S.symbols('t x y r s')
subs={a:1,b:y,c:x,d:t,e:s+t*y,f:r+t*x}
local=S.Poly(S.expand(R.subs(subs)),t,x,y,r,s,modulus=2).as_expr()
local_expected=r**2+y*r*s+x*s**2
assert S.Poly(local-local_expected,t,x,y,r,s,modulus=2).is_zero
local_partials=[S.Poly(S.diff(local,z),t,x,y,r,s,modulus=2).as_expr() for z in (t,x,y,r,s)]
local_ideal=[local]+local_partials
local_product=[r*y,s*y,r*r,r*s,s*s]
localgb=S.groebner(local_ideal,t,x,y,r,s,modulus=2)
local_prodgb=S.groebner(local_product,t,x,y,r,s,modulus=2)
assert all(S.Poly(localgb.reduce(z)[1],t,x,y,r,s,modulus=2).is_zero for z in local_product)
assert all(S.Poly(local_prodgb.reduce(z)[1],t,x,y,r,s,modulus=2).is_zero for z in local_ideal)

# Independently compute the monomial primary-intersection ideal by elimination.
zeta=S.symbols('zeta')
minor=[r,s]
fullsquare=[y*y,y*r,y*s,r*r,r*s,s*s]
blend=[zeta*u for u in minor]+[(1-zeta)*v for v in fullsquare]
intersection_gb=S.groebner(blend,zeta,y,r,s,order='lex',modulus=2)
elim=[v for v in intersection_gb.polys if zeta not in v.as_expr().free_symbols]
intersection_expected=S.groebner(local_product,y,r,s,modulus=2)
assert all(S.Poly(intersection_expected.reduce(h.as_expr())[1],y,r,s,modulus=2).is_zero for h in elim)
assert all(S.Poly(S.groebner([h.as_expr() for h in elim],y,r,s,modulus=2).reduce(u)[1],y,r,s,modulus=2).is_zero for u in local_product)

# The transverse fiber y=0 is k[r,s]/(r,s)^2, basis {1,r,s}.
zz=S.groebner([r*r,r*s,s*s],r,s,modulus=2)
assert all(S.Poly(zz.reduce(v)[1],r,s,modulus=2).is_zero for v in [r*r,r*s,s*s])
assert all(not S.Poly(zz.reduce(v)[1],r,s,modulus=2).is_zero for v in [S.Integer(1),r,s])

# Exhaust all 63 k-rational points of P^5 over F_2: singular support is rank-one Segre.
num_singular=num_rankone=0
for vec in product((0,1),repeat=6):
    if not any(vec): continue
    dic=dict(zip(V,vec))
    sing=(int(reduced(R).subs(dic))%2==0 and all(int(g.subs(dic))%2==0 for g in partial))
    rankone=all(int(reduced(h).subs(dic))%2==0 for h in I)
    assert sing==rankone, f'finite-field point mismatch {vec}'
    num_singular+=sing
    num_rankone+=rankone
assert num_singular==((2**2-1)*(2**3-1))==21
print('RESULTANT_IDENTITY_OK')
print('SIX_PARTIALS_OK')
print('GLOBAL_IDEAL_BIDIRECTIONAL_GROEBNER_OK')
print('LOCAL_MODEL_AND_JACOBIAN_OK')
print('LOCAL_PRIMARY_INTERSECTION_ELIMINATION_OK')
print('TRANSVERSE_LENGTH_THREE_BASIS_OK')
print('F2_PROJECTIVE_POINTS=63 SINGULAR_POINTS=21 SEGRE_POINTS=21')
print('ALL_CHECKS_PASSED')
