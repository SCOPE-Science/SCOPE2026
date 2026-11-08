#!/usr/bin/env python3
"""Reproducible exact and Fourier-quadrature checks for phase-aligned two-orbit means."""
from fractions import Fraction as F
from math import pi,cos,sin,acos,sqrt,isclose

def eval_pair(a,phi,t):
    ap=(complex(cos(t),sin(t)),a*complex(cos(2*t),sin(2*t)))
    bm=(complex(cos(t+phi),sin(t+phi)),-a*complex(cos(2*(t+phi)),sin(2*(t+phi))))
    return ap,bm

def dot(x,y): return sum((v*w.conjugate()).real for v,w in zip(x,y))
def norm2(x): return dot(x,x)
def max_corr_fraction(a):
    b=a*a
    x=F(1) if 4*b <= 1 else 1/(4*b)
    m=b+x-2*b*x*x
    var=(F(1)+b-m)/2
    gap=b-var
    return x,m,var,gap

assert max_corr_fraction(F(1,4))==(F(1),F(15,16),F(1,16),F(0))
assert max_corr_fraction(F(1,2))==(F(1),F(3,4),F(1,4),F(0))
for a in [F(1,8),F(1,4),F(1,2),F(3,5),F(3,4),F(1),F(5,3),F(2)]:
    x,m,v,gap=max_corr_fraction(a)
    assert v == (a*a if a<=F(1,2) else F(1,2)-F(1,16)/(a*a))
    assert gap == (F(0) if a<=F(1,2) else (4*a*a-1)**2/(16*a*a))
    af=float(a); phi=acos(float(x))
    for theta in [0.0,0.1,0.7,1.2,2.4,5.1]:
        aa,bb=eval_pair(af,phi,theta)
        assert isclose(dot(aa,bb),float(m),rel_tol=1e-12,abs_tol=1e-12)
        assert isclose(norm2(aa),1+af*af,rel_tol=1e-12,abs_tol=1e-12)
        assert isclose(norm2(bb),1+af*af,rel_tol=1e-12,abs_tol=1e-12)
        avg=[(u+v)/2 for u,v in zip(aa,bb)]
        assert isclose((norm2([u-v for u,v in zip(aa,bb)])/4),float(v),rel_tol=1e-12,abs_tol=1e-12)
    for j in range(0,361):
        ph=2*pi*j/360
        C=cos(ph)-af*af*cos(2*ph)
        assert C<=float(m)+1e-10
    if a>F(1,2):
        assert phi>0
        assert not isclose(af*sin(phi),0,abs_tol=1e-10)
# Exact local descent at arithmetic average when a > 1/2:
for a in [F(3,5),F(3,4),F(1),F(2)]:
    aa=float(a)
    for ph in [0.0001,0.01,0.02]:
        C=cos(ph)-aa*aa*cos(2*ph)
        assert C>1-aa*aa
print('VERIFY_OK exact_parameter_cases=8 harmonic_inner_products=48 scanned_phases=2888 suboptimal_descent_checks=12')
