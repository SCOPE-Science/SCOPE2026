"""Finite exact and floating-point diagnostics for planar similarity conditioning.

The infinite-dimensional amplification statement is proved analytically in RESULT.md.
Run: python verify.py
"""
from fractions import Fraction
from math import cos, sin, sqrt, pi
from cmath import exp
import random


def mult(a, b):
    return ((a[0][0]*b[0][0]+a[0][1]*b[1][0],
             a[0][0]*b[0][1]+a[0][1]*b[1][1]),
            (a[1][0]*b[0][0]+a[1][1]*b[1][0],
             a[1][0]*b[0][1]+a[1][1]*b[1][1]))


def star(a):
    return ((a[0][0].conjugate(), a[1][0].conjugate()),
            (a[0][1].conjugate(), a[1][1].conjugate()))


def norm2(a):
    tr = sum(abs(a[i][j])**2 for i in range(2) for j in range(2))
    det = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    return sqrt((tr + sqrt(max(0.0, tr*tr-4*abs(det)**2)))/2)


def eq(a, b, tol=3e-10):
    return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2)) < tol


def u(phi, phase):
    c,s=cos(phi),sin(phi)
    z=exp(1j*phase)
    return ((c,-s/z),(s*z,c))


def conj(u0, a):
    return mult(mult(u0,a),star(u0))


def diag(x,y):
    return ((x,0),(0,y))


count=0
for i in range(1,21):
    for j in range(1,21):
        a,b=Fraction(i,3)+1,Fraction(j,7)+1
        qa=((Fraction(0),a),(1/a,Fraction(0)))
        qb=((Fraction(0),b),(1/b,Fraction(0)))
        d=diag(b/a,Fraction(1))
        assert mult(d,qa)==mult(qb,d)
        na=((Fraction(0),a),(Fraction(0),Fraction(0)))
        nb=((Fraction(0),b),(Fraction(0),Fraction(0)))
        assert mult(d,na)==mult(nb,d)
        assert max(b/a,a/b)>=1
        count+=3

r=random.Random(20261108)
for _ in range(256):
    a,b=1+30*r.random(),1+30*r.random()
    ua,ub=u(r.random()*pi, r.random()*2*pi),u(r.random()*pi,r.random()*2*pi)
    qa,qb=conj(ua,((0,a),(1/a,0))),conj(ub,((0,b),(1/b,0)))
    na,nb=conj(ua,((0,a),(0,0))),conj(ub,((0,b),(0,0)))
    y=mult(mult(ub,diag(b/a,1)),star(ua))
    yi=mult(mult(ua,diag(a/b,1)),star(ub))
    expected=max(a/b,b/a)
    assert eq(mult(y,qa), mult(qb,y))
    assert eq(mult(y,na), mult(nb,y))
    assert eq(mult(y,yi),diag(1,1))
    assert abs(norm2(qa)-a) < 2e-11
    assert abs(norm2(qb)-b) < 2e-11
    assert abs(norm2(na)-a) < 2e-11
    assert abs(norm2(nb)-b) < 2e-11
    assert abs(norm2(y)*norm2(yi)-expected) < 5e-10
    count+=7

print(f'PASS: {count} exact and numerical assertions; universal theorem is analytic.')
