#!/usr/bin/env python3
"""Independent exact interval-state verification for neutral Moran BD on P5.
All mutant sets reachable from one mutant are intervals. No external packages.
"""
from fractions import Fraction as F
n=5
degree=[1,2,2,2,1]
intervals=[(l,r) for l in range(n) for r in range(l,n) if (l,r)!=(0,n-1)]
where={x:i for i,x in enumerate(intervals)}
k=len(intervals)
A=[[F(int(i==j)) for j in range(k)] for i in range(k)]
W=sum((F(1,d) for d in degree),F())
h=[sum((F(1,degree[v]) for v in range(l,r+1)),F())/W for l,r in intervals]
for i,(l,r) in enumerate(intervals):
    transitions=[]
    if l>0:
        transitions.append(((l-1,r), F(1,n*degree[l])))
        transitions.append(((l+1,r), F(1,n*degree[l-1])))
    if r<n-1:
        transitions.append(((l,r+1), F(1,n*degree[r])))
        transitions.append(((l,r-1), F(1,n*degree[r+1])))
    for new,p in transitions:
        if new in where:
            A[i][where[new]]-=p
# In particular, self-loop mass is automatically retained in I-Q because
# no-event replacement probabilities are excluded from the transitions.
# Actual equation uses I-Q = (sum distinct event probabilities) I - offdiag.
# Since each transition is given only for a state change, subtract from the
# diagonal the no-change probability by replacing its initial 1 with total
# state-change probability.
for i,(l,r) in enumerate(intervals):
    ps=F(0)
    if l>0: ps+=F(1,n*degree[l])+F(1,n*degree[l-1])
    if r<n-1: ps+=F(1,n*degree[r])+F(1,n*degree[r+1])
    A[i][i]=ps

def solve(A,b):
    m=len(b); X=[a[:]+[b[i]] for i,a in enumerate(A)]
    for j in range(m):
        t=next(t for t in range(j,m) if X[t][j]!=0)
        X[t],X[j]=X[j],X[t]
        v=X[j][j]; X[j]=[z/v for z in X[j]]
        for i in range(m):
            if i==j:continue
            v=X[i][j]
            if v: X[i]=[x-v*y for x,y in zip(X[i],X[j])]
    return [row[-1] for row in X]

u=solve(A,h)
assert all(sum((A[i][j]*u[j] for j in range(k)),F())==h[i] for i in range(k))
mean=lambda v:u[where[v,v]]/h[where[v,v]]
assert h[where[1,1]]==h[where[2,2]]==F(1,7)
assert mean(1)==F(14650,329),mean(1)
assert mean(2)==F(26955,658),mean(2)
assert mean(1)-mean(2)==F(335,94)
print('interval states',k,'fixation probabilities',h[where[1,1]],h[where[2,2]])
print('conditional means',mean(1),mean(2),'difference',mean(1)-mean(2))
print('PASS')
