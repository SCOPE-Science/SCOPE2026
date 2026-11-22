"""Finite checks of the wrapped exponential--Erlang discriminant and variance.

Use standard library only: python checker.py. Analytic proofs are in RESULT.md.
"""
from fractions import Fraction as F
from math import isclose

def moment(x,q,k):
    return (1-q)*x/(x-1j*k)+q*(x/(x-1j*k))**2

def pair(x,q):
    a=1+x*x
    return x*x/a-2*q*x*x/a**2, x/a+q*x*(x*x-1)/a**2

count=0
for p in range(1,20):
    x=F(p,11)
    for z in range(1,18):
        q=F(z,19)
        u,v=pair(x,q)
        d=v*v-u*(1-u)
        assert d==q*q*x*x/(1+x*x)**2
        th=(float(v)+float(d)**.5)/(1-float(u))
        qq=(1+th*th)*float(d)**.5/th
        assert isclose(th,float(x),rel_tol=1e-10,abs_tol=1e-10)
        assert isclose(qq,float(q),rel_tol=1e-9,abs_tol=1e-9)
        m=moment(float(x),float(q),1)
        assert isclose(m.real,float(u),rel_tol=1e-11,abs_tol=1e-11)
        assert isclose(m.imag,float(v),rel_tol=1e-11,abs_tol=1e-11)
        count+=5
for p in range(1,40):
    x=F(p,12)
    u,v=pair(x,F(0))
    a=2*u-1
    b=2*v
    assert a*a+b*b==1
    m2=moment(float(x),0,2)
    var=.5*(1+((float(a)-1j*float(b))**2*m2).real)-float(u)**2
    formula=(float(x)**2+2)/((1+float(x)**2)**2*(float(x)**2+4))
    assert isclose(var,formula,rel_tol=1e-11,abs_tol=1e-11)
    assert var>0
    count+=3
print('PASS',count,'finite checks')
