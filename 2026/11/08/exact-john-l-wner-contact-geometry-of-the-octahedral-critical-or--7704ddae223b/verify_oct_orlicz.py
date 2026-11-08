"""Checks exact algebra and numerical implications of the octahedral Orlicz-radius theorem.

Run with Python 3 standard library. The proof for all real directions is in RESULT.md.
"""
from fractions import Fraction as F
from math import log,cosh,sqrt,acos,pi,exp,acosh
from random import Random

def poly(t, q):
    a,b,c = t
    e2=a*b+b*c+c*a
    e3=a*b*c
    return 1+4*q+(6-8*e2)*q*q+4*(1-4*e2+16*e3)*q**3+(1-4*e2)**2*q**4

def bounds(r):
    return 4*log(cosh(r/2)),log(cosh(sqrt(3)*r/2))+3*log(cosh(r/(2*sqrt(3))))

def bisect(f):
    a,b=0.,2.
    assert f(a)<1<f(b)
    for _ in range(75):
        m=(a+b)/2
        if f(m)<1:a=m
        else:b=m
    return (a+b)/2

rng=Random(739181)
checks=0
for _ in range(5000):
    xyz=[rng.randint(-30,30) for i in range(3)]
    norm=sum(a*a for a in xyz)
    if not norm: continue
    t=tuple(F(a*a,norm) for a in xyz)
    e2=t[0]*t[1]+t[1]*t[2]+t[0]*t[2]
    e3=t[0]*t[1]*t[2]
    assert 1-4*e2+9*e3 >=0
    assert 9*e3<=e2
    q=F(rng.randint(1,100),200)
    prod=F(1)
    for sg in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]:
        ss=sum(a*b for a,b in zip(xyz,sg))
        prod*=1+q*F(ss*ss,norm)
    assert prod==poly(t,q)
    eq=poly((F(1,3),)*3,q)
    axis=poly((F(1),F(0),F(0)),q)
    assert eq<=prod<=axis
    checks+=1
ri=bisect(lambda r:bounds(r)[0]); ro=bisect(lambda r:bounds(r)[1])
assert abs(ri-2*acosh(exp(.25)))<1e-12
assert 1.47380<ri<1.47382<1.54462<ro<1.54464<2
assert abs(bounds(ri)[0]-1)<1e-12 and abs(bounds(ro)[1]-1)<1e-12
print('PASS',checks,'exact rational Euler-factor comparisons; radii:',ri,ro)
