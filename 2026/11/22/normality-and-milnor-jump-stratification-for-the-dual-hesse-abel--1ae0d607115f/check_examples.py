#!/usr/bin/env python3
"""Exact illustrative checks of quadratic boundary strata over Q(zeta_3).

No numerical approximation or algebraic geometry package is required; SymPy
performs exact polynomial arithmetic. The general proof is in RESULT.md.
"""
import sympy as sp
x,y,z,t=sp.symbols('x y z t')
cycl=t*t+t+1
rem=lambda f: sp.rem(sp.expand(f),cycl,t).expand()
zeta=lambda j:rem(t**(j%3))
P=(x**3-y**3)*(y**3-z**3)*(z**3-x**3)
triples=[(0,0,1),(0,1,0),(1,0,0)]+[(zeta(i+j),zeta(j),1) for i in range(3) for j in range(3)]
assert len(triples)==12

def hit_triple(Q):
    return [i for i,(a,b,c) in enumerate(triples)
            if rem(Q.subs({x:a,y:b,z:c},simultaneous=True))==0]

def rank(Q):
    return sp.hessian(Q,(x,y,z)).rank()

def tangency_count(Q):
    count=0
    for family in range(3):
        for j in range(3):
            a=zeta(j)
            if family==0: f=Q.subs({x:a*y});u,v=y,z
            elif family==1: f=Q.subs({y:a*z});u,v=x,z
            else: f=Q.subs({z:a*x});u,v=x,y
            A=rem(f.subs({u:1,v:0},simultaneous=True))
            C=rem(f.subs({u:0,v:1},simultaneous=True))
            B=rem(f.subs({u:1,v:1},simultaneous=True)-A-C)
            if rem(B*B-4*A*C)==0:count+=1
    return count

def node(L1,L2):
    a=sp.Matrix([[L.diff(v) for v in (x,y,z)] for L in (L1,L2)])
    return [sp.expand(v) for v in a.row(0).cross(a.row(1))]

Qs={
 'smooth transverse':x*x+y*y+7*z*z,
 'smooth tangent':(x-y)*(x+2*y)+z*z,
 'rank-two off':(x-y+z)*(x+2*y+3*z),
 'rank-two on':(x-y+z)*(x-y+2*z),
 'double line':(x+2*y+3*z)**2,
}
expected={'smooth transverse':(3,293),'smooth tangent':(3,296),
          'rank-two off':(2,296),'rank-two on':(2,299),
          'double line':(1,320)}
for name,Q in Qs.items():
    assert hit_triple(Q)==[],(name,hit_triple(Q))
    r=rank(Q)
    if r==3:
        tang=tangency_count(Q)
        mu=293+3*tang
    elif r==2:
        fac=sp.factor_list(Q)[1]
        assert len(fac)==2 and all(exp==1 for _,exp in fac)
        pt=node(fac[0][0],fac[1][0]); onB=sp.simplify(P.subs(dict(zip((x,y,z),pt))))==0
        mu=299 if onB else 296
    else:
        assert sp.factor_list(Q)[1][0][1]==2
        mu=320
    assert (r,mu)==expected[name],(name,r,mu)
    print(name,'rank=',r,'vertex_Milnor=',mu)
print('All five exact illustrative cases passed.')
