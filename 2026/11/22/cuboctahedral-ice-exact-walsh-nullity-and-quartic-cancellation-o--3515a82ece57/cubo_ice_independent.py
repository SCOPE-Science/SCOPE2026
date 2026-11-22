#!/usr/bin/env python3
"""Independent exact Fourier certificate for Eulerian orientations of the cuboctahedral graph.
Build the incidence parity solution independently of orientation recursion.
"""
from itertools import combinations
from collections import Counter,deque
from math import comb,gcd

Q=[(i,j) for i in range(8) for j in range(i+1,8) if (i^j).bit_count()==1]
assert len(Q)==12
E=[(i,j) for i in range(12) for j in range(i+1,12) if set(Q[i])&set(Q[j])]
assert len(E)==24
adj=[[] for _ in range(12)]
for k,(a,b) in enumerate(E):
    adj[a].append((b,k));adj[b].append((a,k))
parent=[-1]*12;pe=[-1]*12;order=[0];parent[0]=0
for v in order:
    for u,k in adj[v]:
        if parent[u]<0:
            parent[u]=v;pe[u]=k;order.append(u)
assert len(order)==12
chords=[k for k in range(24) if k not in pe]
assert len(chords)==13
rhs0=[sum(1 for a,b in E if b==v)&1 for v in range(12)]
solutions=[];bitmap=[0]*(1<<13)
for free in range(1<<13):
    rhs=rhs0.copy();whole=0
    for j,k in enumerate(chords):
        bit=(free>>j)&1
        if bit:
            whole |= (1<<k)
            a,b=E[k];rhs[a]^=1;rhs[b]^=1
    for v in reversed(order[1:]):
        bit=rhs[v]
        if bit:
            whole |= (1<<pe[v]);rhs[parent[v]]^=1
    assert rhs[0]==0
    out=[0]*12
    for k,(a,b) in enumerate(E):
        if (whole>>k)&1:out[a]+=1
        else:out[b]+=1
    if all(d==2 for d in out):
        solutions.append(whole);bitmap[free]=1
assert len(solutions)==600

def fwht(v):
    n=len(v);h=1
    while h<n:
        for i in range(0,n,h*2):
            for j in range(i,i+h):
                a,b=v[j],v[j+h];v[j]=a+b;v[j+h]=a-b
        h*=2

fwht(bitmap)
hist=Counter(bitmap);zero=hist[0]
assert zero==4639,(zero,hist)
assert len(bitmap)-zero==3553
assert min(abs(a) for a in bitmap if a)==4
assert sum(a*a for a in bitmap)==(1<<13)*600
allfreq=bitmap.copy()
proj=[int(a!=0) for a in bitmap]
fwht(proj)
sumabs=sum(abs(x) for x in proj)
g=gcd(sumabs,len(proj));assert (sumabs//g,len(proj)//g)==(29471,2048)
weight2zero=weight4zero=0
for weight in (2,4):
    count=0
    for idx in combinations(range(24),weight):
        S=sum(1<<i for i in idx)
        v=sum(1 if ((x&S).bit_count()&1)==0 else -1 for x in solutions)
        if v==0: count+=1
    if weight==2: weight2zero=count
    else: weight4zero=count
assert weight2zero==0
assert weight4zero==864
assert sum(hist.values())==8192
print('INDEPENDENT_PASS')
print('vertices=12 edges=24 independent_coordinates=13')
print('orientations=600 quotient_zeros=4639 quotient_rank=3553')
print('full_zeros=9500672 full_rank=7276544 min_nonzero=4')
print('weight2_zeros=0 weight4_zeros=864')
print('projection_norm=29471/2048')
print('quotient_spectral_histogram:',sorted(hist.items()))
