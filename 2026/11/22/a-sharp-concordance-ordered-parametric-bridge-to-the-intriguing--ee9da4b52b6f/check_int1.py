"""Numerical/symbolic spot checks for a one-parameter copula family.
Scientific claims rely on the accompanying analytic proof, not on these finite checks.
"""
from fractions import Fraction
from math import log, exp, isfinite
import random
import mpmath as mp
import sympy as sp

mp.mp.dps = 60


def C(g, x, y):
    x,y,g=mp.mpf(x),mp.mpf(y),mp.mpf(g)
    if x==0 or y==0:return mp.mpf(0)
    if x==1:return y
    if y==1:return x
    a=1+g*(1-x)/x
    return x*(1+y*mp.power(1-x,a)-mp.power(1-x*y,a))


def pieces(g,x,y):
    x,y,g=mp.mpf(x),mp.mpf(y),mp.mpf(g)
    s=1-x;t=1-x*y
    b=g*s/x;q=g+(1-g)*x;k=1-g
    u=mp.power(s,b)
    H1=u*(s-q-g*s/x*mp.log(s))
    L=-mp.log(t)-s*(1-t)/t
    H2=mp.power(t,b)*(g+2*k*x+g*q/x*L)
    lower=u*(1-g*x-g*s/x*mp.log(s))
    return H1,H2,lower,L


checks=0
x,y,g=sp.symbols("x y g", real=True)
s=1-x;t=1-x*y;b=g*s/x;q=g+(1-g)*x
assert sp.simplify(q-x*(1+b))==0
checks+=1
assert sp.simplify(sp.diff(b,x)+g/x**2)==0
checks+=1
assert sp.simplify(sp.diff(q,x)-(1-g))==0
checks+=1

rng=random.Random(271828)
for i in range(600):
    xx=mp.mpf(rng.randint(1,999))/1000
    yy=mp.mpf(rng.randint(0,1000))/1000
    gg=mp.mpf(rng.randint(0,1000))/1000
    h1,h2,lb,L=pieces(gg,xx,yy)
    assert L>=-mp.mpf('1e-55')
    checks+=1
    assert h1+h2>=lb-mp.mpf('1e-50')
    checks+=1
    assert lb>0
    checks+=1
    direct=mp.diff(lambda u: mp.diff(lambda v:C(gg,u,v),yy),xx)
    assert abs(direct-(h1+h2))<mp.mpf('1e-35')*max(1,abs(direct))
    checks+=1
    if 0<yy<1:
        ga=mp.mpf(rng.randint(0,900))/1000
        gb=ga+mp.mpf('0.001')
        assert C(gb,xx,yy)>C(ga,xx,yy)
        checks+=1
    assert abs(C(0,xx,yy)-xx*yy)<mp.mpf('1e-50')
    checks+=1

# Verify exact endpoint identities and two finite invalidity witnesses.
for xx in [mp.mpf(1)/3,mp.mpf(1)/2,mp.mpf(9)/10]:
    for yy in [mp.mpf(1)/5,mp.mpf(3)/5]:
        a=1/xx
        assert abs(C(1,xx,yy)-xx*(1+yy*(1-xx)**a-(1-xx*yy)**a))<mp.mpf('1e-50')
        checks+=1
neg=mp.mpf('-0.2')
yneg=1-mp.e**(-8)
for e in [mp.mpf('1e-6'),mp.mpf('1e-12'),mp.mpf('1e-18')]:
    xx=1-e
    d=sum(pieces(neg,xx,yneg)[:2]);
    assert d<0
    checks+=1
for e in [mp.mpf('1e-4'),mp.mpf('1e-8'),mp.mpf('1e-12')]:
    xx=1-e
    d=sum(pieces(mp.mpf('1.2'),xx,mp.mpf('0'))[:2])
    assert d<0
    checks+=1

print('PASS',checks,'supporting checks; 60 decimal digits')
