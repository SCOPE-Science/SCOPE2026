"""Independent tuple/signature and adjacency-intersection verification of mu(C5).
Python 3, no nonstandard dependencies. Run: python verification_b.py
"""
from itertools import combinations
from collections import Counter

V=tuple(('v',i) for i in range(5))+tuple(('u',i) for i in range(5))+(('w',0),)
# Construct by a separate graph-construction rule from the standard Mycielskian definition.
base={i:{(i-1)%5,(i+1)%5} for i in range(5)}
NBR={v:set() for v in V}
for i in range(5):
    for j in base[i]:
        NBR[('v',i)].add(('v',j))
        NBR[('v',i)].add(('u',j))
        NBR[('u',j)].add(('v',i))
    NBR[('u',i)].add(('w',0))
    NBR[('w',0)].add(('u',i))
assert sum(map(len,NBR.values()))//2==20

def total_located(S):
    outside=tuple(v for v in V if v not in S)
    return (all(NBR[x]&S for x in V)
            and len({frozenset(NBR[x]&S) for x in outside})==len(outside))

def identified(S):
    signatures=[frozenset((NBR[x]|{x})&S) for x in V]
    return all(signatures) and len(set(signatures))==11

def enumerator(p):
    for k in range(12):
        ans={frozenset(c) for c in combinations(V,k) if p(set(c))}
        if ans:return k,ans
    raise AssertionError
kt,T=enumerator(total_located)
ki,I=enumerator(identified)
assert kt==ki==5 and (len(T),len(I))==(110,191) and T<I

def config_graph(codes, slide):
    G={s:set() for s in codes}
    for a,b in combinations(codes,2):
        if len(a&b)!=4:continue
        if slide:
            v=next(iter(a-b));w=next(iter(b-a))
            if w not in NBR[v]:continue
        G[a].add(b);G[b].add(a)
    return G

def bfs(G,s):
    D={s:0};q=[s]
    for a in q:
        for b in G[a]:
            if b not in D:
                D[b]=D[a]+1;q.append(b)
    assert len(D)==len(G)
    return D

for slide in (False,True):
    H=config_graph(T,slide);K=config_graph(I,slide)
    assert (sum(map(len,H.values()))//2,sum(map(len,K.values()))//2)==((190,555) if slide else (520,1405))
    dsH={s:bfs(H,s) for s in T}
    dsK={s:bfs(K,s) for s in T}
    C=Counter(dsH[s][t]-dsK[s][t] for s,t in combinations(T,2))
    target=({0:4135,1:1440,2:360,3:60} if slide else {0:5725,1:270})
    assert C==target,(slide,C)
    assert max(max(x.values()) for x in dsH.values())==(8 if slide else 5)
    print('slide' if slide else 'jump','difference counts',dict(sorted(C.items())))
print('PASS independent tuple certificate')

# Independently check dihedral orbit decomposition and an extremal pair.
def transform(s, shift, sign):
    def phi(x):
        if x[0] in ('v','u'):
            return (x[0], (shift+sign*x[1])%5)
        return x
    return frozenset(phi(x) for x in s)
def orbit_partition(fam):
    unseen=set(fam);sizes=[]
    while unseen:
        seed=next(iter(unseen))
        orb={transform(seed,k,e) for k in range(5) for e in (-1,1)}
        assert orb<=fam
        unseen.difference_update(orb)
        sizes.append(len(orb))
    return sorted(sizes)
# Derive actual orbit sizes without hard-coded representatives.
assert Counter(orbit_partition(T))==Counter({10:9,5:4})
assert Counter(orbit_partition(I))==Counter({10:15,5:8,1:1})

def fs(spec):
    return frozenset((x[0],int(x[1:])) for x in spec.split() if x[0]!='w') | (frozenset({('w',0)}) if 'w' in spec.split() else frozenset())
start=fs('v0 v1 v2 u0 u3');end=fs('v1 v2 v3 u0 u3')
Lpath=[fs(x) for x in ['v0 v1 v2 u0 u3','v0 v1 v2 v4 u3','v0 v1 v2 v3 u3','v1 v2 v3 u3 u4','v1 v2 v3 u3 w','v1 v2 v3 u0 u3']]
Ipath=[start,fs('v1 v2 u0 u3 u4'),end]
Ht=config_graph(T,True);Hi=config_graph(I,True)
assert all(x in T for x in Lpath) and all(y in Ht[x] for x,y in zip(Lpath,Lpath[1:]))
assert all(x in I for x in Ipath) and all(y in Hi[x] for x,y in zip(Ipath,Ipath[1:]))
assert Ipath[1] not in T
assert bfs(Ht,start)[end]==5 and bfs(Hi,start)[end]==2
print('PASS witness: five legal locating-total slides versus two identifying-code slides')
