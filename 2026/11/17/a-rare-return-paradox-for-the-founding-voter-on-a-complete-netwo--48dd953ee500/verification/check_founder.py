"""Exact labelled-state cross-check for the founder flip theorem.
No external files or services required beyond NumPy and SciPy.
"""
from fractions import Fraction
from math import comb, sqrt, factorial
import numpy as np
from scipy.sparse import dok_matrix, csc_matrix
from scipy.sparse.linalg import spsolve


def laguerre_at_minus_one(k):
    return sum(Fraction(comb(k,j), factorial(j)) for j in range(k+1))


def exact_recurrence(n):
    u1, u2 = Fraction(1), Fraction(2)
    if n==2: return Fraction(1,2)
    for j in range(2,n):
        u1,u2 = u2,2*u2-Fraction(j-1,j)*u1
    return 1/u2


def labelled_check(n):
    full=(1<<n)-1
    states=list(range(1,full))
    ix={v:i for i,v in enumerate(states)}
    Q=dok_matrix((len(states),len(states)),dtype=float)
    root_intensity=np.zeros(len(states))
    for x in states:
        i=ix[x]
        for v in range(n):
            bit=(x>>v)&1
            opp=sum(((x>>j)&1)!=bit for j in range(n) if j!=v)
            rate=opp/(n-1)
            if not rate:continue
            y=x^(1<<v)
            Q[i,i]+=rate
            if y in ix:Q[i,ix[y]]-=rate
            if v==0:root_intensity[i]+=rate
    e=spsolve(csc_matrix(Q),root_intensity)

    # Kill when the founder changes, and reward hitting all 1.
    keep=[x for x in range(1,full) if x&1]
    ik={v:i for i,v in enumerate(keep)}
    K=dok_matrix((len(keep),len(keep)),dtype=float)
    b=np.zeros(len(keep))
    for x in keep:
        i=ik[x]
        for v in range(n):
            bit=(x>>v)&1
            opp=sum(((x>>j)&1)!=bit for j in range(n) if j!=v)
            rate=opp/(n-1)
            if not rate:continue
            y=x^(1<<v)
            K[i,i]+=rate
            if y==full:b[i]+=rate
            elif y in ik:K[i,ik[y]]-=rate
    p=spsolve(csc_matrix(K),b)
    return float(e[ix[1]]),float(p[ik[1]])

for n in range(2,10):
    exact=float(exact_recurrence(n))
    expectation=2*(n-1)/(n+2)
    E,P=labelled_check(n)
    assert abs(E-expectation)<1e-10,(n,E,expectation)
    assert abs(P-exact)<1e-10,(n,P,exact)
    print(f'n={n}: E[flips]={E:.12f}, P(no flips)={P:.12f}, exact-matches=True')

print('All exact analytic/labelled-state cross-checks passed.')
for n in (100,10000,1000000):
    K=int(sqrt(n))
    bound=1/K+(K-1)/(2*(n-K))
    print(f'n={n}: proved P(any upward founder flip) <= {bound:.9f}; E[upward]={((n-1)*(n-2)/(2*n*(n+2))):.9f}')
# Independent exact type/count aggregation for the probability of a first upward founder change.
from scipy.sparse import lil_matrix

def upward_event_probability(n):
    states=[(h,j) for h in (0,1) for j in range(n) if (h,j)!=(0,0) and (h,j)!=(1,n-1)]
    ix={s:i for i,s in enumerate(states)}
    Q=lil_matrix((len(states),len(states)),dtype=float)
    b=np.zeros(len(states))
    for (h,j),i in ix.items():
        # other sites copy another opinion: either the founder or an opposite other
        total=j+h
        births=(n-1-j)*total/(n-1)
        deaths=j*(n-total)/(n-1)
        founder_rate=(n-1-j)/(n-1) if h else j/(n-1)
        for target,rate in [((h,j+1),births),((h,j-1),deaths),((1-h,j),founder_rate)]:
            if rate==0:continue
            Q[i,i]+=rate
            if h==0 and target[0]==1: b[i]+=rate
            elif target in ix:Q[i,ix[target]]-=rate
    return float(spsolve(csc_matrix(Q),b)[ix[1,0]])

for n in range(3,18):
    a=upward_event_probability(n)
    k=int(sqrt(n))
    bd=1/k+(k-1)/(2*(n-k)) if k<n else 1
    assert a <= bd+1e-10
    print(f'n={n}: P(founder ever returns upward)={a:.10f}; bound={bd:.10f}')
