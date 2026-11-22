#!/usr/bin/env python3
"""Independent numerical and finite-sample checks of the matched-pair exponential kernel."""
import itertools
import math
from functools import lru_cache
import numpy as np
from scipy.integrate import quad
from scipy.special import exp1

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def h(x, y):
    return abs(x-y)/(x+y)

def q(x):
    if x == 0.0:
        return 1.0
    if x < 70:
        return -1.0 + 2*math.exp(-x) + 2*x*math.exp(x)*(exp1(x)-2*exp1(2*x))
    # Only used for integration on 0..70, never requires unstable large arguments.
    raise ValueError('q(x) used outside verified integration range')

@lru_cache(None)
def matchings(indices):
    if not indices:
        return ((),)
    a=indices[0]
    out=[]
    for j in range(1,len(indices)):
        b=indices[j]
        rest=indices[1:j]+indices[j+1:]
        for m in matchings(rest):
            out.append(((a,b),)+m)
    return tuple(out)

def uvalue(z):
    n=len(z)
    return 2*sum(h(z[i],z[j]) for i in range(n) for j in range(i+1,n))/(n*(n-1))

def match_mean(z, matching):
    n=len(z)
    return (2/n)*sum(h(z[a],z[b]) for a,b in matching)

# Verify conditional expectation over complete perfect matchings for nonrandom vectors.
for z in [(1., 3.), (0.2, 0.8, 1.3, 10.), (0.5, 0.9, 1.4, 3., 4., 9.)]:
    m=matchings(tuple(range(len(z))))
    check(len(m)==math.factorial(len(z))//(2**(len(z)//2)*math.factorial(len(z)//2)), 'number of perfect matchings')
    vals=np.array([match_mean(z,a) for a in m])
    check(abs(np.mean(vals)-uvalue(z))<1e-14, 'permutation mean equals complete U statistic')

# Independent integral checks of the conditional kernel mean.
for x in (0.003,0.03,0.1,0.3,0.75,1.0,1.7,4.,8.,20.):
    v=quad(lambda y: h(x,y)*math.exp(-y),0,x,epsabs=2e-12)[0]
    v+=quad(lambda y: h(x,y)*math.exp(-y),x,80,epsabs=2e-12)[0]
    check(abs(v-q(x))<2e-11, 'exponential-integral expression of q(x)')

# Split of two exponentials is uniform, hence its absolute centered transform is uniform.
for p in range(1,9):
    moment=quad(lambda u: abs(2*u-1)**p,0,1,epsabs=1e-13)[0]
    check(abs(moment-1/(p+1))<1e-12, 'uniform ratio moment')

expect_q=quad(lambda x: math.exp(-x)*q(x),1e-8,60,epsabs=1e-11,limit=400)[0]+1e-8
zeta=quad(lambda x: math.exp(-x)*(q(x)-.5)**2,1e-8,60,epsabs=1e-11,limit=400)[0]+2.5e-9
check(abs(expect_q-.5)<2e-8, 'projection mean')
check(abs(zeta-0.0158672827997417)<2e-8, 'projection variance')
check(0<zeta<1/24, 'strict nondegenerate projection and remainder')

def variance_all(n):
    return (4*(n-2)*zeta+1/6)/(n*(n-1))

def variance_B(n,b):
    return variance_all(n)+(1/(6*n)-variance_all(n))/b

for n in (2,4,6,10,50,1000):
    check(abs(variance_B(n,1)-1/(6*n))<1e-15,'one matching variance')
    check(variance_all(n)<=variance_B(n,50)+1e-15,'variance floor')
for n in (4,6,10,100):
    gain1=variance_B(n,1)-variance_all(n)
    gain50=variance_B(n,1)-variance_B(n,50)
    check(abs(gain50/gain1-.98)<1e-12,'50 repetitions capture 98% of reducible variance')

check(abs(24*zeta-.380814787193801)<3e-7,'sharp asymptotic variance floor fraction')
check(abs(6*(4*zeta+(1/50)*(1/6-4*zeta))-.393198491449925)<3e-7,'50 permutation variance fraction')
check(abs(6*50*(4*zeta+(1/50)*(1/6-4*zeta))-19.6599245724963)<3e-5,'independence-based variance ratio')

# Separate simulation tests of finite-n unconditional covariance, using independently
# randomized perfect matchings on the same exponential data (the dependence is essential).
rng=np.random.default_rng(20261117)
reps=150000
for n,b in [(4,1),(4,5),(6,4),(10,6)]:
    x=rng.exponential(size=(reps,n))
    sums=np.zeros(reps)
    row=np.arange(reps)[:,None]
    for _ in range(b):
        perms=np.argsort(rng.random((reps,n)),axis=1)
        left=x[row,perms[:,::2]]
        right=x[row,perms[:,1::2]]
        sums += np.mean(np.abs(left-right)/(left+right),axis=1)
    vals=sums/b
    check(abs(float(vals.mean())-.5)<0.0015,'Monte Carlo matching mean')
    check(abs(float(vals.var())-variance_B(n,b))<0.0014,'Monte Carlo matching variance')

print('checks_passed:',checks)
print('zeta1:',format(zeta,'.15g'))
print('full_average_asymptotic_n_variance:',format(4*zeta,'.15g'))
print('single_pairing_asymptotic_n_variance:',format(1/6,'.15g'))
print('variance_fraction_infinite_permutations:',format(24*zeta,'.15g'))
print('variance_fraction_B50:',format(6*variance_B(10**9,50)*(10**9),'.15g'))
print('independence_naive_variance_multiplier_B50:',format(50*(6*(4*zeta+(1/50)*(1/6-4*zeta))),'.15g'))
