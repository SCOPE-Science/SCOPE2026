"""Exact and numerical verification of a switching-contact star SIR law."""
import math
from fractions import Fraction
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
from scipy.special import gammaln

# Rates: initially stationary off->on a, on->off b, recovery mu, transmission lam.
a=b=lam=mu=1.0
s=a+b
p=a/s
r=mu*(s+mu)/(a+mu)
w=a*(s+mu)/(s*(a+mu))
d0=1-w
D=math.sqrt((s+lam)**2-4*a*lam)
rho=(s+lam-D)/2
R=(s+lam+D)/2
c=(R-p*lam)/D
d=1-c
assert abs(r-1.5)<1e-12 and abs(d0-.25)<1e-12
assert 0<rho<lam*p<lam*(a+mu)/(s+mu)
assert c>0 and d>0

def u(t):
    return c*math.exp(-rho*t)+d*math.exp(-R*t)

def ni_all(k):
    return w*math.exp(math.lgamma(1+r/lam)+math.lgamma(k+1)-math.lgamma(k+1+r/lam))

def ni_none(k):
    return d0+w*r/(r+k*lam)

def li_all(k):
    return quad(lambda t:mu*math.exp(-mu*t)*(-math.expm1(math.log(u(t))))**k,0,max(60, 3*math.log(k+1)/rho),epsabs=2e-12,epsrel=2e-11)[0]

def li_none(k):
    return quad(lambda t: mu*math.exp(-mu*t)*u(t)**k,0,1,epsabs=2e-13,epsrel=2e-11)[0]+quad(lambda t: mu*math.exp(-mu*t)*u(t)**k,1,60,epsabs=2e-13,epsrel=2e-11)[0]

# Independent finite-state CTMC linear systems: exact for a=b=lam=mu=1.
import sympy as sp

def hit_probabilities(states, init, transitions, k):
    idx={v:i for i,v in enumerate(states)}
    mat=sp.zeros(len(states))
    rhs_all=sp.zeros(len(states),1)
    rhs_none=sp.zeros(len(states),1)
    for state,i in idx.items():
        outs=transitions(state)
        total=sum(rate for nxt,rate in outs)
        mat[i,i]=total
        for nxt,rate in outs:
            if nxt[0]=='recover':
                if nxt[1]==k: rhs_all[i]+=rate
                if nxt[1]==0: rhs_none[i]+=rate
            else:
                mat[i,idx[nxt]]-=rate
    all_v=mat.inv()*rhs_all
    none_v=mat.inv()*rhs_none
    return sp.simplify(sum(prob*all_v[idx[st]] for st,prob in init)),sp.simplify(sum(prob*none_v[idx[st]] for st,prob in init))

for k in range(2,6):
    st=[(j,h) for j in range(k+1) for h in (0,1)]
    def tr(z):
        j,h=z
        out=[(('recover',j),sp.Integer(1))]
        if h==0: out.append(((j,1),sp.Integer(1)))
        else: out.append(((j,0),sp.Integer(1)))
        if j<k and h:out.append(((j+1,1),sp.Integer(k-j)))
        return out
    ni_a,ni_n=hit_probabilities(st,[((0,0),sp.Rational(1,2)),((0,1),sp.Rational(1,2))],tr,k)
    # LI count susceptible off x, on y, z=k-x-y already infected.
    st2=[(x,y) for x in range(k+1) for y in range(k-x+1)]
    def tr2(z):
        x,y=z;j=k-x-y
        out=[(('recover',j),sp.Integer(1))]
        if x:out.append(((x-1,y+1),sp.Integer(x)))
        if y:out.append(((x+1,y-1),sp.Integer(y)))
        if y:out.append(((x,y-1),sp.Integer(y)))
        return out
    init2=[((k-y,y),sp.Rational(math.comb(k,y),2**k)) for y in range(k+1)]
    li_a,li_n=hit_probabilities(st2,init2,tr2,k)
    print('k',k,'CTMC_NI',ni_a,ni_n,'CTMC_LI',li_a,li_n)
    assert abs(float(ni_a)-ni_all(k))<1e-11
    assert abs(float(ni_n)-ni_none(k))<1e-11
    assert abs(float(li_a)-li_all(k))<1e-10
    assert abs(float(li_n)-li_none(k))<1e-10
    assert ni_a>li_a and ni_n>li_n

