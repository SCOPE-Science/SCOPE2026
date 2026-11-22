#!/usr/bin/env python3
"""Independent calculation using generalized Petersen GP(10,3) and Floyd-Warshall.
Standard library only; run: python3 verify_petersen_cover.py
"""
from itertools import combinations
from collections import Counter

n=20
nbr=[0]*n
# outer vertices 0..9; inner vertices 10..19
for i in range(10):
    j=(i+1)%10; nbr[i] |= 1<<j; nbr[j] |= 1<<i
    j=10+i; nbr[i] |= 1<<j; nbr[j] |= 1<<i
    j=10+((i+3)%10); a=10+i; nbr[a] |= 1<<j; nbr[j] |= 1<<a
assert all(x.bit_count()==3 for x in nbr)
FULL=(1<<20)-1

def succeeds(z):
    observed=z
    for i in range(20):
        if (z>>i)&1: observed |= nbr[i]
    while observed!=FULL:
        growth=0
        for i in range(20):
            if (observed>>i)&1:
                outside=nbr[i] & ~observed
                if outside and (outside & (outside-1))==0: growth|=outside
        if not growth: return False
        observed |= growth
    return True

for k in (1,2):
    assert not any(succeeds(sum(1<<i for i in s)) for s in combinations(range(20),k))
sets=[sum(1<<i for i in s) for s in combinations(range(20),3)
      if succeeds(sum(1<<i for i in s))]
assert len(sets)==240
inds={m:i for i,m in enumerate(sets)}
# Compute original graph metric with independent unweighted Floyd–Warshall.
gdist=[[0 if i==j else (1 if (nbr[i]>>j)&1 else 1000)
        for j in range(20)] for i in range(20)]
for k in range(20):
    for i in range(20):
        for j in range(20):
            if gdist[i][j]>gdist[i][k]+gdist[k][j]:gdist[i][j]=gdist[i][k]+gdist[k][j]

sig=[]
for m in sets:
    t=[i for i in range(20) if (m>>i)&1]
    sig.append(tuple(sorted(gdist[i][j] for i,j in combinations(t,2))))
assert Counter(sig)=={(2,3,5):120,(3,3,4):120}
INF=1000
J=[[0 if i==j else INF for j in range(240)] for i in range(240)]
T=[[0 if i==j else INF for j in range(240)] for i in range(240)]
for i,s in enumerate(sets):
    for o in range(20):
        if not s>>o&1:continue
        for w in range(20):
            if s>>w&1:continue
            k=inds.get(s^(1<<o)^(1<<w))
            if k is None:continue
            J[i][k]=1
            if nbr[o]>>w&1:T[i][k]=1
assert Counter((sig[i],sum(x==1 for x in J[i])) for i in range(240))=={
    ((2,3,5),17):120,((3,3,4),13):120}
assert Counter(sum(x==1 for x in row) for row in T)=={4:240}

def fw(M):
    # alternate APSP algorithm to check each full pair metric
    for k in range(240):
        rk=M[k]
        for i in range(240):
            d=M[i][k]
            if d>=INF:continue
            ri=M[i]
            for j in range(240):
                nd=d+rk[j]
                if nd<ri[j]:ri[j]=nd
    assert all(max(row)<INF for row in M)
    return Counter(M[i][j] for i in range(240) for j in range(i+1,240))

cj=fw(J);ct=fw(T)
assert cj=={1:1800,2:8160,3:18480,4:240},cj
assert ct=={1:480,2:1440,3:3540,4:6780,5:9000,6:6000,7:1380,8:60},ct
assert Counter((sig[i],max(T[i])) for i in range(240))=={
    ((2,3,5),7):120, ((3,3,4),8):120}
assert sum(1 for i in range(240) if 8 in T[i])==120
assert all(sum(1 for d in T[i] if d==8)==1 for i in range(240) if sig[i]==(3,3,4))
assert all(sum(1 for d in T[i] if d==8)==0 for i in range(240) if sig[i]==(2,3,5))
assert all((sets[i]&sets[j])==0 for i in range(240) for j in range(i+1,240) if T[i][j]==8)
print('representation: generalized Petersen GP(10,3)')
print('optima:',len(sets),'signatures:',dict(Counter(sig)))
print('unrestricted histogram:',dict(sorted(cj.items())))
print('sliding histogram:',dict(sorted(ct.items())))
print('sharp 60-pair antipodal matching confirmed')
print('PASS')
