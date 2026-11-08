"""Reproduce finite exact and numerical checks for the heterogeneous two-hub resistance design.
Run: python verify_design.py. Standard numpy, scipy, sympy only.
The all-size mathematical statement is proved separately; these checks are supplementary.
"""
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize

COUNT=0
def check(condition, note):
    global COUNT
    assert bool(condition), note
    COUNT+=1

def kirchhoff_by_grounded(m, edges):
    # connected and positive-conductance graph; exact rational matrix inverse.
    N=m+2; L=sp.zeros(N)
    for i,j,w in edges:
        w=sp.Rational(w)
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w;L[j,i]-=w
    A=L[:N-1,:N-1]
    # Formula sum_{i<j} Rij = N tr L^+, and tr L^+ =tr L_ground^{-1} - (1/N) 1^T L_ground^{-1}1.
    inv=A.inv()
    return sp.simplify(N*sp.trace(inv)-sum(inv))

def symmetric_edges(x,y):
    m=len(x); return [(0,i+2,x[i]) for i in range(m)]+[(1,i+2,x[i]) for i in range(m)]+[(0,1,y)]

def formula(x,y):
    m=len(x); A=(m+1)/2; C=m+2
    return A*sum(1/t for t in x)+C/(sum(x)+2*y)

def optimum(c,d,B):
    c=np.asarray(c,dtype=float)
    m=len(c); A=(m+1)/2; C=m+2
    def f(rho):return sum(np.sqrt(A/(rho*c-C)))-1
    rho=brentq(f,C/min(c)*(1+1e-12),1e8,xtol=1e-12)
    threshold=4*C/rho
    if d<threshold:
        k=np.sqrt(A*d/(C*(4*c-d)))
        H=(d+np.sqrt(A*d/C)*sum(np.sqrt(4*c-d)))/2
        T=B/H
        x=T*k
        y=T*(1-sum(k))/2
        val=(np.sqrt(C*d)+np.sqrt(A)*sum(np.sqrt(4*c-d)))**2/(2*B)
    else:
        k=np.sqrt(A/(rho*c-C))
        T=B/(2*sum(c*k))
        x=T*k; y=0.
        val=formula(x,y)
    return x,y,threshold,val,rho

# 1. Independently compute the Kirchhoff index from an exact Laplacian inverse.
for m in (2,3,4,5):
    for s in range(1,6):
        x=[sp.Rational((s+i+1),s+3) for i in range(m)]
        for y in (sp.Rational(0),sp.Rational(s,7)):
            val=kirchhoff_by_grounded(m,symmetric_edges(x,y))
            target=sp.Rational(m+1,2)*sum(1/u for u in x)+sp.Rational(m+2)/(sum(x)+2*y)
            check(val==sp.simplify(target),(m,s,y,val,target))

# 2. Interior and boundary optimality, global comparison against asymmetric allocations.
rng=np.random.default_rng(271828)
for m in (2,3,4,6):
 for k in range(6):
    c=rng.uniform(.6,5,size=m)
    B=rng.uniform(2,40)
    x0,y0,threshold,val,rho=optimum(c,max(.0001, .2),B)
    for d in (threshold*.07, threshold*.55, threshold,threshold*1.3,threshold*4.0):
      x,y,th,v,rt=optimum(c,d,B)
      cost=2*np.dot(c,x)+d*y
      check(abs(cost-B)<1e-7,(m,'budget',cost,B))
      check(np.all(x>0) and y>=-1e-9,(m,'positive'))
      check(abs(formula(x,y)-v)<1e-7,(m,'objective',x,y,v))
      check((y>1e-9)==(d<th-1e-9),(m,'support',d,th,y))
      if y>1e-9:
        s=(m+2)/(sum(x)+2*y)**2
        lm=2*s/d
        for xi,ci in zip(x,c):
            check(abs((m+1)/2/xi**2+s-2*lm*ci)<1e-7,'active stationarity')
      else:
        lm=((m+1)/2/x[0]**2+(m+2)/(sum(x))**2)/(2*c[0])
        check(d*lm+1e-8>=2*(m+2)/(sum(x))**2,'boundary KKT')
        for xi,ci in zip(x,c):
            check(abs((m+1)/2/xi**2+(m+2)/(sum(x))**2-2*lm*ci)<1e-7,'boundary stationarity')
      for t in range(8):
        # fully asymmetric feasible allocation, not just mirror-symmetric competitors
        raw=rng.uniform(.03,3,size=2*m+1)
        prices=np.r_[c,c,d]
        w=B*raw/np.dot(prices,raw)
        edges=[(0,i+2,w[i]) for i in range(m)]+[(1,i+2,w[m+i]) for i in range(m)]+[(0,1,w[-1])]
        L=np.zeros((m+2,m+2))
        for i,j,vv in edges:L[i,i]+=vv;L[j,j]+=vv;L[i,j]-=vv;L[j,i]-=vv
        spec=np.linalg.eigvalsh(L)
        actual=(m+2)*sum(1/sv for sv in spec[1:])
        check(actual+1e-7>=v,'full asymmetric candidate')

# 3. Equal-cost threshold (closed rational formula) and scaling.
for m in range(2,35):
 c=np.ones(m); _,_,th,_,rho=optimum(c,1.0,10)
 th2=8*(m+2)/(m*m*(m+1)+2*(m+2))
 check(abs(th-th2)<1e-9,'equal price threshold')

print('VERIFY_OK',COUNT)
