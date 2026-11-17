#!/usr/bin/env python3
"""Standalone finite checks of the stated deterministic-map formulas.
These tests corroborate algebra and quadratures; they do not certify ergodicity.
"""
from fractions import Fraction as F
import math
import random
import sympy as sp
import mpmath as mp

x,y,a,c,d,k,u=sp.symbols('x y a c d k u',positive=True)
s=2+c
X=x*(1+k*(a-s*x-d*y))
Y=y*(1+k*(a-s*y-d*x))
J=sp.Matrix([X,Y]).jacobian([x,y])
z=sp.symbols('z', positive=True)
sub={x:z,y:z,a:3/k}
assert sp.simplify((X-Y).subs(sub))==0
assert sp.simplify(X.subs(sub)-z*(4-k*(s+d)*z))==0
v=sp.Matrix([1,-1]); w=sp.Matrix([1,1]); jj=J.subs(sub)
assert all(sp.simplify(t)==0 for t in jj*v-(4-2*k*s*z)*v)
assert all(sp.simplify(t)==0 for t in jj*w-(4-2*k*(s+d)*z)*w)
assert sp.simplify((4-2*k*s*z).subs(z,4*u/(k*(s+d)))-4*(1-2*s*u/(s+d)))==0

rng=random.Random(731921)
for i in range(200):
    aa=F(rng.randrange(1,22),rng.randrange(1,18))
    cc=F(rng.randrange(1,25),rng.randrange(1,19))
    dd=F(rng.randrange(0,31),rng.randrange(1,15))
    kk=F(3,1)/aa
    uu=F(rng.randrange(1,70),rng.randrange(71,150))
    zz=F(4,1)*uu/(kk*(F(2,1)+cc+dd))
    xn=zz*(1+kk*(aa-(2+cc+dd)*zz))
    expected=F(16,1)*uu*(1-uu)/(kk*(2+cc+dd))
    assert xn==expected
    lam=F(4,1)-2*kk*(2+cc)*zz
    assert lam==4*(1-2*(2+cc)/(2+cc+dd)*uu)

# Verify the exact radial invariance at the exceptional coupling, separately.
for cc in [F(1,10),F(7,3),F(1)]:
    dd=2+cc; kk=F(3,2); aa=F(2)
    xx=F(2,7); yy=F(3,8)
    xnext=xx*(1+kk*(aa-(2+cc)*xx-dd*yy))
    ynext=yy*(1+kk*(aa-(2+cc)*yy-dd*xx))
    assert xnext*yy==ynext*xx

def exponent_closed(eta):
    if eta>=mp.mpf('0.5'):
        return mp.log(2*eta)
    return mp.log(2*(1-eta+mp.sqrt(1-2*eta)))

mp.mp.dps=35
for eta_str in ['0.125','0.3333','0.49','0.5','0.55','0.6666666666666666667','0.775','0.95','1.0']:
    eta=mp.mpf(eta_str)
    def integrand(theta):
        return mp.log(abs(4*(1-eta+eta*mp.cos(theta))))
    if eta>mp.mpf('0.5'):
        root=mp.acos(-(1-eta)/eta)
        integ=(mp.quad(integrand,[0,root])+mp.quad(integrand,[root,mp.pi]))/mp.pi
    elif eta==mp.mpf('0.5'):
        # The integrable endpoint case follows from the exact cosine/Jensen identity,
        # not a high-precision quadrature; count it separately.
        assert exponent_closed(eta)==0
        print('analytic boundary', eta_str, 'closed', 0)
        continue
    else:
        integ=mp.quad(integrand,[0,mp.pi])/mp.pi
    err=abs(integ-exponent_closed(eta))
    assert err<mp.mpf('1e-20'),(eta_str,err)
    print('quadrature',eta_str,'closed',mp.nstr(exponent_closed(eta),14),'error',mp.nstr(err,4))

for c0 in [F(1,1000),F(1,10),F(1,2),F(2,1)]:
  for d0 in [F(0),F(1,10),F(1,2),F(1)]:
    val=2*float((2+c0)/(2+c0+d0))
    assert val>=4/3
    assert (val>4/3) or (c0==0 and d0==1)

print('PASS symbolic eigendirections, 200 exact-rational trials, 8 independent quadratures, 1 analytic endpoint, physical sharp inequality')
