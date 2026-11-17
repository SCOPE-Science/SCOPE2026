#!/usr/bin/env python3
"""Exhaustive finite quotient and all-size weighted coefficient certificates."""
from itertools import combinations_with_replacement
from collections import defaultdict
from math import factorial

T=list(combinations_with_replacement(range(4),2))
index={v:i for i,v in enumerate(T)}
W=[3**i for i in range(10)]
N=3**10
ROT=[index[tuple(sorted(((a+1)%4,(b+1)%4)))] for a,b in T]
ZERO=[index[tuple(sorted(((a+1)%4 if a else 0,(b+1)%4 if b else 0)))] for a,b in T]
DEFECT=ROT.copy(); DEFECT[index[(0,1)]]=index[(0,2)]

def digits(k):return tuple((k//w)%3 for w in W)
def encode(c):return sum(v*w for v,w in zip(c,W))

def transfer(k):
    c=digits(k)
    excited=sum(c[i]*(2 if a==b else 1) for i,(a,b) in enumerate(T) if a==1 or b==1)
    if excited==0: trans=ZERO
    elif excited==1 and c[index[(0,1)]]==1: trans=DEFECT
    else:trans=ROT
    out=[0]*10
    for i,count in enumerate(c):
        out[trans[i]]=min(2,out[trans[i]]+count)
    return encode(out)

def all_rest(k):
    c=digits(k)
    return sum(c[1:])==0

def rotating(k):
    c=digits(k)
    counts=[min(2,sum(v*((a==color)+(b==color)) for (a,b),v in zip(T,c))) for color in range(4)]
    if 0 in counts:return False
    return all(counts[color]>1 or c[index[tuple(sorted((color,(color-1)%4)))]]==0 for color in range(4))

F=[transfer(k) for k in range(N)]
TAU=[-1]*N;PER=[0]*N
for k in range(N):
    s=k
    for t in range(7):
        if all_rest(s):TAU[k]=t;PER[k]=1;break
        if rotating(s):TAU[k]=t;PER[k]=4;break
        s=F[s]
    assert TAU[k]>=0,(k,digits(k))
    assert TAU[k]<=6
    if PER[k]==4:assert rotating(s)
    if PER[k]==1:assert all_rest(s)
assert max(TAU)==6
assert all(TAU[k]<=5 for k in range(N) if sum(digits(k))<=2)

# For a labelled graph with m matched pairs: labelled initial states are obtained
# by assigning m pair types, with 2 orientations for a mixed pair type.
# The signature weight of multiplicities a_j is m! prod w_j^a_j/a_j!.
def all_compositions(total,parts):
    if parts==1:yield (total,);return
    for k in range(total+1):
        for r in all_compositions(total-k,parts-1):yield(k,)+r

def census(m):
    out=defaultdict(int)
    for a in all_compositions(m,10):
        sig=encode([min(2,v) for v in a]);weight=factorial(m)
        for x,(lo,hi) in zip(a,T):
            weight//=1 # keep integer-valued product until final denominator
        numerator=factorial(m);denominator=1
        for x,(lo,hi) in zip(a,T):
            numerator*= (2 if lo!=hi else 1)**x
            denominator*=factorial(x)
        weight=numerator//denominator
        assert weight*denominator==numerator
        out[(TAU[sig],PER[sig])]+=weight
    assert sum(out.values())==16**m
    return out

print('finite quotient signatures',N)
print('all 59049 signatures enter all-rest or full-rotation by 6: yes')
print('maximal quotient entry time',max(TAU))
for m in range(2,7):
    tab=census(m)
    pp=sum(v for (t,p),v in tab.items() if t==0 and p==4)
    most=max(t for t,p in tab)
    largest=sum(v for (t,p),v in tab.items() if t==most)
    print('m',m,'states',16**m,'period4_states',pp,'period4_orbits',pp//4,
          'max_tau',most,'last_layer',largest,'extinction_basin',sum(v for (t,p),v in tab.items() if p==1),
          'period4_basin',sum(v for (t,p),v in tab.items() if p==4))
    if m==2: assert (most,largest,pp)==(5,16,8)
    if m==3: assert (most,largest,pp)==(6,60,552)
    if m==4: assert (most,largest,pp)==(6,448,23096)
    if m==5: assert (most,largest,pp)==(6,2460,586760)
    if m==6: assert (most,largest,pp)==(6,12144,12001368)

for x in [1,2]:
    c=[0]*10;c[index[(0,0)]]=x;c[index[(0,3)]]=1;c[index[(1,2)]]=1
    assert TAU[encode(c)]==6
print('all checks passed')
