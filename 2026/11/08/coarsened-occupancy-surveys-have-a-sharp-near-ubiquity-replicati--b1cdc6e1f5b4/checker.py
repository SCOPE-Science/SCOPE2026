"""Exact finite checks and numerical stress tests for occupancy-survey information."""
from fractions import Fraction as F
from itertools import product
from math import comb, log, exp

checks=0

def eq(a,b,label=''):
    global checks
    checks+=1
    if a!=b: raise AssertionError((label,a,b))

def ok(cond,label=''):
    global checks
    checks+=1
    if not cond: raise AssertionError(label)

def agg_info(t,p,f,psi):
    a=1-p;b=1-f
    u=psi*a**t+(1-psi)*b**t
    delta=b**t-a**t
    return delta*delta/(u*(1-u))

def full_info(t,p,f,psi):
    result=F(0)
    for k in range(t+1):
        x=p**k*(1-p)**(t-k)
        y=f**k*(1-f)**(t-k)
        result+=comb(t,k)*(x-y)**2/(psi*x+(1-psi)*y)
    return result

for p,f in [(F(2,3),F(1,4)),(F(4,5),F(3,5)),(F(7,10),F(2,5))]:
    ok(0<f<p<1)
    for t in range(1,7):
        ps1=0; ps0=0; calc=0
        for yy in product((0,1),repeat=t):
            k=sum(yy)
            x=p**k*(1-p)**(t-k)
            y=f**k*(1-f)**(t-k)
            ps1+=x;ps0+=y
            calc+=(x-y)**2/(F(2,3)*x+F(1,3)*y)
        eq(ps1,F(1),'normalization under presence')
        eq(ps0,F(1),'normalization under absence')
        eq(calc,full_info(t,p,f,F(2,3)),'Fisher from full binary histories')
        eq(full_info(t,p,f,F(1)),(f*f/p+(1-f)**2/(1-p))**t-1,'boundary chi square')
        eq(agg_info(t,p,f,F(2,3)),( (1-f)**t-(1-p)**t )**2/((F(2,3)*(1-p)**t+F(1,3)*(1-f)**t)*(1-(F(2,3)*(1-p)**t+F(1,3)*(1-f)**t))), 'aggregate Fisher')
        ok(full_info(t,p,f,F(2,3))>=agg_info(t,p,f,F(2,3)),'data processing')
        if t>=2: ok(full_info(t,p,f,F(2,3))>agg_info(t,p,f,F(2,3)),'strict loss')
        else: eq(full_info(t,p,f,F(2,3)),agg_info(t,p,f,F(2,3)),'one read equality')

# Exact estimator variance checked via an independent binomial calculation.
for p,f,psi in [(F(3,5),F(1,10),F(9,10)),(F(4,5),F(3,5),F(999,1000))]:
    for t in range(1,10):
        a,b=1-p,1-f
        qp=1-a**t; qf=1-b**t
        u=psi*a**t+(1-psi)*b**t
        theta=1-u
        v=(theta*(1-theta))/(qp-qf)**2
        val1=(1-qf)/(qp-qf)
        val0= -qf/(qp-qf)
        eq(theta*val1+(1-theta)*val0,psi,'estimator expectation')
        eq(theta*(val1-psi)**2+(1-theta)*(val0-psi)**2,v,'estimator variance')

# Validate near-boundary lattice asymptotic in several parameter regimes.
def H(t,p,f,eps):
    a,b=1-p,1-f
    u=(1-eps)*a**t+eps*b**t
    return t*u*(1-u)/(b**t-a**t)**2
for p,f in [(0.6,0.1),(0.7,0.4),(0.8,0.5)]:
    a,b=1-p,1-f
    assert a<b*b
    la=log(b/a);mu=-log(b);nu=log(b*b/a)
    for eps in [1e-5,1e-7,1e-9]:
        L=log(1/eps)
        scores=[(H(t,p,f,eps),t) for t in range(1,100)]
        value,t=min(scores)
        x=L/la
        phase=x-int(x)
        Phi=min(exp(mu*(j-phase))+exp(-nu*(j-phase)) for j in range(-20,21))
        approx=(L/la)*eps**(nu/la)*Phi
        ok(abs(t-x)<6,'logarithmic replication window')
        ok(0.8<value/approx<1.40,'lattice asymptotic finite check')
for p,f in [(0.8,0.6),(0.5,0.4)]:
    a,b=1-p,1-f
    ok(a>=b*b,'nondiscrimination regime')
    for eps in [0.01,0.0001,0.000001]:
        _,t=min((H(k,p,f,eps),k) for k in range(1,120))
        eq(t,1,'bounded-optimum example')
print('PASS',checks,'exact and numerical assertions')
