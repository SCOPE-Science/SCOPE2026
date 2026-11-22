#!/usr/bin/env python3
"""Exact integer/polynomial certificate for a constrained one-deletion graph.
Python 3 standard library only. Run from the directory containing artifacts.
"""
import json
from pathlib import Path

C = json.loads((Path(__file__).parent / 'transfer_certificate.json').read_text(encoding='utf8'))

# A nondeterministic synchronous pair reader for a shared one-deletion output:
# P pre-deletions, Q post-deletions, Xb/Yb lag with retained bit b.
# Integer NFA states: P=0,Q=1,X0=2,X1=3,Y0=4,Y1=5.
def advance(S, a, b):
    T = set()
    if 0 in S:
        if a == b: T.add(0)
        T.update((1, 2+b, 4+a))
    if 1 in S and a == b:
        T.add(1)
    if 2+a in S:
        T.update((1, 2+b))
    if 4+b in S:
        T.update((1, 4+a))
    return frozenset(T)

initial=(frozenset((0,)),-1,-1)
raw=[initial]; loc={initial:0}; adj=[]
for S,p,q in raw:
    children=[]
    for a,b in ((0,0),(0,1),(1,0),(1,1)):
        if p==a==1 or q==b==1: continue
        nxt=(advance(S,a,b),a,b)
        if nxt not in loc:
            loc[nxt]=len(raw); raw.append(nxt)
        children.append(loc[nxt])
    adj.append(children)
assert len(raw)==17
accept=[int(1 in S) for S,_,_ in raw]
# Coarsest stable partition by accepting status and counted transitions.
colors=accept[:]
while True:
    groups=sorted(set(colors))
    signatures=[(colors[i],tuple(sum(colors[j]==g for j in adj[i]) for g in groups)) for i in range(len(raw))]
    coding={s:k for k,s in enumerate(sorted(set(signatures)))}
    nxt=[coding[s] for s in signatures]
    if len(set(nxt))==len(set(colors)):break
    colors=nxt
assert len(set(colors))==12
# Quotient from the initial state, then remove states with no accepting future.
representatives={g:colors.index(g) for g in set(colors)}
qtrans={g:{} for g in representatives}
for g,i in representatives.items():
    for j in adj[i]:
        h=colors[j]; qtrans[g][h]=qtrans[g].get(h,0)+1
    # Each constituent of an equitable class has the same transitions by count.
    for i2 in [k for k in range(len(raw)) if colors[k]==g]:
        assert accept[i2]==accept[i]
        assert all(sum(colors[j]==h for j in adj[i2])==qtrans[g].get(h,0) for h in representatives)
active={g for g,i in representatives.items() if accept[i]}
while True:
    nxt=active|{g for g,outs in qtrans.items() if any(h in active for h in outs)}
    if nxt==active:break
    active=nxt
assert len(active)==9
queue=[colors[0]];order=[]
for g in queue:
    if g not in order:order.append(g)
    for h in qtrans[g]:
        if h in active and h not in queue:queue.append(h)
assert len(order)==9
observed=[[qtrans[g].get(h,0) for h in order] for g in order]
assert observed==C['transition_matrix'], (observed,C['transition_matrix'])
assert [accept[representatives[g]] for g in order]==C['accepting']

# Check an *infinite-length identity* by a finite exact polynomial certificate.
# If (I-z M) P(z) = D(z) b and D(0)=1, then the unique formal
# power series continuation counts are P(z)/D(z).
def add(A,B):
    O=[0]*max(len(A),len(B))
    for i,a in enumerate(A):O[i]+=a
    for i,b in enumerate(B):O[i]+=b
    while len(O)>1 and O[-1]==0:O.pop()
    return O

def neg(A):return [-a for a in A]
def shift(A,k=1):return [0]*k + A

def mul(A,B):
    O=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):O[i+j]+=a*b
    return O

D=C['denominator_asc']; P=C['state_numerators_asc']; b=C['accepting'];M=observed
assert D[0]==1
for i in range(9):
    lhs=P[i][:]
    for j,m in enumerate(M[i]):
        if m:lhs=add(lhs,neg(shift([m*x for x in P[j]])))
    rhs=[x*b[i] for x in D]
    assert add(lhs,neg(rhs))==[0],(i,lhs,rhs)
# D(z)=(1-z)(1-z-z^2)^3 and P_A is the accepted ordered-pair GF numerator.
A=[1,-1,-1]
assert D==mul([1,-1],mul(A,mul(A,A)))
# Hamming-only edges are counted by z/(1-z-z^2)^2.
# E(z)= (T(z)-F(z)+1)/2 with F(z)=(1+z)/(1-z-z^2).
# Assert T(z) = 2E(z)+(F(z)-1) via polynomial clearing.
E_num=[0,1,-1,0,1] # z*(1-z+z^3)
# E = E_num / D; F-1 = (2z+z^2)/A.
lhs=P[0]
rhs=add([2*x for x in E_num],mul([0,2,1],mul([1,-1],mul(A,A))))
assert add(lhs,neg(rhs))==[0],(lhs,rhs)
# Verify split E=z/A^2 + z^2/((1-z)A^3).
assert add(mul([0,1],mul([1,-1],A)),[0,0,1])==E_num
print('TRANSFER_CERTIFICATE_OK states=17 quotient=12 productive=9')
