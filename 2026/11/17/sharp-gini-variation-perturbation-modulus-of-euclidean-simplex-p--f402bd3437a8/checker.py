#!/usr/bin/env python3
"""Independent rational diagnostics for complete-graph Gini variation of simplex projection."""
from fractions import Fraction as F
from itertools import product
from math import isqrt

def tv(v):
    return sum(abs(v[i]-v[j]) for i in range(len(v)) for j in range(i+1,len(v)))

def jac(n,mask,h):
    active=[i for i in range(n) if mask>>i&1]
    k=len(active)
    av=sum((h[i] for i in active),F(0))/k
    return [h[i]-av if i in active else F(0) for i in range(n)]

def bound(n):
    return max(F((k-1)*(2*n-k),k*(n-1)) for k in range(2,n+1))

def project(x):
    n=len(x)
    y=sorted(x,reverse=True)
    active=0
    tau=F(0)
    for k in range(1,n+1):
        candidate=(sum(y[:k],F(0))-1)/k
        if y[k-1]>candidate:
            active=k; tau=candidate
    assert active>=1
    out=[max(F(0),v-tau) for v in x]
    assert sum(out)==1
    return out

count=0
for n in range(2,10):
    computed=F(0)
    for mask in range(1,1<<n):
        for cut in range(1,(1<<n)-1):
            x=[F((cut>>i)&1) for i in range(n)]
            ratio=tv(jac(n,mask,x))/tv(x)
            computed=max(computed,ratio)
            count+=1
    assert computed==bound(n),(n,computed,bound(n))
    print('ALL_ACTIVE_SETS_AND_ALL_NONTRIVIAL_CUTS',n,'PASS',computed)
print('EXACT_ACTIVE_SUPPORT_CUT_COMPARISONS_PASSED',count)

witnesses=0
for n in range(2,90):
    k=max(range(2,n+1),key=lambda s:F((s-1)*(2*n-s),s*(n-1)))
    x=[F(1,k) if i<k else F(-1) for i in range(n)]
    step=F(1,7*k)
    y=x.copy(); y[0]+=step
    a=project(x); b=project(y)
    assert sum(a)==sum(b)==1
    assert sum(v>0 for v in a)==k==sum(v>0 for v in b)
    assert tv([s-t for s,t in zip(b,a)])/tv([s-t for s,t in zip(y,x)])==bound(n)
    witnesses+=1
print('EXACT_ATTAINED_SIMPLEX_PAIRS_PASSED',witnesses)

pairs=0
for n in range(2,9):
    pool=[F(-2),F(-1,2),F(0),F(1,3),F(1),F(2)]
    inputs=[[pool[(i*i+3*i+j*(i+2)+j*j)%len(pool)] for i in range(n)] for j in range(70)]
    for x in inputs:
      for y in inputs:
        diff=[a-b for a,b in zip(x,y)]
        if tv(diff)==0: continue
        output=[a-b for a,b in zip(project(x),project(y))]
        assert tv(output)<=bound(n)*tv(diff)
        pairs+=1
print('EXACT_TWO_INPUT_NONLINEAR_INEQUALITIES_PASSED',pairs)
print('ALL_COMPLETE_GRAPH_GINI_SIMPLEX_CHECKS_PASSED')
