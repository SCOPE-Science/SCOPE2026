#!/usr/bin/env python3
"""Independent exhaustive proof checker, bitmask representation, Python 3 standard library."""
from collections import Counter, deque
from itertools import combinations
N=13; FULL=(1<<N)-1
R={pow(a,2,N) for a in range(1,N)}
assert R=={1,3,4,9,10,12}
OPEN=[sum(1<<v for v in range(N) if (v-u)%N in R) for u in range(N)]
CLOSED=[OPEN[u]|1<<u for u in range(N)]
assert all(m.bit_count()==6 for m in OPEN)

def locating(C):
    signatures=[OPEN[u]&C for u in range(N) if not (C>>u)&1]
    return 0 not in signatures and len(signatures)==len(set(signatures))

def identifying(C):
    sig=[CLOSED[u]&C for u in range(N)]
    return 0 not in sig and len(set(sig))==N

levels={}
for k in range(5):
    levels[k]=[sum(1<<v for v in c) for c in combinations(range(N),k) if locating(sum(1<<v for v in c))]
assert [len(levels[k]) for k in range(5)]==[0,0,0,0,247]
sets=sorted(levels[4]); IDS={C for C in sets if identifying(C)}
assert len(IDS)==26
idx={c:i for i,c in enumerate(sets)}

def network(slide):
    ad=[set() for _ in sets]
    for i,C in enumerate(sets):
        for u in range(N):
            if not (C>>u)&1:continue
            available=(OPEN[u] if slide else FULL)&~C
            for v in range(N):
                if (available>>v)&1:
                    D=(C ^ (1<<u))|(1<<v)
                    if D in idx:ad[i].add(idx[D])
    assert all(i in ad[j] for i,neighbors in enumerate(ad) for j in neighbors)
    return ad

def distances(ad):
    dist_hist=Counter();ecc=[]
    for start in range(len(sets)):
        d=[-1]*len(sets);d[start]=0;q=deque([start])
        while q:
            u=q.popleft()
            for v in ad[u]:
                if d[v]<0:d[v]=d[u]+1;q.append(v)
        assert min(d)>=0
        ecc.append(max(d))
        dist_hist.update(d[start+1:])
    return ecc,dict(sorted(dist_hist.items()))

A=network(False); B=network(True)
assert sum(map(len,A))//2==1599
assert sum(map(len,B))//2==858
EA,da=distances(A); EB,db=distances(B)
assert Counter(EA)=={4:247}
assert Counter(EB)=={5:221,6:26}
assert {sets[i] for i,e in enumerate(EB) if e==6}==IDS
# All distance-six pairs are the thirteen translates of one explicit pair.
farpairs=set()
for i,start in enumerate(sets):
    d=[-1]*len(sets);d[i]=0;q=deque([i])
    while q:
        u=q.popleft()
        for v in B[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    for j in range(i+1,len(sets)):
        if d[j]==6:farpairs.add(frozenset((start,sets[j])))
S=sum(1<<a for a in (0,1,3,9)); T=sum(1<<a for a in (0,4,10,12))
translate=lambda X,b:sum(1<<((a+b)%N) for a in range(N) if X>>a&1)
expected={frozenset((translate(S,b),translate(T,b))) for b in range(N)}
assert farpairs==expected and len(expected)==13
assert all((P&Q).bit_count()==1 for P,Q in (tuple(z) for z in farpairs))
assert Counter(map(len,B))=={3:26,6:117,8:39,9:26,10:39}
# Orbit calculation: the full automorphism group is affine maps x -> a*x+b for nonzero quadratic residues a.
AFF=[(a,b) for a in sorted(R) for b in range(N)]
rem=set(sets); orbit_list=[]
while rem:
    rep=min(rem)
    orbit={sum(1<<((a*v+b)%N) for v in range(N) if (rep>>v)&1) for a,b in AFF}
    assert orbit<=rem
    rem-=orbit
    i=idx[rep]
    orbit_list.append((len(orbit),len(B[i]),EB[i],bool(rep in IDS),tuple(v for v in range(N) if rep>>v&1)))
assert sorted(x[0] for x in orbit_list)==[26,26,39,39,39,78]
assert sum(int(x[3])*x[0] for x in orbit_list)==26
print('PASS bitmask; minima=247 identifying=26 jump_edges=1599 slide_edges=858')
print('jump_distance_hist',da)
print('slide_distance_hist',db)
print('affine_orbits',sorted(orbit_list))
