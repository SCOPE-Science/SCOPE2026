"""Stand-alone numerical/algebraic checks for directed many-loci selection laws.
Python standard library only; no infinite assertion is certified by finite tests.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import exp, gamma, log, sqrt
from random import Random
from statistics import mean


def qso_step(x):
    m=len(x)//2
    y=[]
    for i in range(m):
        j=(i+1)%m
        delta=x[2*i+1]*x[2*j]-x[2*i]*x[2*j+1]
        y.extend((x[2*i]+delta,x[2*i+1]-delta))
    return y

def beta(x):
    m=len(x)//2
    c=[x[2*i]+x[2*i+1] for i in range(m)]
    q=[x[2*i]/c[i] for i in range(m)]
    weights=[1/c[(i+1)%m] for i in range(m)]
    return sum(weights[i]*q[i] for i in range(m))/sum(weights)

for m in [3,4,7,10]:
    den=m*(m+1)//2
    c=[F(i+1,den) for i in range(m)]
    q=[F(i+1,m+2) for i in range(m)]
    x=[v for i in range(m) for v in (c[i]*q[i],c[i]*(1-q[i]))]
    b0=beta(x)
    for n in range(8):
        nxt=qso_step(x)
        assert beta(nxt)==b0
        assert all(nxt[2*i]+nxt[2*i+1]==c[i] for i in range(m))
        assert all(v>=0 for v in nxt)
        x=nxt
    # Separate row-stochastic representation on ratios.
    ratios=[x[2*i]/c[i] for i in range(m)]
    post=qso_step(x)
    for i in range(m):
        j=(i+1)%m
        assert post[2*i]/c[i] == (1-c[j])*ratios[i]+c[j]*ratios[j]
print('EXACT_INVARIANT_AND_CYCLIC_MARKOV_REDUCTION_OK')

# High precision tail identity and leading coefficient for Y=(U-1/2)/G,
# U uniform and G Gamma(shape=2,rate=1).
getcontext().prec=70
for t in [Decimal(10),Decimal(100),Decimal(1000),Decimal(10000)]:
    e=(-1/(2*t)).exp()
    tail=1-4*t+(1+4*t)*e
    assert tail>0
    relative=abs(t*t*tail-Decimal(1)/24)/(Decimal(1)/24)
    assert relative < Decimal(2)/t
print('EXACT_CRITICAL_TAIL_AND_CONSTANT_1_OVER_24_OK')

# Gamma and beta moments, independently using integration-by-parts identities.
for a in [1.25,1.5,2,3,5]:
    v=1/(4*(2*a+1))
    eg1=1/(2*a-1)
    eg2=1/((2*a-1)*(2*a-2))
    proposed=(2*a-1)/(4*(2*a+1)*(2*a-2))
    assert abs(v*eg2/eg1**2-proposed)<1e-14
print('FINITE_VARIANCE_DIRICHLET_CONSTANTS_OK')

# Independent direct-simulation spot check of conditional consensus.
rng=Random(20261106)
for m in [3,6]:
    for trial in range(6):
        g=[rng.gammavariate(2,1) for i in range(m)]
        total=sum(g)
        c=[z/total for z in g]
        q=[rng.random() for i in range(m)]
        x=[v for i in range(m) for v in (c[i]*q[i],c[i]*(1-q[i]))]
        expected=beta(x)
        for t in range(10000):
            x=qso_step(x)
        assert abs(x[0]/c[0]-expected)<2e-10
print('DIRECT_NONLINEAR_ITERATION_AGREES_WITH_CONSENSUS_OK')

# Finite-sample illustration only; not a proof of either CLT.
for a in [1.0,2.0]:
    m=3000
    trials=320
    obs=[]
    for trial in range(trials):
        g=[rng.gammavariate(2*a,1) for _ in range(m)]
        q=[rng.betavariate(a,a) for _ in range(m)]
        weights=[1/z for z in g]
        z=sum(weights[i]*q[(i-1)%m] for i in range(m))/sum(weights)
        scaled=(z-0.5)*sqrt(m/(log(m) if a==1 else 1))
        obs.append(scaled)
    theoretical=1/24 if a==1 else (2*a-1)/(4*(2*a+1)*(2*a-2))
    print('SIMULATION_ILLUSTRATION', 'a=',a,'mean=',round(mean(obs),5),
          'empirical_variance=',round(sum((z-mean(obs))**2 for z in obs)/(trials-1),5),
          'limiting_normal_variance=',round(theoretical,5))
print('DIRECTED_MANY_LOCI_VERIFICATION_OK')
