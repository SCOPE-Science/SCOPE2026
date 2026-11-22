"""Reproduce exact algebra and supplementary numerical eigenvalue tests."""
import sympy as sp
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from itertools import product

s,mu,q,t=sp.symbols('s mu q t', positive=True)
L=sp.Matrix([[1,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,1]])
xs=q+t; ys=q-t
A=mu*sp.eye(4)+L+sp.diag(xs,ys,ys,xs)
S=sp.Matrix([[mu+1+xs,-1],[-1,mu+1+ys]])
T=sp.Matrix([[mu+1+xs,-1],[-1,mu+3+ys]])
assert sp.simplify(A*sp.Matrix([1,0,0,1])-sp.Matrix([S[0,0],S[1,0],S[1,0],S[0,0]]))==sp.zeros(4,1)
assert sp.factor(A.charpoly(s).as_expr()-(S.charpoly(s).as_expr()*T.charpoly(s).as_expr()))==0
# The two extreme eigenvalues are m-sqrt(1+t^2) and m+1+sqrt(1+(t-1)^2).
assert sp.factor(S.det()-(mu+1+q)**2+1+t*t)==0
assert sp.factor(T.det()-(mu+2+q)**2+1+(t-1)**2)==0
f0=(1+q+sp.sqrt(1+q*q))/(2*sp.sqrt(1+q*q))
assert sp.simplify(q/(sp.sqrt(1+q*q)*(1+q-sp.sqrt(1+q*q)))-f0)==0
assert sp.simplify(sp.diff(f0,q)-(1-q)/(2*(1+q*q)**sp.Rational(3,2)))==0

def goal(t,mu,B):
    q=B/4; m=mu+1+q
    a=np.sqrt(1+t*t); b=np.sqrt(1+(1-t)**2)
    return (m+1+b)/(m-a)
def dlog(t,mu,B):
    q=B/4;m=mu+1+q
    a=np.sqrt(1+t*t);b=np.sqrt(1+(1-t)**2)
    return t/(a*(m-a))+(t-1)/(b*(m+1+b))
def optimal(mu,B):
    q=B/4
    if dlog(q,mu,B)<=0:return q
    return brentq(lambda t:dlog(t,mu,B),0,min(q,0.5),xtol=1e-14)
def full_matrix(mu,B,ds):return mu*np.eye(4)+np.array(L,dtype=float)+np.diag(ds)
def cond(A):
    z=np.linalg.eigvalsh(A);return z[-1]/z[0]

runs=0
rng=np.random.default_rng(3691)
for mu in (.001,.01,.1,1,10,100):
 for B in (.001,.01,.1,.2,.5,1,2,5,10,50):
    tt=optimal(mu,B);q=B/4
    d=[q+tt,q-tt,q-tt,q+tt]
    opt=cond(full_matrix(mu,B,d))
    assert abs(opt-goal(tt,mu,B))<=2e-10*opt
    xx=minimize_scalar(lambda t:goal(t,mu,B),bounds=(-q,q),method='bounded',options={'xatol':1e-13})
    assert opt<=xx.fun*(1+2e-8)
    for _ in range(100):
        v=rng.dirichlet(np.ones(4))*B
        cc=cond(full_matrix(mu,B,v))
        assert cc>=opt*(1-3e-12),(mu,B,d,v,cc,opt)
        runs+=1
# Critical B numerical check and high budget concentration
for mu in (.001,.01,.1,1,10,100,1000):
    qc=brentq(lambda c:dlog(c,mu,4*c),1e-14,.5,xtol=1e-14)
    assert 0<qc<.5
    assert abs(optimal(mu,4*qc)-qc)<1e-10
    assert optimal(mu,4*qc+.1)<(4*qc+.1)/4
assert abs(optimal(1,1)-.175427)<2e-6
assert abs(optimal(1,200)-.5)<.04
print('PASS: 6 exact symbolic identities, 6000 random allocations, 60 fixed-budget comparisons, 7 sharp critical checks, 2 reference checks')
