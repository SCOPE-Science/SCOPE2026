#!/usr/bin/env python3
"""Algebra and finite numerical diagnostics for a Hardy-space shift.

Requires only Python 3 standard library. Exact symbolic polynomial checks are
supplementary to the analytical proof for all real parameters.
"""
from fractions import Fraction as Q
from math import sqrt

class P:
    """Sparse exact polynomial in (w, beta, k)."""
    def __init__(self, terms=None):
        self.t = {e: Q(c) for e, c in (terms or {}).items() if c}
    def __add__(self, rhs):
        if not isinstance(rhs, P): rhs = P({(0,0,0): rhs})
        d = dict(self.t)
        for e, c in rhs.t.items(): d[e] = d.get(e,Q(0)) + c
        return P(d)
    __radd__ = __add__
    def __neg__(self): return P({e:-c for e,c in self.t.items()})
    def __sub__(self,rhs): return self+-rhs if isinstance(rhs,P) else self+(-rhs)
    def __rsub__(self,rhs): return rhs + -self
    def __mul__(self,rhs):
        if not isinstance(rhs,P): rhs = P({(0,0,0):rhs})
        d={}
        for x,a in self.t.items():
            for y,b in rhs.t.items():
                e=tuple(i+j for i,j in zip(x,y))
                d[e]=d.get(e,Q(0))+a*b
        return P(d)
    __rmul__ = __mul__
    def __pow__(self,n):
        assert n>=0
        ans=P({(0,0,0):1})
        for _ in range(n): ans=ans*self
        return ans
    def dw(self):
        return P({(i-1,j,k):i*c for (i,j,k),c in self.t.items() if i})
    def sub_w(self,x):
        if isinstance(x,P):
            ans=P()
            for (i,j,k),c in self.t.items():
                ans=ans+c*(x**i)*(B**j)*(K**k)
            return ans
        d={}
        for (i,j,k),c in self.t.items():
            e=(0,j,k);d[e]=d.get(e,Q(0))+c*x**i
        return P(d)
    def sub_k(self,x):
        d={}
        for (i,j,k),c in self.t.items():
            e=(i,j,0);d[e]=d.get(e,Q(0))+c*x**k
        return P(d)
    def __eq__(self,rhs):
        if not isinstance(rhs,P):rhs=P({(0,0,0):rhs})
        return self.t==rhs.t

W=P({(1,0,0):1}); B=P({(0,1,0):1}); K=P({(0,0,1):1})
ONE=P({(0,0,0):1}); checks=0

def check(x):
    global checks
    assert x
    checks+=1

# Rational maximum F(w) = q U(w)/D(w).
U=W*(1-W**2)
D=ONE-B*W**2-(ONE-B)*K*W
N=ONE-(3-B)*W**2+2*(ONE-B)*K*W**3+B*W**4
check(U.dw()*D-U*D.dw()==N)
check(N.dw()==2*W*(-(3-B)+3*(ONE-B)*K*W+2*B*W**2))
check(N.sub_w(K)==(ONE-K**2)*(ONE-(2-B)*K**2))
check(N.sub_k(Q(1))==(ONE-W)**2*(B*W**2+2*W+ONE))
# Squared kernel-overlap identity after r=(w-k)/(1-kw).
E=ONE-K*W; H=W-K
check((E**2-H**2)*(ONE-W**2)==(ONE-K**2)*(E-W*H)**2)
check((E-W*H)==ONE-W**2)
check(E-B*W*H==D)

# Exact admissible q/k Pythagorean pairs, finite diagnostics only.
for q,k in ((Q(3,5),Q(4,5)),(Q(4,5),Q(3,5)),
            (Q(5,13),Q(12,13)),(Q(12,13),Q(5,13))):
    check(q*q+k*k==1)
    for beta in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(9,10)):
        for w in (Q(0),Q(1,9),Q(1,3),Q(2,3),Q(9,10),Q(99,100)):
            r=(w-k)/(1-k*w)
            check(abs(r)<1 and w<1)
            check((1-r*r)*(1-w*w)==q*q*(1-r*w)**2)
            f=q*w*(1-w*w)/(1-beta*w*w-(1-beta)*k*w)
            direct=q*(1-r*w)*w/(1-beta*r*w)
            check(f==direct)
            check(f>=0)
# At q=3/5, k=4/5, the sharp damping parameter is 7/16.
q=Q(3,5);k=Q(4,5);beta=Q(7,16)
root_N=lambda w:1-(3-beta)*w*w+2*(1-beta)*k*w**3+beta*w**4
check(root_N(k)==0)
check(q*k==Q(12,25))

# One-dimensional stationary root (bisection is a finite diagnostic).
def numeric(q,beta):
    k=sqrt(max(0.0,1-q*q))
    def n(w):return 1-(3-beta)*w*w+2*(1-beta)*k*w**3+beta*w**4
    lo,hi=0.0,1.0
    for _ in range(130):
        mid=(lo+hi)/2
        if n(mid)>0:lo=mid
        else:hi=mid
    w=(lo+hi)/2
    d=1-beta*w*w-(1-beta)*k*w
    return w,q*w*(1-w*w)/d,k

for beta in (0.0,0.2,0.5,0.9):
    for q in (0.1,0.2,0.4,0.5,0.6,0.7071067811865476,0.8,0.9,1.0):
        w,radius,k=numeric(q,beta)
        check(radius>=q*k-1e-12)
        check(0<w<1)
        threshold=(1-beta)/(2-beta)
        check((w>=k-1e-12)==(q*q>=threshold-1e-12))
        for beta2 in (0.0,0.5,0.99):
            # Every sampled test pair is dominated by the algebraic maximum.
            for x in (0.0,0.1,0.3,0.6,0.85,0.99):
                if beta2==beta:
                    f=q*x*(1-x*x)/(1-beta*x*x-(1-beta)*k*x)
                    check(f<=radius+1e-10)
for beta in (0.0,0.5,0.9):
    for q in (1e-2,1e-3):
        w,r,k=numeric(q,beta)
        approx=(2*q/(1+beta)
                -2*sqrt((1-beta)*(3+beta))*q*q/(1+beta)**2)
        check(abs(r-approx)<5*q**3)
        check(abs((1-w)/q-sqrt((1-beta)/(3+beta)))<2*q)
for q in (0.3,0.5,0.9,1.0):
    for e in (1e-4,1e-5):
        w,r,k=numeric(q,1-e)
        pred=q*sqrt(2*(1-k)*e)
        check(abs((q-r)/pred-1)<0.06)
print('GEOMETRIC_Q_BEREZIN_CHECK_OK',checks,'exact and finite diagnostic assertions')