for k in [20,100,500,2000]:
    x=ni_all(k);y=li_all(k)
    assert x>y
    cn=x*k**(r/lam)/(w*math.gamma(1+r/lam))
    cl=y*k**(mu/rho)/(math.gamma(1+mu/rho)*c**(-mu/rho))
    print('asymptotic',k,'ni',x,'li',y,'constants',cn,cl,'none',ni_none(k),li_none(k))
assert abs(ni_none(500)-.25)<.003
assert abs(li_none(2000)*2000-2)<.05
print('PASS: exact independent CTMC, strict extremes, large-degree limits and constants')

# Non-symmetric positive-rate tests, with a fresh exact-rational finite-state
# construction independent of the closed formulas above.
for aa,bb,ll,mm in [(1,2,3,2),(3,1,2,5),(2,4,1,3)]:
    aa,bb,ll,mm=map(sp.Integer,(aa,bb,ll,mm))
    k=3
    states_ni=[(j,h) for j in range(k+1) for h in (0,1)]
    def tn(z):
        j,h=z
        out=[(('recover',j),mm)]
        out.append(((j,1),aa) if h==0 else ((j,0),bb))
        if j<k and h:out.append(((j+1,1),ll*(k-j)))
        return out
    pi=aa/(aa+bb)
    na,nn=hit_probabilities(states_ni,[((0,0),1-pi),((0,1),pi)],tn,k)
    states_li=[(x,y) for x in range(k+1) for y in range(k-x+1)]
    def tl(z):
        x,y=z;j=k-x-y
        out=[(('recover',j),mm)]
        if x:out.append(((x-1,y+1),aa*x))
        if y:out.append(((x+1,y-1),bb*y))
        if y:out.append(((x,y-1),ll*y))
        return out
    init=[((k-y,y),sp.binomial(k,y)*pi**y*(1-pi)**(k-y)) for y in range(k+1)]
    la,ln=hit_probabilities(states_li,init,tl,k)
    a0,b0,l0,m0=map(float,(aa,bb,ll,mm))
    ss=a0+b0; rr=m0*(ss+m0)/(a0+m0)
    ww=a0*(ss+m0)/(ss*(a0+m0)); dd=1-ww
    pr=a0/ss
    delta=math.sqrt((ss+l0)**2-4*a0*l0)
    slow=(ss+l0-delta)/2; fast=(ss+l0+delta)/2
    cc=(fast-l0*pr)/delta
    def uu(t):return cc*math.exp(-slow*t)+(1-cc)*math.exp(-fast*t)
    assert abs(float(na)-ww*math.exp(math.lgamma(1+rr/l0)+math.lgamma(k+1)-math.lgamma(k+1+rr/l0)))<1e-11
    assert abs(float(nn)-(dd+ww*rr/(rr+k*l0)))<1e-11
    la2=quad(lambda t:m0*math.exp(-m0*t)*(1-uu(t))**k,0,40,epsabs=1e-12)[0]
    ln2=quad(lambda t:m0*math.exp(-m0*t)*uu(t)**k,0,40,epsabs=1e-12)[0]
    assert abs(float(la)-la2)<1e-11
    assert abs(float(ln)-ln2)<1e-11
    assert na>la and nn>ln
    assert rr/l0 < m0/slow
    print('non-symmetric exact CTMC rates',tuple(map(int,(aa,bb,ll,mm))),'NI',na,nn,'LI',la,ln)
print('PASS: heterogeneous positive-rate finite-state checks')
