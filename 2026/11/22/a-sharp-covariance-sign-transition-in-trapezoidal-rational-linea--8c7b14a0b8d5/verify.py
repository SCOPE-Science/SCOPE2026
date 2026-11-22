"""Exact symbolic and independently triangulated moment checks for trapezoidal frusta.

Requires sympy and scipy. Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import sympy as sp
import numpy as np
from scipy.spatial import ConvexHull

A,B,D,T,R = sp.symbols('a b d t r', positive=True)
y=sp.symbols('y',real=True)
w=A+D*(B-y)
area=sp.integrate(w,(y,0,B))
mu_x=sp.factor(sp.integrate(w**2/2,(y,0,B))/area)
mu_y=sp.factor(sp.integrate(y*w,(y,0,B))/area)
base_c=sp.factor(sp.integrate(y*w**2/2,(y,0,B))/area-mu_x*mu_y)
assert sp.factor(base_c+B**2*D*(6*A**2+6*A*B*D+B**2*D**2)/(36*(2*A+B*D)**2))==0
rho=sp.factor((-base_c/(mu_x*mu_y)).subs(A,R*B*D))
assert sp.factor(rho-(6*R**2+6*R+1)/(4*(3*R+1)*(3*R**2+3*R+1)))==0
mom1=3*(1-T**4)/(4*(1-T**3))
mom2=3*(1-T**5)/(5*(1-T**3))
q=sp.factor(1-mom1**2/mom2)
assert sp.factor(q-(1-T)**2*(T**4+4*T**3+10*T**2+4*T+1)/(16*(T**2+T+1)*(T**4+T**3+T**2+T+1)))==0
assert sp.factor(sp.diff(q,T)-15*T**2*(T-1)*(T+1)*(T**2+1)*(3*T**2+4*T+3)/(16*(T**2+T+1)**2*(T**4+T**3+T**2+T+1)**2))==0
assert sp.factor(sp.Rational(1,16)-rho-3*(3*R**3-4*R**2-6*R-1)/(16*(3*R+1)*(3*R**2+3*R+1)))==0

def expected(a,b,d,t):
    subs={A:sp.Rational(a),B:sp.Rational(b),D:sp.Rational(d),T:sp.Rational(t)}
    ux=mu_x.subs(subs); uy=mu_y.subs(subs); c=base_c.subs(subs)
    e1=sp.Rational(3,4) if t==0 else mom1.subs(subs)
    e2=sp.Rational(3,5) if t==0 else mom2.subs(subs)
    if t==1: e1=e2=1
    return sp.factor(e2*c+(e2-e1**2)*ux*uy)

def det3(x,y,z):
    return x[0]*(y[1]*z[2]-x[0]*0-y[2]*z[1])+x[1]*(y[2]*z[0]-y[0]*z[2])+x[2]*(y[0]*z[1]-y[1]*z[0])

def volume_cov_direct(a,b,d,t):
    a,b,d,t=map(F,(a,b,d,t))
    v=[]
    for s,z in [(F(1),F(0)),(t,F(1))]:
        for x,y in [(0,0),(a+b*d,0),(a,b),(0,b)]:
            p=(F(s*x),F(s*y),z)
            if p not in v:v.append(p)
    hull=ConvexHull(np.array(v,dtype=float))
    center=tuple(sum(p[i] for p in v)/len(v) for i in range(3))
    V=F(0); SX=F(0); SY=F(0); SXY=F(0)
    for ids in hull.simplices:
        pts=[center]+[v[j] for j in ids]
        u=[pts[1][i]-center[i] for i in range(3)]
        v2=[pts[2][i]-center[i] for i in range(3)]
        w2=[pts[3][i]-center[i] for i in range(3)]
        vol=abs(det3(u,v2,w2))/6
        if not vol:continue
        ex=sum(p[0] for p in pts)/4
        ey=sum(p[1] for p in pts)/4
        exy=(sum(p[0] for p in pts)*sum(p[1] for p in pts)+sum(p[0]*p[1] for p in pts))/20
        V+=vol; SX+=vol*ex; SY+=vol*ey; SXY+=vol*exy
    return (SXY/V)-(SX/V)*(SY/V)

number=0
for a,b,d,t in product([1,2,3,5,10],[1,2],[1,2],[F(0),F(1,4),F(1,2),F(3,4),F(1)]):
    if t==0 and a==10: continue
    direct=volume_cov_direct(a,b,d,t)
    theoretical=F(expected(a,b,d,t))
    assert direct==theoretical,(a,b,d,t,direct,theoretical)
    number+=1
# root uniqueness and selected phase signs
crit=max(float(sp.re(root)) for root in sp.nroots(3*R**3-4*R**2-6*R-1) if abs(float(sp.im(root)))<1e-10)
assert 2.27<crit<2.28
assert expected(3,1,1,0)>0 and expected(3,1,1,1)<0
assert expected(1,1,1,0)<0
assert expected(3,1,1,F(1,4))>0 and expected(3,1,1,F(1,2))<0
print('ALL_CHECKS_PASSED',number,'independent exact tetrahedral prismatoid moment comparisons')
