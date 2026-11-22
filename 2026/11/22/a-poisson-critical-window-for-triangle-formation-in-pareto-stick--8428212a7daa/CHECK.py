"""Reproducible finite checks for a rare-Pareto-triangle point-process theorem.

The infinite-parameter limits require the separate analytic proof.
"""
import itertools
import math
from scipy.integrate import quad
import numpy as np

N = 0

def check(ok, message):
    global N
    assert bool(ok), message
    N += 1

C = math.pi**2 / 12
D = 3 * float(__import__('scipy').special.zeta(3, 1)) / 4

def one_prob(beta, gamma):
    val, err = quad(lambda x: beta * x**(beta-1) * (-math.expm1(-gamma * math.log1p(x))), 0, 1, epsabs=2e-11, limit=180)
    return val

for n in range(3, 9):
    for sample in itertools.combinations_with_replacement(range(1, 9), n):
        by_all = all(sample[k] >= sample[i] + sample[j] for i in range(n) for j in range(i+1,n) for k in range(j+1,n))
        by_adj = all(sample[i+2] >= sample[i+1] + sample[i] for i in range(n-2))
        check(by_all == by_adj, (n,sample))

for n in [3, 4, 6, 13, 40]:
    for alpha in [.0003, .001, .02, .14]:
        betas = [(n-i)*alpha for i in range(1,n)]
        for i in range(n-2):
            a,b = betas[i:i+2]
            q = one_prob(a,b)
            target = C*a*b
            err_bound = D*a*a*b + .5*math.log(2)*C*a*b*b
            check(0<=q<=target+1e-12,(n,alpha,i,'upper',q,target))
            check(abs(q-target)<=err_bound+1e-12,(n,alpha,i,'error',q,target,err_bound))

for n in (20,80,300,1000):
    alpha=math.sqrt(3/n**3)
    approx=C*alpha**2*n*(n-1)*(n-2)/3
    check(approx <3*C/3,('Riemann',n,approx))
    check(abs(approx -C*3/3)<=15/n,('rate',n,approx))

# An adjacent intersection may only occur when both consecutive constraints fail.
for n in (5,8,11):
    for alpha in (.01,.1):
        b=[(n-i)*alpha for i in range(1,n)]
        for i in range(n-3):
            a,bb,c=b[i:i+3]
            prob,_=quad(lambda x: a*x**(a-1)*quad(lambda y:bb*y**(bb-1)*(-math.expm1(-c*math.log1p(y))),1/(1+x),1,epsabs=3e-10)[0],0,1,epsabs=1e-9,limit=100)
            check(prob <= math.log(2)*c*one_prob(a,bb)+1e-10,(n,i,alpha,prob))

# Deterministic seeded cross-check of convergence; this is not a proof.
rng=np.random.default_rng(20261120)
for n in (180,450):
    alpha=math.sqrt(3/n**3)
    b=(n-np.arange(1,n))*alpha
    gaps=rng.exponential(size=(9000,n-1))/b
    ratios=np.exp(-gaps)
    total=(ratios[:,1:]*(1+ratios[:,:-1])>1).sum(axis=1)
    predicted=math.pi**2*3/36
    check(abs(float(total.mean())-predicted)<.21,(n,total.mean(),predicted))
    check(abs(float(np.mean(total==0))-math.exp(-predicted))<.12,(n,np.mean(total==0)))

print('PASS',N,'deterministic/seeded checks')
