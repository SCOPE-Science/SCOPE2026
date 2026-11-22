"""Supplementary finite-dimensional checks for an analytic signed-biclique heat-kernel theorem.
Run: python check_signed.py. Numerical checks supplement, not replace, the proof.
"""
from math import sqrt, exp, log, isclose
import numpy as np
import sympy as sp
from scipy.linalg import eigh
from scipy.optimize import brentq

checks = 0

def ck(v, msg='check'):
    global checks
    assert bool(v), msg
    checks += 1

def data(m,a):
    tau=1+a
    b=m+1-2*tau
    c=2*m-1
    delta=sqrt((b-c)**2+4*(m-1))
    lam0=(b+c-delta)/2
    lam1=(b+c+delta)/2
    w=(lam1-b)/delta
    return lam0,lam1,w

def edge(m,a,t):
    lo,hi,w=data(m,a)
    return .5*(1/m+(1-1/m)*exp(-m*t)-w*exp(-lo*t)-(1-w)*exp(-hi*t))

def minimum(m,a):
    lo,hi,w=data(m,a)
    # Derivative: monotonically crossing unique positive point after convex exponential rescaling.
    def h(t):return w*lo*exp((m-lo)*t)+(1-w)*hi*exp(-(hi-m)*t)-(m-1)
    hi_t=1.
    while h(hi_t)<0:hi_t*=2
    return brentq(h,0,hi_t)

def root(m,a):
    t_min=minimum(m,a)
    assert edge(m,a,t_min)<0
    t_hi=max(1.,2*t_min)
    while edge(m,a,t_hi)<0:t_hi*=2
    return brentq(lambda t: edge(m,a,t),t_min,t_hi)

def mat(m,a):
    L=np.zeros((2*m,2*m))
    for i in range(m):
        for j in range(m,2*m):
            z=(-a if i==0 and j==m else 1.)
            L[i,i]+=z;L[j,j]+=z;L[i,j]-=z;L[j,i]-=z
    return L

# Exact symbolic invariant: two-by-two antisymmetric block and determinant.
m,t=sp.symbols('m t', real=True)
MM=sp.Matrix([[m+1-2*t,sp.sqrt(m-1)],[sp.sqrt(m-1),2*m-1]])
ck(sp.simplify(MM.det()-2*(m*m-t*(2*m-1)))==0)
ck(sp.simplify(sp.trace(MM)-(3*m-2*t))==0)
ck(sp.simplify(3*m-2*m*m/(2*m-1)-m*(4*m-3)/(2*m-1))==0)

for m in (2,3,4,7,12):
    ac=(m-1)**2/(2*m-1)
    wc=(2*m-1)**2/(m*(4*m-3))
    for fraction in (0.002,0.02,0.1,0.4,0.8,0.99):
        a=ac*fraction
        L=mat(m,a)
        ev,U=eigh(L)
        low,high,w=data(m,a)
        ck(abs(ev[0])<2e-13)
        ck(abs(ev[1]-low)<3e-12)
        ck(0<low<m<high and 0<w<1)
        tm=minimum(m,a); tr=root(m,a)
        ck(0<tm<tr)
        ck(abs(edge(m,a,tr))<2e-11)
        ck(edge(m,a,tm)<0)
        for x in np.linspace(.005, min(8.,max(2*tr,2.)),24):
            H=(U*np.exp(-ev*x))@U.T
            ck(abs(H[0,m]-edge(m,a,x))<4e-11)
            ck(abs(np.max(np.abs(H).sum(axis=1))-(1+2*max(0,-edge(m,a,x))))<5e-11)
            # No off-diagonal negative entries other than the antagonistic edge.
            for i in range(2*m):
                for j in range(i+1,2*m):
                    if (i,j)!=(0,m):ck(H[i,j]>-5e-13)
        print('m',m,'a/critical',fraction,'recovery',round(tr,8))
    # both endpoint transition asymptotic formulae
    small_a=ac*1.e-7
    tsmall=root(m,small_a)
    target=sqrt(6*small_a)/(m-1)
    ck(abs(tsmall/target-1)<.03)
    near=ac*(1-1.e-5)
    tnear=root(m,near)
    target=log(m*wc)/(2*wc*(ac-near))
    ck(abs(tnear/target-1)<.003)
print('PASS',checks,'assertions')
