#!/usr/bin/env python3
"""Exact polynomial-identity checks and deterministic phase diagnostics.

Requires Python 3 standard library only. Run: python CHECK.py
This verifies identities and representative numerical cases; the accompanying
analytical proof establishes the universal parameter statements.
"""
from math import sqrt, isclose
from fractions import Fraction as F

# Sparse exact multivariate polynomials in (x,t,a,h,w), with integer powers.
class Poly:
    def __init__(self, terms=None): self.terms={k:v for k,v in (terms or {}).items() if v}
    @staticmethod
    def const(v): return Poly({(0,)*5:F(v)})
    @staticmethod
    def var(i):
        e=[0]*5; e[i]=1
        return Poly({tuple(e):F(1)})
    def __add__(self,o):
        o=P(o); d=self.terms.copy()
        for k,v in o.terms.items(): d[k]=d.get(k,F(0))+v
        return Poly(d)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.terms.items()})
    def __sub__(self,o):return self+-P(o)
    def __rsub__(self,o):return P(o)+-self
    def __mul__(self,o):
        o=P(o);d={}
        for a,x in self.terms.items():
            for b,y in o.terms.items():
                z=tuple(u+v for u,v in zip(a,b));d[z]=d.get(z,F(0))+x*y
        return Poly(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        y=P(1); z=self
        while n:
            if n&1:y=y*z
            z=z*z;n//=2
        return y
    def derivative(self,i=0):
        d={}
        for k,v in self.terms.items():
            if k[i]:
                e=list(k);e[i]-=1;d[tuple(e)]=v*k[i]
        return Poly(d)
    def __eq__(self,o):return self.terms==P(o).terms
    def __repr__(self):return f'Poly({len(self.terms)} terms)'
def P(x):return x if isinstance(x,Poly) else Poly.const(x)
X,T,A,H,V=(Poly.var(j) for j in range(5))

checks=0
def check(condition,label):
    global checks
    checks+=1
    if not condition: raise AssertionError(label)

Q=(A*H*T+2*A-H*T)*X**3+6*A*T*X**2+6*A*T**2*X+2*A**2*T**3
S=(A*H*T+2*A-H*T)*X**2+4*A*T*X+2*A*T**2
N=(H*X**2-2*A*T)*(X+T)**2
B=H*X*((H*T+2)*X+4*T)*(X+A*T)**2
NH=X*(X+T)
BH=(X+A*T)*((H*T+2)*X+2*T)

# Full exact polynomial identities: no finite-sampling assumption.
check(N.derivative()*B-N*B.derivative() ==
      2*H*T*(X+T)*(H*X+2)*(X+A*T)*Q,'W prime factorization')
check(NH.derivative()*BH-NH*BH.derivative()==T*S,'H prime factorization')
B0=(X+A*T)*(H*X+2)
check((T*X).derivative()*B0-T*X*B0.derivative()==T*(2*A*T-H*X**2),'bulk derivative')
B1=(X+T)*(H*X+2)
check((H*T*V*X**2).derivative()*B1-H*T*V*X**2*B1.derivative()==
      H*T*V*X*((H*T+2)*X+4*T),'wall derivative')
check(X*T*(X+T+H*V*X*(X+A*T)) ==
      (T*X)*(X+T)+(H*T*V*X**2)*(X+A*T),'published/split diffusivity')
check(X*T*(X+T+H*V*X*(X+A*T))-T*V*((X+T)*(X+A*T)*(H*X+2)) ==
      T*(NH-V*BH),'plateau comparison identity')

# Numerical diagnostics for two exact transition types and their boundary.
def D(x,a,h,t,w):return t*x/((x+a*t)*(h*x+2))+h*t*w*x*x/((x+t)*(h*x+2))
def Hcross(x,a,h,t):return x*(x+t)/((x+a*t)*((h*t+2)*x+2*t))
def Wstat(x,a,h,t):return (h*x*x-2*a*t)*(x+t)**2/(h*x*((h*t+2)*x+4*t)*(x+a*t)**2)
def bisect(f,lo,hi,steps=100):
    fl=f(lo)
    assert fl*f(hi)<0
    for _ in range(steps):
        mid=(lo+hi)/2
        if f(mid)*fl>0:lo=mid;fl=f(lo)
        else:hi=mid
    return (lo+hi)/2

def unique_finite_peak(a,h,t,w):
    x0=sqrt(2*a*t/h)
    c=2*a-(1-a)*h*t
    if c<0:
        q=bisect(lambda x:c*x**3+6*a*t*x*x+6*a*t*t*x+2*a*a*t**3,x0,max(2*x0,10*t))
        # The right bracket might need growth, but selected cases are bounded.
        return bisect(lambda x:Wstat(x,a,h,t)-w,x0,q)
    hi=max(2*x0,1.)
    while Wstat(hi,a,h,t)<=w:hi*=2
    return bisect(lambda x:Wstat(x,a,h,t)-w,x0,hi)

# The source's discontinuous-transition example.
a,h,t=0.5,2.0,10.0
c=2*a-(1-a)*h*t
check(c<0,'discontinuous regime')
k=-c
z=t*(2*a+sqrt(2*a*(1-a)*h*t))/k
wc=Hcross(z,a,h,t)
wlim=1/(h*t+2)
q=bisect(lambda x:c*x**3+6*a*t*x*x+6*a*t*t*x+2*a*a*t**3,z,100*t)
ws=Wstat(q,a,h,t)
check(wlim<wc<ws,'coexistence precedes spinodal')
check(isclose(wc,0.05772153925510175,rel_tol=1e-12),'exact coexistence example')
check(isclose(ws,0.06546955270989654,rel_tol=1e-12),'exact spinodal example')
check(isclose(D(z,a,h,t,wc),t*wc,abs_tol=1e-13),'exact coexistence equality')
check(isclose(Wstat(z,a,h,t),wc,abs_tol=1e-13),'coexistence stationary')
for w in [0.001,0.02,wlim,wc*0.99,wc,wc*1.01,(wc+ws)/2,ws*1.01]:
    xs=[10**(-3+i*0.01) for i in range(801)]
    vals=[D(x,a,h,t,w) for x in xs]
    bound=t*w
    if w<wc: check(max(vals)>bound,'finite region dominates plateau')
    elif w>wc:check(max(vals)<=bound+1e-7,'plateau region bounds')
for w in [wlim*0.5, (wlim+wc)*0.5, wc*0.99]:
    xm=unique_finite_peak(a,h,t,w)
    check(D(xm,a,h,t,w)>max(D(xm/1.01,a,h,t,w),D(xm*1.01,a,h,t,w)), 'finite optimum locally unique')

# At and above tricritical threshold, the stationary branch diverges
# respectively as inverse gap or inverse square root of gap.
for a,h,t in [(1.,2.,1.),(.5,2.,1.)]:
    c=2*a-(1-a)*h*t
    winf=1/(h*t+2)
    for gap in [1e-5,1e-6,1e-7]:
        x=unique_finite_peak(a,h,t,winf-gap)
        if c>0: predicted=2*t*c/((h*t+2)**2*gap)
        else:predicted=t*(1-a)*sqrt(3*a/(2*gap))
        check(abs(x/predicted-1)<.06,'continuous crossover scaling')
# Systematic diagnostics cover both types, all allowed turning-angle sectors,
# and the discontinuous metastability window. All inequalities are checked
# away from transition roundoff.
for aa in [0.15,0.35,0.65,0.9,1.0,1.6,2.0]:
    for hh in [1.1,2.0,5.0]:
        for tt in [0.2,1.0,5.0,20.0]:
            cc=2*aa-(1-aa)*hh*tt
            winf=1/(hh*tt+2)
            xzero=sqrt(2*aa*tt/hh)
            if cc>=0:
                for j in range(1,19):
                    zz=xzero*(1+j/2)
                    check(Wstat(zz,aa,hh,tt)<winf,'continuous stationary-branch envelope')
                    check(Hcross(zz,aa,hh,tt)<winf,'continuous global envelope')
                if cc>1e-8:
                    mx=unique_finite_peak(aa,hh,tt,winf*0.5)
                    check(D(mx,aa,hh,tt,winf*0.5)>tt*winf*0.5,'finite optimal transport')
            else:
                kk=-cc
                zz=tt*(2*aa+sqrt(2*aa*(1-aa)*hh*tt))/kk
                coex=Hcross(zz,aa,hh,tt)
                lo=zz
                hi=10*max(1,zz)
                while cc*hi**3+6*aa*tt*hi**2+6*aa*tt**2*hi+2*aa**2*tt**3>0:
                    hi*=2
                spinx=bisect(lambda x:cc*x**3+6*aa*tt*x*x+6*aa*tt**2*x+2*aa**2*tt**3,lo,hi)
                spin=Wstat(spinx,aa,hh,tt)
                check(winf<coex<spin and xzero<zz<spinx,'strict three-threshold ordering')
                for zz2 in [zz/3,zz/2,zz,2*zz,3*zz,10*zz]:
                    check(Hcross(zz2,aa,hh,tt)<=coex+1e-13,'exact coexistence envelope')
                check(abs(D(zz,aa,hh,tt,coex)-tt*coex)<1e-9,'coexistence level')
print(f'PASS: {checks} exact algebraic or deterministic diagnostic checks')
