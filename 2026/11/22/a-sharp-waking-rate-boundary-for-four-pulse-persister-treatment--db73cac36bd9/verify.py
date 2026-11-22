"""Reproducible algebraic and numerical checks for a two-state switched bacterial system.

Requires sympy and mpmath. Mathematical proof is in RESULT.md.
"""
from fractions import Fraction
import random
import sympy as sp
import mpmath as mp

A, b, d, g, z, u, v = sp.symbols('a b d g z u v', positive=True)
On = sp.Matrix([[-A-d,z],[A,-z]])
Off = sp.Matrix([[g-A,b],[A,-b]])
q = -g*z*z+(b*(g-d)+(g-A)*(d+g))*z+b*(d*(b+A+d+g)+A*g)
assert sp.expand((On*Off-Off*On).det()-A*q)==0
X=sp.Matrix(sp.symbols('x0:4')).reshape(2,2)
Y=sp.Matrix(sp.symbols('y0:4')).reshape(2,2)
assert sp.expand(sp.trace(X*X*Y*Y)-sp.trace(X*Y*X*Y)-(X*Y-Y*X).det())==0
phi=(1+sp.sqrt(5))/2
w=sp.Matrix([phi,1]); B1=Off.subs({A:1,b:1,d:1,g:1})
A1=On.subs({A:1,d:1,z:sp.sqrt(5)})
assert all(sp.simplify(t)==0 for t in B1*w-(sp.sqrt(5)-1)*w/2)
assert all(sp.simplify(t)==0 for t in A1*w+(sp.sqrt(5)-1)*w/2)
assert sp.simplify(q.subs({A:1,b:1,d:1,g:1})-(5-z*z))==0

mp.mp.dps=65
rng=random.Random(20231115)

def eigenplus(M):
    tr=M[0,0]+M[1,1]
    det=mp.det(M)
    return (tr+mp.sqrt(tr*tr-4*det))/2

def phases(a,b,d,g,z,u,v):
    on=mp.matrix([[-a-d,z],[a,-z]])
    off=mp.matrix([[g-a,b],[a,-b]])
    x=mp.expm(u*on); y=mp.expm(v*off)
    group=x*x*y*y; altern=x*y*x*y
    return eigenplus(group),eigenplus(altern),(group[0,0]+group[1,1])-(altern[0,0]+altern[1,1]),mp.det(x*y-y*x)

for k in range(36):
    a,b0,d0,g0=[mp.mpf(rng.randrange(1,21))/rng.randrange(1,8) for _ in range(4)]
    u0,v0=[mp.mpf(rng.randrange(1,11))/rng.randrange(1,8) for _ in range(2)]
    lam=(g0-a-b0+mp.sqrt((g0-a-b0)**2+4*g0*b0))/2
    critical=b0+(1+d0/g0)*lam
    assert b0<critical<b0+d0+g0
    for fac in [mp.mpf('0.4'),mp.mpf('0.9'),mp.mpf('1.1'),mp.mpf('2')]:
        z0=critical*fac
        rg,rt,trgap,detcomm=phases(a,b0,d0,g0,z0,u0,v0)
        assert abs(trgap-detcomm)<mp.mpf('1e-47')*max(1,abs(trgap),abs(detcomm))
        assert (rg>rt)==(z0<critical)
    # At the resonance every finite positive word has the predicted Perron root.
    on=mp.matrix([[-a-d0,critical],[a,-critical]])
    off=mp.matrix([[g0-a,b0],[a,-b0]])
    product=mp.eye(2); ton=mp.mpf('0');toff=mp.mpf('0')
    for ison,duration in [(True,mp.mpf('0.2')),(False,mp.mpf('0.7')),
                           (False,mp.mpf('0.13')),(True,mp.mpf('0.4')),
                           (False,mp.mpf('0.31'))]:
        product=mp.expm(duration*(on if ison else off))*product
        if ison: ton+=duration
        else: toff+=duration
    predicted=mp.exp((lam/g0)*(g0*toff-d0*ton))
    assert abs(eigenplus(product)/predicted-1)<mp.mpf('1e-50')

for zz,uu,vv,kappa,group_larger in [
    (1,1,1,mp.mpf('0.05'),True),
    (3,mp.mpf('0.5'),2,mp.mpf('0.37'),False)]:
    rg,rt,_,_=phases(mp.mpf(1),mp.mpf(1),mp.mpf(1),mp.mpf(1),mp.mpf(zz),mp.mpf(uu),mp.mpf(vv))
    factor=mp.exp(-2*kappa*(uu+vv))
    if group_larger:
        assert rg*factor>1 and rt*factor<1
    else:
        assert rg*factor<1 and rt*factor>1
    print('z',zz,'grouped Floquet',mp.nstr(rg*factor,20),'alternating Floquet',mp.nstr(rt*factor,20))
print('PASS: exact algebra, 144 strict phase tests, 36 all-order resonance tests, 2 stability witnesses')
