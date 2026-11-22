"""Standalone numerical checks of a two-date, pooled two-founder introduction theorem.

Run: python verify.py
The proof for all real parameters is analytical; these checks are finite tests.
"""
from decimal import Decimal, getcontext
from math import exp, cosh, sinh, tanh
from itertools import product

getcontext().prec = 60
checks = 0


def check(truth, description='assertion'):
    global checks
    assert truth, description
    checks += 1


def F(t):
    return -__import__('math').expm1(-t) - t * exp(-t)


def prob(B, x, lo, hi, rho):
    mean = (lo + hi) * B / 2
    swing = (hi - lo) * (2 * x - B) / 2
    return ((1 + rho) * (F(hi * B) + F(lo * B))
            + (1 - rho) * (F(mean + swing) + F(mean - swing))) / 4


def original_sum(B, x, lo, hi, rho):
    w_same = (1 + rho) / 4
    w_diff = (1 - rho) / 4
    return (w_same * F(hi * B) + w_same * F(lo * B)
            + w_diff * F(hi * x + lo * (B-x))
            + w_diff * F(lo * x + hi * (B-x)))


def H(B, lo, hi):
    alpha = (hi+lo)/2
    beta = (hi-lo)/2
    t = beta*B
    if t < 1e-4:
        # t*coth(t/2) = 2 + t^2/6 - t^4/360 + ...
        return 1 - alpha*B + t*t/6 - t**4/360 + t**6/15120
    return t / tanh(t/2) - 1 - alpha * B


def threshold(lo, hi):
    left, right = 1/((lo+hi)/2), 1/lo
    check(H(left, lo, hi)>0, 'left bound')
    check(H(right, lo, hi)<0, 'right bound')
    for _ in range(90):
        mid=(left+right)/2
        if H(mid,lo,hi)>0: left=mid
        else: right=mid
    return (left+right)/2


# Direct four-environment sum equals hyperbolic-pair representation.
for lo in [0.05, .2, .5, .8]:
    for hi in [.81, .95, 1.0]:
        if lo >= hi: continue
        for rho in [-.9, -.25, 0, .5, .99]:
            for B in [.05,.3,1,2,5,12]:
                for k in range(21):
                    x=B*k/20
                    check(abs(prob(B,x,lo,hi,rho)-original_sum(B,x,lo,hi,rho))<3e-13,
                          'four-state equality')

# Global optimization against 100-point grids on both sides of each threshold.
for lo,hi in [(.01,.9),(.1,.9),(.25,.75),(.6,.95),(.02,.03),(.8,1)]:
    Bcrit=threshold(lo,hi)
    for mult in [.01,.1,.6,.8,.99,1.01,1.2,2,5,10]:
        B=Bcrit*mult
        hsign=H(B,lo,hi)
        check((hsign>0)==(B<Bcrit), 'unique-budget-sign')
        for rho in [-.8,0,.4,.95]:
            endpoint=prob(B,0,lo,hi,rho)
            center=prob(B,B/2,lo,hi,rho)
            target=endpoint if mult<1 else center
            check(target>=(center if mult<1 else endpoint)-1e-12,
                  'endpoint center dominance')
            for j in range(101):
                x=B*j/100
                check(prob(B,x,lo,hi,rho)<=target+8e-12,
                      'global against finite grid')

# A uniquely interior strict minimum can occur, never an interior global maximum.
for m in [0.1,.5,.99,1,1.01,1.5,2,5,12]:
    # t/tanh(t) rises continuously from 1.
    prev=1.0
    for i in range(1,1000):
        t=i/100.0
        ratio=t/tanh(t)
        check(ratio>prev-1e-13,'monotone root function')
        prev=ratio
        # exact derivative identity for F(m+t)+F(m-t) as real analytic function
        if t<=m:
            deriv=(m+t)*exp(-m-t)-(m-t)*exp(-m+t)
            fact=2*exp(-m)*(t*cosh(t)-m*sinh(t))
            check(abs(deriv-fact)<1e-9,'derivative factorization')

# At least-one-founder rule is strictly center-optimal for all mismatched conditions.
for lo,hi,rho,B in product([.1,.35],[.6,1],[-.5,.5],[.1,.5,2,5]):
    if lo>=hi: continue
    q=lambda x: ((1+rho)*(2-exp(-lo*B)-exp(-hi*B))
        +(1-rho)*(2-exp(-(lo*x+hi*(B-x)))-exp(-(hi*x+lo*(B-x)))))/4
    best=q(B/2)
    for j in range(51):
        check(q(B*j/50)<=best+1e-12,'one-founder concavity')

# High-precision example including exact location of the crossing, with bounds.
D=Decimal
lo,hi=D(1)/4,D(3)/4
alpha,beta=(lo+hi)/2,(hi-lo)/2

def Hd(B):
    v=beta*B
    ev=v.exp()
    return v*(ev+1)/(ev-1)-1-alpha*B

L,R=D('2'),D('3')
for _ in range(210):
    mid=(L+R)/2
    if Hd(mid)>0:L=mid
    else:R=mid
Bstar=(L+R)/2
check(L>=D(2) and R<D(3),'threshold interval')
check(abs(Hd(Bstar))<D('1e-52'),'threshold precision')

def fd(z):
    return 1-(1+z)*(-z).exp()

def pd(B,x):
    rho=D(1)/2
    return ((1+rho)*(fd(hi*B)+fd(lo*B))
      +(1-rho)*(fd(hi*x+lo*(B-x))+fd(lo*x+hi*(B-x))))/4
for B in [D(2),D(4)]:
    gap=pd(B,D(0))-pd(B,B/2)
    check((gap>0)==(B<Bstar),'example signs')
    print('B=',B,'all=',pd(B,0),'half=',pd(B,B/2),'gap=',gap)
print('B_star=',Bstar)
print('All',checks,'finite checks PASSED (not a substitute for proof).')
