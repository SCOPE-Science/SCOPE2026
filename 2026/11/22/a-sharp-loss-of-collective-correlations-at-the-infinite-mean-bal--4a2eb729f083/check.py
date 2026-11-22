"""Reproducible checks for independent Beta cloud and finite-mean covariance.
All infinite-time claims are proved analytically in RESULT.md; these checks are finite computations.
"""
from fractions import Fraction
import math, random

def moment_identity(n, alpha, ks):
    gamma = n*alpha
    prod = math.prod((alpha/(alpha+k) for k in ks))
    k = sum(ks)
    phase = gamma/(gamma+k)
    ratios = sum(math.prod(alpha/(alpha+ks[i]) for i in range(n) if i!=j) for j in range(n))/n
    assert math.isclose(phase*ratios, prod, rel_tol=2e-14, abs_tol=2e-14)
    return prod

for n in [2,3,4,6]:
    for alpha in [0.11,0.21,0.41,0.79]:
        for ks in [(i*3+j)%5 for i in range(n) for j in []]: pass
        for k0 in range(125):
            ks = tuple((k0//(5**j))%5 for j in range(n))
            moment_identity(n,alpha,ks)

# Independent computation of finite-mean covariance from an equilibrium age law.
for n,alpha in [(2,0.8),(3,0.5),(5,0.3)]:
    g=n*alpha
    assert g>1
    meanz=(g+1)/(2*g)
    secondz=(g+2)/(3*g)
    cov=(alpha/(alpha+1))**2*(secondz-meanz**2)
    closed=(alpha/(alpha+1))**2*(g-1)*(g+3)/(12*g*g)
    assert math.isclose(cov,closed,rel_tol=1e-13)
    assert closed>0

# Direct renewal simulation of the physical reset protocol (rather than just limit laws).
random.seed(271828)
n=2; alpha=0.24; t=1000000.; trials=1600
sumx=[0.,0.]; sumxx=0.; sumx2=0.; total_cycles=0
for _ in range(trials):
    s=0.
    while True:
        v=[random.random()**(1/alpha) for _ in range(n)]
        dur=1/max(v)
        if s+dur>=t:
            age=t-s
            xx=[1-age*vv for vv in v]
            assert min(xx)>=-1e-10 and max(xx)<=1+1e-10
            sumx[0]+=xx[0]; sumx[1]+=xx[1]
            sumxx+=xx[0]*xx[1]
            sumx2+=xx[0]*xx[0]
            break
        s+=dur
        total_cycles+=1
means=[w/trials for w in sumx]
cov=sumxx/trials-means[0]*means[1]
expectation=1/(alpha+1)
second=2/((alpha+1)*(alpha+2))
assert abs(means[0]-expectation)<0.06, (means[0],expectation)
assert abs(means[1]-expectation)<0.06
assert abs(sumx2/trials-second)<0.06
assert abs(cov)<0.045, cov
print('PASS: 2000+ analytic mixed-moment identities, 3 covariance identities, and actual finite-time renewal simulation.')
print('Finite-time trials', trials, 'mean position', means, 'covariance',round(cov,5), 'completed cycles',total_cycles)
