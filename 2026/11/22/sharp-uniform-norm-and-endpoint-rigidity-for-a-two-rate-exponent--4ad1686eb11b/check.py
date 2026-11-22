"""Supplementary reproducibility checks for a two-exponential projection theorem.

All theorem-level inequalities are established analytically in RESULT.md.
This numerical script checks formula normalization, the three kernel-sign regimes,
and equality cases; it is not a substitute for the proof.
"""
from __future__ import annotations
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
r,w=sp.symbols('r w', positive=True)
G=sp.Matrix([[sp.Rational(1,2),1/(1+r)],[1/(1+r),1/(2*r)]])
Inv=sp.simplify(G.inv())
D=2*(r+1)/(r-1)**2
expected=sp.Matrix([[D*(r+1),-2*r*D],[-2*r*D,r*(r+1)*D]])
assert all(sp.simplify(x)==0 for x in Inv-expected), 'Gram inverse mismatch'
A=(r+1)-2*r*w
B=r*((r+1)*w-2)
assert sp.simplify(A+B/r-(r-1)*(1-w))==0
assert sp.simplify(A+B-(r-1)*(r*w-1))==0


def exact_row(t, R):
    R=mp.mpf(R);t=mp.mpf(t)
    W=mp.exp(-(R-1)*t);U=mp.exp(-t)
    DD=2*(R+1)/(R-1)**2
    aa=(R+1)-2*R*W
    bb=R*((R+1)*W-2)
    integral=aa+bb/R
    if aa<0:
        z=(-aa/bb)**(1/(R-1))
        integral+=2*(-aa)*(R-1)/R*z
    elif aa+bb<0:
        z=(aa/-bb)**(1/(R-1))
        integral=2*aa*(R-1)/R*z-integral
    return DD*U*integral


def direct_row(t,R):
    R=mp.mpf(R);t=mp.mpf(t)
    W=mp.exp(-(R-1)*t);U=mp.exp(-t)
    aa=(R+1)-2*R*W
    bb=R*((R+1)*W-2)
    DD=2*(R+1)/(R-1)**2
    z=None
    if aa*(aa+bb)<0:
        z=mp.power(-aa/bb,1/(R-1))
    f=lambda x: abs(aa+bb*x**(R-1))
    if z is not None:
        out=mp.quad(f,[0,z,1])
    else: out=mp.quad(f,[0,1])
    return DD*U*out


def norm_formula(R):
    R=mp.mpf(R)
    return 4*(R+1)/R*mp.exp(-mp.log(R)/(R-1))

runs=0
for R in ['1.01','1.1','1.5','2','3','5','20','100']:
    R=mp.mpf(R)
    T1=mp.log(2*R/(R+1))/(R-1)
    T2=mp.log(R)/(R-1)
    ts=[mp.mpf('0'),T1/4,T1*.8,T1,(T1+T2)/2,T2,T2*mp.mpf('1.2'),T2*2,T2*5]
    ceiling=norm_formula(R)
    for t in ts:
        x=exact_row(t,R);y=direct_row(t,R)
        assert mp.almosteq(x,y,rel_eps=mp.mpf('1e-35'),abs_eps=mp.mpf('1e-35')), (R,t,x,y)
        assert x<=ceiling+mp.mpf('1e-35'),(R,t,x,ceiling)
        if t>0:
            assert x<ceiling
        runs+=1
    assert mp.almosteq(exact_row(0,R),ceiling,rel_eps=mp.mpf('1e-48'))
    assert ceiling < 4
    print('ratio',mp.nstr(R,8),'exact sharp norm',mp.nstr(ceiling,15), 'sample checks passed')
assert abs(norm_formula(mp.mpf('1.000000001'))-8/mp.e)<mp.mpf('1e-8')
assert abs(norm_formula(mp.mpf('10000000'))-4)<mp.mpf('1e-4')
print('PASS:',runs,'high-precision row comparisons; exact Gram inverse and signs; endpoint and both limits.')
