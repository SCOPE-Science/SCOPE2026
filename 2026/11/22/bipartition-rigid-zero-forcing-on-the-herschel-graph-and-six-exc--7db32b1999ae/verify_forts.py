"""Independent set/fort-transversal and all-pairs Floyd--Warshall verification.
Constructs the Herschel graph from its alternative 1-based adjacency description.
Python 3 standard library only: python verify_forts.py
"""
import json
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path

ADJ={1:(2,4,5),2:(1,3,6,7),3:(2,4,8),4:(1,3,9,10),
     5:(1,6,10),6:(2,5,11),7:(2,8,11),8:(3,7,9),
     9:(4,8,11),10:(4,5,11),11:(6,7,9,10)}
U=set(ADJ)
assert len(U)==11 and all(v in ADJ[w] for v,vs in ADJ.items() for w in vs)
assert sum(len(x) for x in ADJ.values())==36

def is_fort(s):
    return all(len(set(ADJ[x])&s)!=1 for x in U-s)
forts=[set(comb) for n in range(1,12) for comb in combinations(sorted(U),n)
       if is_fort(set(comb))]
# Only inclusion-minimal forts are needed, but retain all for a second cross-check.
minimal=[f for f in forts if not any(other < f for other in forts)]
assert all(is_fort(s) for s in minimal)

def hits_all_forts(s):return all(bool(s&f) for f in minimal)
minimal_size=None;solutions=[]
for k in range(12):
    S=[frozenset(c) for c in combinations(sorted(U),k)
       if hits_all_forts(set(c))]
    if S:minimal_size=k;solutions=S;break
assert minimal_size==5 and len(solutions)==114
P={1,3,6,7,9,10};Q=U-P
assert len(P)==6 and len(Q)==5
assert all(len(s&P)==3 and len(s&Q)==2 for s in solutions)

def mask(s):return sum(1<<(x-1) for x in s)
M=sorted(mask(s) for s in solutions)
E=sorted((mask(a),mask(b)) for a,b in combinations(sorted(solutions,key=mask),2)
         if len(a & b)==4)
assert len(E)==540
assert not any(any(tuple(sorted(set(a)^set(b)))==tuple(sorted((u,v)))
                   for u in U for v in ADJ[u]) for a,b in combinations(solutions,2) if len(a&b)==4)

# Floyd--Warshall on the FULL 114-state exchange graph.
index={m:i for i,m in enumerate(M)};n=len(M)
d=[[0 if i==j else 1000 for j in range(n)] for i in range(n)]
for a,b in E:
    i,j=index[a],index[b];d[i][j]=d[j][i]=1
for k in range(n):
    for i in range(n):
        dik=d[i][k]
        if dik==1000:continue
        for j in range(n):
            new=dik+d[k][j]
            if new<d[i][j]:d[i][j]=new
hist=Counter();excess=Counter();rare=[]
for i,a in enumerate(M):
    assert max(d[i])==5
    for j in range(i+1,n):
        b=M[j];diam=d[i][j];lb=(a^b).bit_count()//2
        hist[diam]+=1;excess[diam-lb]+=1
        if diam-lb==2:rare.append([a,b])
assert hist=={1:540,2:1938,3:2664,4:1167,5:132}
assert excess=={0:6183,1:252,2:6}

# Enumerate automorphisms using degree-class-preserving permutations.
deg3=sorted(v for v in U if len(ADJ[v])==3)
deg4=sorted(v for v in U if len(ADJ[v])==4)
edge_set={frozenset((v,w)) for v in U for w in ADJ[v]}
rare_pairs={tuple(pair) for pair in rare}
orbit=set();automorphisms=0
for triple in permutations(deg4):
    partial=dict(zip(deg4,triple))
    for octuple in permutations(deg3):
        f={**partial,**dict(zip(deg3,octuple))}
        if all(frozenset((f[v],f[w])) in edge_set for v,w in (tuple(e) for e in edge_set)):
            automorphisms+=1
            a,b=rare[0]
            def phi(m):return sum(1<<(f[i+1]-1) for i in range(11) if m>>i&1)
            orbit.add(tuple(sorted((phi(a),phi(b)))))
assert automorphisms==12 and orbit==rare_pairs

c=json.loads(Path(__file__).with_name('certificate.json').read_text())
assert c['minimum_masks']==M
assert c['jump_edges']==[list(x) for x in E]
assert {tuple(x) for x in c['max_excess_pairs']}==rare_pairs
assert c['johnson_excess_hist']=={'0':6183,'1':252,'2':6}
print('FORTS_PASS z=5 minima=114 slide=0 jumps=540 allpairs=6441 maxexcess_orbit=6 automorphisms=12')
print('forts',len(forts),'minimal_forts',len(minimal))
