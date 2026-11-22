"""Deterministic diagnostic checks for the two-season fixed-effort yield theorem.

Python 3 standard library only. The infinite-domain proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose, log, exp
import random

TESTS = 0

def ck(condition, description='identity'):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(f'{description}, assertion {TESTS}')

def direct_data(r0,r1,S,K0,K1,t):
    p=r0*r1*S
    q=p-1
    x0=q*K0*K1/(K1+r0*t*K0)
    x1=t*q*K0*K1/(r1*S*K1+t*K0)
    s1=S/t
    f0=r0*x0/(1+x0/K0)
    f1=r1*x1/(1+x1/K1)
    c0=(1-t)*f0
    c1=(1-s1)*f1
    return x0,x1,c0+c1

def formula_y(r0,r1,S,K0,K1,t):
    q=r0*r1*S-1
    return q*K0*K1*((1-t)/(r1*S*K1+t*K0)+(t-S)/(S*(K1+r0*t*K0)))

def policy(r0,r1,S,K0,K1):
    q=r0*r1*S-1
    assert q>0
    L=lambda t:(K1+r0*K0*t)/(r1*S*K1+K0*t)
    threshold=sqrt((K1+r0*S*K0)/(S*(K0+r1*S*K1)))
    if L(S)>=threshold:
        return S, 'first-only'
    if L(1)<=threshold:
        return 1., 'second-only'
    t=K1*(threshold*r1*S-1)/(K0*(r0-threshold))
    return t, 'interior'

rng=random.Random(20261115)
for _ in range(1200):
    r0=exp(rng.uniform(.05,2.2)); r1=exp(rng.uniform(.05,2.2))
    S=exp(-rng.uniform(.002, .95*(log(r0)+log(r1))))
    K0=exp(rng.uniform(-3,3)); K1=exp(rng.uniform(-3,3))
    Q=r0*r1*S-1
    t,kind=policy(r0,r1,S,K0,K1)
    ck(S-1e-12<=t<=1+1e-12,'optimal feasible')
    x0,x1,y=direct_data(r0,r1,S,K0,K1,t)
    ck(isclose(x1,t*r0*x0/(1+x0/K0),rel_tol=4e-11),'first-season cycle')
    ck(isclose(x0,(S/t)*r1*x1/(1+x1/K1),rel_tol=4e-11),'second-season cycle')
    ck(isclose(y,formula_y(r0,r1,S,K0,K1,t),rel_tol=8e-11,abs_tol=2e-11),'yield identity')
    for j in range(41):
        u=S+(1-S)*j/40
        yu=formula_y(r0,r1,S,K0,K1,u)
        ck(yu<=y+3e-10*(1+y),'global grid maximum')
        if kind=='interior':
            regret= Q**2*(K0*K1)**2*(K0+r1*S*K1)*(u-t)**2/(
                (r1*S*K1+K0*t)**2*(r1*S*K1+K0*u)*(K1+r0*K0*u))
            ck(isclose(y-yu,regret,rel_tol=4e-6,abs_tol=3e-9*(1+y)),'exact regret')

for _ in range(200):
    r0=F(rng.randint(2,8),1);r1=F(rng.randint(2,8),1)
    S=F(rng.randint(1,8),rng.randint(9,17))
    if r0*r1*S<=1 or S>=1: continue
    K0=F(rng.randint(1,16),rng.randint(1,5))
    K1=F(rng.randint(1,16),rng.randint(1,5))
    t=S+(1-S)*F(rng.randint(0,8),9)
    x0,x1,y=direct_data(r0,r1,S,K0,K1,t)
    ck(y==formula_y(r0,r1,S,K0,K1,t),'exact rational yield')
    ck(x1==t*r0*x0/(1+x0/K0),'exact rational recurrence 0')
    ck(x0==(S/t)*r1*x1/(1+x1/K1),'exact rational recurrence 1')

r0=r1=F(4); S=F(1,5); K0=F(10);K1=F(1)
t,kind=policy(float(r0),float(r1),float(S),float(K0),float(K1))
ck(kind=='first-only' and abs(t-.2)<1e-12,'corner example optimality')
ck(formula_y(r0,r1,S,K0,K1,S)==F(44,7),'corner exact yield')
r0=r1=4.;S=.2;K0=K1=1.
t,kind=policy(r0,r1,S,K0,K1)
ck(kind=='interior' and isclose(t,sqrt(S),rel_tol=1e-12),'symmetric optimum')

# A fixed effort only affects extinction through the two-season low-density multiplier.
for _ in range(100):
    r0=exp(rng.uniform(.05,2));r1=exp(rng.uniform(.05,2))
    S=exp(-rng.uniform(.05,3))
    K0=exp(rng.uniform(-2,2));K1=exp(rng.uniform(-2,2))
    for t in [S,sqrt(S),1.]:
        s0=t;s1=S/t
        x=1.0
        for i in range(2500):
            x=s0*r0*x/(1+x/K0)
            x=s1*r1*x/(1+x/K1)
        if r0*r1*S<.95:
            ck(x<1e-12,'extinction when multiplier below one')
        elif r0*r1*S>1.05:
            q=r0*r1*S-1
            target=q*K0*K1/(K1+r0*t*K0)
            ck(isclose(x,target,rel_tol=1e-8,abs_tol=1e-10),'globally attracting two-cycle')

print(f'PASS: {TESTS} deterministic diagnostic assertions. Analytic proof required for universal claims.')
