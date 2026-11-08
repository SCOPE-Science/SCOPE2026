#!/usr/bin/env python3
"""Exact-rational finite truncation checks for geometric duplication alignment."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import prod

def runs(s):
    out=[]
    for x in s:
        if out and out[-1][0] == x:
            out[-1]=(x,out[-1][1]+1)
        else:
            out.append((x,1))
    return out

def decoded(s,k):
    return tuple(x for x,c in zip(s,k) for _ in range(c))

def check_truncated(s,p,B):
    m=len(s); z=1-p
    prob=defaultdict(F)
    multiplicity=defaultdict(int)
    # Probability of each possible duration vector, with no renormalization:
    # only duration vectors with all components at most B are considered.
    maxp=defaultdict(F)
    for k in product(range(1,B+1),repeat=m):
        y=decoded(s,k)
        v=p**m * z**(sum(k)-m)
        prob[y]+=v
        multiplicity[y]+=1
        maxp[y]=max(maxp[y],v)
    actual=sum(maxp.values(),F(0))
    lengths=[r for _,r in runs(s)]
    pred=prod((p**(r-1))*(1-z**(r*(B-1)+1)) for r in lengths)
    assert actual == pred,(s,p,B,actual,pred)
    # Exact posterior composition count from noiseless observation.
    from math import comb
    for y in prob:
        out_runs=runs(y)
        N=prod(comb(t-1,r-1) for (_,r),(_,t) in zip(runs(s),out_runs))
        assert len(out_runs)==len(lengths)
        assert N >= multiplicity[y],(s,y,N,multiplicity[y])
        assert prob[y] == maxp[y]*multiplicity[y], (s,y,prob[y],maxp[y],N)
    return len(prob)

def matrix_product(pi,Q,p,m):
    v=pi[:]
    for _ in range(m-1):
        v=[sum(v[i]*Q[i][j]*(p if i==j else 1) for i in range(len(pi))) for j in range(len(pi))]
    return sum(v)

def check_markov(pi,Q,p,m):
    n=len(pi)
    bywords=F(0)
    for s in product(range(n),repeat=m):
        w=pi[s[0]]
        for a,b in zip(s,s[1:]):
            w*=Q[a][b]
        bywords+=w*p**(m-len(runs(s)))
    mat=matrix_product(pi,Q,p,m)
    assert bywords==mat,(m,p,bywords,mat)

checks=0
outputs=0
for alphabet in (2,3):
    for m in range(1,6 if alphabet==2 else 5):
        for s in product(range(alphabet),repeat=m):
            for p in (F(1,2),F(2,3)):
                for B in (2,3):
                    outputs+=check_truncated(s,p,B)
                    checks+=1
pi=[F(2,3),F(1,3)]
Q=[[F(3,4),F(1,4)],[F(1,2),F(1,2)]]
for m in range(1,8):
    for p in (F(1,2),F(2,3),F(1)):
        check_markov(pi,Q,p,m)
        checks+=1
print('PASS:',checks,'exact-rational experiments;',outputs,'noiseless output-group checks')
print('Proof covers all lengths and fields of observation; bounded enumeration is not its proof.')

# Independent checks of the log-curvature classification at fixed run totals.
from itertools import combinations_with_replacement
from math import factorial

def compositions(total,parts):
    if parts==1:
        yield (total,)
    else:
        for first in range(1,total-parts+2):
            for rest in compositions(total-first,parts-1):
                yield (first,)+rest

# Positive log-convex law, a normalized mixture of two different geometries.
def convex_a(k):
    return F(1,2)*(F(1,2)**k) + F(1,2)*(F(1,3)*F(2,3)**(k-1))

# Positive, strictly log-concave factorial-tail weights (normalization cancels
# from comparisons at fixed run length).
def concave_weight(k):
    return F(1,factorial(k))

curvature_checks=0
for r in range(1,6):
    for L in range(r,r+19):
        tuples=list(compositions(L,r))
        assert max(prod(convex_a(k) for k in ks) for ks in tuples) == convex_a(L-r+1)*convex_a(1)**(r-1)
        u,v=divmod(L,r)
        assert max(prod(concave_weight(k) for k in ks) for ks in tuples)==concave_weight(u)**(r-v)*concave_weight(u+1)**v
        curvature_checks+=1
# Verify nontrivial exact strict separation at the first discriminating total.
assert concave_weight(2)**2>concave_weight(1)*concave_weight(3)
print('PASS:',curvature_checks,'additional exact-rational log-curvature mode checks')
