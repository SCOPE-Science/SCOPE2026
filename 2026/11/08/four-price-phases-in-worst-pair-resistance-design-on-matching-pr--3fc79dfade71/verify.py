#!/usr/bin/env python3
"""Independent finite checks for a weighted bipartite network resistance-diameter theorem.

Use: python verify.py

The finite checks are supplementary and do not establish the all-size theorem.
"""
import math
from fractions import Fraction
import sympy as sp
from scipy.optimize import minimize_scalar

def exact_distances(m, x, y):
    # Direct grounded-Laplacian inversion, independent of the closed formulas.
    L = sp.zeros(2 * m)
    for i in range(m):
        for j in range(m):
            w = x if i == j else y
            L[i, i] += w
            L[m+j, m+j] += w
            L[i, m+j] -= w
            L[m+j, i] -= w
    H = L[:2*m-1, :2*m-1].inv()
    def R(a,b):
        v=sp.zeros(2*m-1,1)
        if a<2*m-1: v[a]=1
        if b<2*m-1: v[b]=-1
        return (v.T*H*v)[0]
    return (R(0,1),R(0,m),R(0,m+1))

def shell_formulas(m, x, y):
    d=x+(m-1)*y
    z=2*x+(m-2)*y
    rs=1/(m*y)+1/z
    rm=sp.Rational(2*(m-1),m)/z+1/(m*d)
    rn=1/(m*y)+sp.Rational(m-2,m)/z+1/(m*d)
    return rs,rm,rn

def params(m,P):
    tc=(math.sqrt(m*(m-2))-(m-2))/2
    p1=(m-1)/(m-2)
    p2=(m-1+tc*tc)/((m-2)/2+tc*tc)
    p3=(4*m*m-11*m+8)/((m-2)*(2*m-3))
    if P<=p1:
        t=(math.sqrt(m*(2*(m-1)-P*(m-2))/P)-(m-2))/2
    elif P<=p2:
        t=tc
    elif P<=p3:
        c=math.sqrt((m-1)-P*(m-2)/2)
        u=math.sqrt(P-1)
        t=((m-1)*c-(m-2)*u/2)/(u-c)
    else:
        t=0.0
    return tc,p1,p2,p3,t

def objective(m,P,t):
    if t<0: return float('inf')
    v=P*t+m-1
    return max(v*(1/m+1/(2*t+m-2)),
               v*(2*(m-1)/(m*(2*t+m-2))+1/(m*(t+m-1))))

def test():
    exact_count=0
    for m in range(3,7):
        for x in [0,sp.Rational(1,3),sp.Rational(3,2),sp.Rational(8,3)]:
            for y in [sp.Rational(1,2),sp.Rational(7,5),sp.Rational(3,1)]:
                got=exact_distances(m,x,y)
                want=shell_formulas(m,x,y)
                assert got==want,(m,x,y,got,want)
                assert got[0]>got[2]
                exact_count+=3
    phase_count=0
    for m in [3,4,5,6,8,10,20,40,100]:
        tc,p1,p2,p3,_=params(m,1)
        assert 0<p1<p2<p3<2*(m-1)/(m-2)
        for P in [0.1,0.7,1.0,p1*0.8,p1,(p1+p2)/2,p2,(p2+p3)/2,p3,p3*1.001,p3*2,10.0]:
            if P<=0:continue
            _,_,_,_,t=params(m,P)
            assert t>=-1e-9,(m,P,t)
            t=max(0,t)
            v=objective(m,P,t)
            upper=max(10, 5*t+10)
            opt=minimize_scalar(lambda z:objective(m,P,z), bounds=(0,upper),method='bounded', options={'xatol':1e-11})
            assert v<=opt.fun+5e-7*max(1,v),(m,P,t,v,opt.x,opt.fun)
            for zz in [0,tc, t/2, t+0.05,t+1, t+10]:
                assert v<=objective(m,P,zz)+3e-9*max(1,v)
            phase_count+=1
    # Check symbolic identities defining the crossover and endpoint price.
    m,t,P=sp.symbols('m t P',positive=True)
    a=(m-2)/2;b=m-1
    s=(P*t+b)*(1/m+1/(2*t+m-2))
    r=(P*t+b)*(2*b/(m*(2*t+m-2))+1/(m*(t+b)))
    assert sp.simplify(sp.diff(s,t) - (P/m+(P*(m-2)-2*b)/(2*t+m-2)**2))==0
    assert sp.simplify(sp.diff(r,t) - b/m*((P*a-b)/(t+a)**2+(P-1)/(t+b)**2))==0
    assert sp.simplify(sp.diff(r,t).subs(t,0).subs(P,(4*m*m-11*m+8)/((m-2)*(2*m-3))))==0
    print(f'PASS {exact_count} exact grounded-Laplacian shell checks, {phase_count} phase/optimization checks, 3 symbolic derivative identities')

if __name__=='__main__':
    test()
