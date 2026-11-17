#!/usr/bin/env python3
"""Exact interval-itinerary and drift checks for an optical circle map.

Requires Python 3 and SymPy. Uses algebraic equality rather than floating
experiment to establish five bulk drift coefficients and the final slope.
"""
import sympy as sp

z = sp.sqrt(5)
beta = sp.symbols('beta', real=True, positive=True)
x = sp.symbols('x', real=True)
beta0 = z - 1
cut = (beta-1)/beta
branch = (
    x/2 + (beta+1)/(2*beta),
    beta*x/2 + (1-beta)/2,
    beta*(x-1)+(2+beta)/4,
    2*(x-1)/beta+(beta+1)/(2*beta),
)
ends = (sp.Integer(0), (3-z)/4, sp.Rational(1,2), sp.Rational(3,4),
        (5+z)/8, sp.Integer(1))
itineraries = (
    (0,3,3,2,1), (1,0,3,3,2), (2,1,0,3,3),
    (3,2,1,0,3), (3,3,2,1,0),
)
expected = (
    -(5+3*z)/8, -(5+2*z)/4, -(15+7*z)/16,
    -(5+2*z)/8, -(5+3*z)/16,
)
assert sp.simplify(cut.subs(beta,beta0)-ends[1])==0
assert sp.simplify(branch[0].subs(x,cut)-1)==0
assert sp.simplify(branch[1].subs(x,cut))==0
assert sp.simplify(branch[2].subs(x,sp.Rational(1,2))-branch[1].subs(x,sp.Rational(1,2)))==0
assert sp.simplify(branch[3].subs(x,sp.Rational(3,4))-branch[2].subs(x,sp.Rational(3,4)))==0

def which(v):
    v=float(v)
    c=float(ends[1])
    return 0 if v<c else (1 if v<.5 else (2 if v<.75 else 3))

pieces=[]
for j,(it,exp) in enumerate(zip(itineraries,expected)):
    v=x
    middle=(ends[j]+ends[j+1])/2
    for k,idx in enumerate(it):
        assert which(v.subs({x:middle,beta:beta0}))==idx, (j,k,idx)
        v=sp.cancel(branch[idx].subs(x,v))
    slope=sp.simplify(sp.diff(v,x))
    assert slope==1, (j,slope)
    drift=sp.simplify(sp.diff(v,beta).subs(beta,beta0))
    assert sp.simplify(drift-exp)==0, (j,drift,exp)
    assert sp.simplify(v.subs(beta,beta0)-x)==0
    leng=sp.simplify(ends[j+1]-ends[j])
    assert leng>0 and exp<0
    time=sp.simplify(leng/drift)
    assert sp.simplify(time-(3-sp.Rational(7,5)*z))==0
    pieces.append((leng,drift,time))
period_time=sp.simplify(sum(t for _,_,t in pieces))
assert sp.simplify(period_time-(15-7*z))==0
slope=sp.simplify(1/(5*period_time))
assert sp.simplify(slope+(15+7*z)/100)==0
assert sp.simplify(sum(a for a,_,_ in pieces)-1)==0
assert sp.simplify(sum(a*d for a,d,_ in pieces))<0
print('VERIFY_OK exact_itineraries=5 exact_unit_slopes=5 algebraic_drifts=5 equal_crossing_times=5 derivative=', slope, 'decimal=',float(slope))
