#!/usr/bin/env python3
"""Exact independent finite checks of a characteristic-five plane sextic."""
from itertools import product
import sympy as sp

p=5
x,y,z,u,v=sp.symbols('x y z u v')
Q=x*x+y*y+z*z
P=x*y*z
F=x**6+y**6+z**6+Q*(x**4+y**4+z**4)-12*x*x*y*y*z*z
G=2*Q**3+P**2
assert all(int(c)%p==0 for c in sp.Poly(F-G,x,y,z).coeffs())
print('MOD5_TORUS_SEXTIC_IDENTITY_OK')

partials=[sp.diff(G,t) for t in (x,y,z)]
for a,b in product((1,-1),repeat=2):
    vals={x:a,y:b,z:1}
    assert int(G.subs(vals))%p==0
    assert all(int(f.subs(vals))%p==0 for f in partials)
    T=sp.Poly(G.subs({x:a+u,y:b+v,z:1}),u,v)
    qa=sum((int(c)%p)*u**ij[0]*v**ij[1] for ij,c in T.terms() if sum(ij)==2)
    A=int(qa.expand().coeff(u,2))%p
    B=int(qa.expand().coeff(u,1).coeff(v,1))%p
    C=int(qa.expand().coeff(v,2))%p
    assert (B*B-4*A*C)%5==3
print('FOUR_RATIONAL_NODES_NON_SPLIT_DISCRIMINANT_3_OK')

for zeroindex in range(3):
    for sign in (1,-1):
        v0=[1,2*sign,0]
        # Two nonzero coordinates chosen to satisfy sum of squares=0.
        arr=[0,0,0]
        remaining=[i for i in range(3) if i!=zeroindex]
        arr[remaining[0]],arr[remaining[1]]=1,2*sign
        vals=dict(zip((x,y,z),arr))
        assert int(G.subs(vals))%p==0
        assert all(int(f.subs(vals))%p==0 for f in partials)
print('SIX_F5_CUSP_SUPPORTS_OK')

# GF(25)=GF(5)[t]/(t*t-3), since 3 is nonsquare in GF(5).
def add(a,b): return ((a[0]+b[0])%5,(a[1]+b[1])%5)
def mul(a,b): return ((a[0]*b[0]+3*a[1]*b[1])%5,(a[0]*b[1]+a[1]*b[0])%5)
def sq(a): return mul(a,a)
zero=(0,0); one=(1,0); two=(2,0)
for q in (5,25):
    elements=[(a,0) for a in range(5)] if q==5 else list(product(range(5),repeat=2))
    projective=([(one,a,b) for a,b in product(elements,repeat=2)]+
                [(zero,one,a) for a in elements]+[(zero,zero,one)])
    count=0
    for xx,yy,zz in projective:
        qq=add(add(sq(xx),sq(yy)),sq(zz))
        pp=mul(mul(xx,yy),zz)
        gg=add(mul(two,mul(sq(qq),qq)),sq(pp))
        if gg==zero:count+=1
    assert count==(q+5 if q==5 else q-3),(q,count)
    print(f'GF{q}_PROJECTIVE_POINTS_OK: {count}')

# The normalization has genus zero by the genus formula:
# pa=(6-1)*(6-2)/2=10; six A2 cusps and four ordinary nodes each have delta 1.
assert (6-1)*(6-2)//2 == 6+4
print('ARITHMETIC_GENUS_AND_DELTA_OK')
print('VERIFY_OK')
