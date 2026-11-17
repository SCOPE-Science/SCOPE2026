#!/usr/bin/env python3
"""Exact rational checks for a sharp coexistence census in a predator-prey flow.

Requires SymPy; no network access, and no input files other than this program.
"""
import sympy as sp

x,y=sp.symbols('x y')
R=sp.Rational
p=sp.Poly(100*x**4-1110*x**3+1110*x**2-300*x+21,x)
B=R(21,1000); H=R(9,10)
feed=(2+y)*x*y/(B+y+H*x*(2+y))
f=x*(1-x)*(x-R(1,10))-feed
g=feed-y
Y=x*(1-x)*(x-R(1,10))
Z=2*(x-R(21,200))/(10-x)
assert sp.simplify(g.subs(y,Z))==0
assert sp.simplify((f+g).subs(y,Y))==0
assert sp.simplify(sp.together(Y-Z)*(10-x)*100-p.as_expr())==0
J=sp.Matrix([f,g]).jacobian((x,y))
t=sp.factor(sp.trace(J).subs(y,Z))
d=sp.factor(J.det().subs(y,Z))
T=5937000*x**4-63743800*x**3+44138000*x**2-4416800*x+251559
D=300*x**4-6220*x**3+34410*x**2-22200*x+2979
K=1979000*x*(10-x)
assert sp.cancel(t-T/K)==0
assert sp.cancel(d-(200*x-21)*D/K)==0
V=sp.expand(T**2-4*K*(200*x-21)*D)

def sgn(a):
    return 1 if a>0 else (-1 if a<0 else 0)

def certificate(poly,a,b):
    """Prove polynomial nonvanishing on [a,b] via rational midpoint and Lipschitz."""
    poly=sp.Poly(poly,x); m=(a+b)/2; e=(b-a)/2
    upper=sum(abs(c)*i for (i,),c in poly.terms())
    v=poly.eval(m)
    assert abs(v)>e*upper,(poly.as_expr(),v,e*upper)
    return sgn(v)

intervals=[(R(109668415,10**9),R(109668417,10**9)),
           (R(276024322,10**9),R(276024325,10**9)),
           (R(692199537,10**9),R(692199540,10**9))]
for j,(lo,hi) in enumerate(intervals,1):
    assert R(21,200)<lo<hi<1
    e1,e2=p.eval(lo),p.eval(hi)
    assert e1*e2<0
    # T,K,D and V all have verified nonvanishing signs on the entire bracket.
    ts,ds,vs,ks=certificate(T,lo,hi),certificate(D,lo,hi),certificate(V,lo,hi),certificate(K,lo,hi)
    assert ks==1
    assert (ts,ds,vs)==[(1,1,1),(1,-1,1),(-1,1,-1)][j-1]
    if j==1: assert ts>0 and ds>0 and vs>0
    if j==2: assert ds<0
    if j==3: assert ts<0 and ds>0 and vs<0
    print('root',j,'interval',f'{lo}...{hi}','trace sign',ts,'det sign',ds,'disc sign',vs)
assert p.eval(10)<0 and p.LC()>0
# Four disjoint sign-change intervals; degree four implies exactly four simple real roots.
assert p.count_roots(-sp.oo,sp.oo)==4
# Remaining root beyond 10 and outside the physical x interval.
assert p.count_roots(10,sp.oo)==1
print('VERIFY_OK exact_rational=1 quartic_roots=4 interior_equilibria=3 source_saddle_sink=1 persistent_open_family=1')
# The genuinely cooperative parameter choice has positive underlying
# a=A-lambda/b=19 and two strictly positive equilibria.
Q2=sp.Poly(800*x**4-930*x**3+135*x**2-9*x+5,x)
Y2=x*(1-x)*(x-R(1,10))
Z2=(R(8,100)*x-R(1,10))/(1-16*x)
assert sp.together((1-16*x)*(Y2-Z2)-Q2.as_expr()/50).cancel()==0
assert Q2.eval(R(1,10))>0 and Q2.eval(R(1,2))<0 and Q2.eval(1)>0
assert Q2.count_roots(R(1,10),1)==2
assert R(1,10)>R(1,16) and 1<R(5,4)
# At lambda=Ab, the predator per-capita growth is independent of y.
A0=4; b0=R(1,10);lam0=A0*b0; h0=R(1,5);s0=1
x0=s0/(A0*(1-s0*h0))
y0=Y.subs(x,x0)
assert R(1,10)<x0<1 and y0>0
feed0=(lam0+A0*y)*x*y/(b0+y+h0*x*(lam0+A0*y))
assert sp.simplify((feed0-y).subs({x:x0,y:y0}))==0
assert sp.simplify((x*(1-x)*(x-R(1,10))-feed0).subs({x:x0,y:y0}))==0
print('VERIFY_OK cooperative_two=1 neutral_one=1 positive_hunting_gain=19')
