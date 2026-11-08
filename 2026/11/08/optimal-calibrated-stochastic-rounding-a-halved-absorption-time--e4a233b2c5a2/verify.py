"""Exact checks for finite-grid state-dependent stochastic-rounding allocation.

This standalone verifier uses only the Python standard library.
Analytic proofs of optimality, asymptotics and the central limit theorem
are contained in RESULT.md, not inferred from these finite checks.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, log, sqrt

checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def waterfill(M, B):
    B=F(B)
    assert M>=2 and F(0)<B<F(M-1,2)
    for j in range(1,M):
        c=(B+F(j*(j+1),2*M))/j
        if F(j,M)<=c<=F(j+1,M):
            p=[max(F(k,M),c) for k in range(1,M+1)]
            return c,j,p
    raise ArithmeticError('No water-filling threshold found')

def moments_by_geometric_sum(p):
    return (sum((1/v for v in p),F(0)),
            sum(((1-v)/(v*v) for v in p),F(0)))

def moments_by_markov_first_step(p):
    # Independent first-step check for the pure-death chain.
    m=q=F(0)
    for v in p:
        old=m
        m=old+1/v
        q=(1+2*((1-v)*m+v*old)+v*q)/v
    return m,q-m*m

for M in range(2,13):
    for B in (F(1,10),F(1,2),F(3,4)):
        if B>=F(M-1,2):
            continue
        c,j,p=waterfill(M,B)
        check(sum((v-F(i+1,M) for i,v in enumerate(p)),F(0))==B,'exact budget')
        check(all(F(i+1,M)<=v<=1 for i,v in enumerate(p)),'feasible probabilities')
        check(F(j,M)<=c<=F(j+1,M),'active set boundary')
        check(moments_by_geometric_sum(p)==moments_by_markov_first_step(p),'Markov moments')
        for i in range(j):
            check(p[i]==c,'equal positive-bias hazards')
        for i in range(j,M):
            check(p[i]>=c,'larger baseline hazards unchanged')

# Unbiased chain exactly equals the coupon collector's missing-coupon count.
M=4
D={M:F(1)}
for t in range(1,13):
    nxt={i:F(0) for i in range(M+1)}
    for k,w in D.items():
        if k==0:
            nxt[0]+=w
        else:
            prob=F(k,M)
            nxt[k-1]+=w*prob
            nxt[k]+=w*(1-prob)
    D=nxt
    surj=sum((-1)**j*comb(M,j)*(M-j)**t for j in range(M+1))
    check(D[0]==F(surj,M**t),'exact coupon-collector completion CDF')

# Half-unit total probability-perturbation budget.
c,j,p=waterfill(100,F(1,2))
check(c==F(21,200) and j==10,'M=100 exact solution')
opt=moments_by_geometric_sum(p)[0]
uniform=[F(k,100)+F(1,198) for k in range(1,100)]+[F(1)]
check(sum((uniform[k-1]-F(k,100) for k in range(1,101)),F(0))==F(1,2),'equal uniform budget')
check(opt<moments_by_geometric_sum(uniform)[0],'strict improvement over uniform')
check(F(320)<opt<F(322),'100-state benchmark range')

# Exhaustive rational-mesh comparison (a check, not a continuous proof).
M=4; B=F(1,2); _,_,p=waterfill(M,B); target=moments_by_geometric_sum(p)[0]
for a in product(range(6),repeat=3):
    b=[F(t,10) for t in a]+[F(0)]
    if sum(b)>B: continue
    rates=[F(k,M)+b[k-1] for k in range(1,M+1)]
    if any(rate>1 for rate in rates): continue
    check(target<=moments_by_geometric_sum(rates)[0],'grid competitor')

# Convergence toward the proved mean and variance asymptotic constants.
B=F(1,2)
for M in (100,1000,10000):
    c,j,p=waterfill(M,B)
    mean,variance=moments_by_geometric_sum(p)
    check(abs(float(mean)/M-.5*log(M)-1)<12/sqrt(M),'mean limit')
    check(abs(float(variance)/M**1.5-2)<9/sqrt(M)**.5,'variance limit')
    check(abs(float(c)*sqrt(M)-1)<2/sqrt(M),'threshold limit')

print('PASS',checks,'exact-rational and asymptotic comparison assertions')
print('M=100, B=1/2: c=21/200, j=10')
print('Eoptimal=',float(opt),'Euniform=',float(moments_by_geometric_sum(uniform)[0]))
