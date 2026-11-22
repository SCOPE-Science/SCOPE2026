"""Independent structural verifier for the minimum one-erasure power dominating sets on Q4.
Run: python3 verify_structural.py. Uses no external packages.
"""
from itertools import combinations, permutations
from collections import Counter, deque

V=tuple(range(16))
D=lambda u,v:(u^v).bit_count()
# Auxiliary graph edges connect original cube words at Hamming distance exactly three.
E={(u,v) for u in V for v in V if u<v and D(u,v)==3}
assert len(E)==32

def t(x):
    return x^(15 if x.bit_count()%2 else 0)
assert all(t(t(x))==x for x in V)
assert all(D(u,v)==3 if D(t(u),t(v))==1 else D(u,v)!=3 for u,v in combinations(V,2))

def sorttype(X):
    edges=[(u,v) for u,v in combinations(X,2) if (u,v) in E]
    if len(edges)==4:return 'C4'
    if len(edges)==3:
        deg=Counter(v for edge in edges for v in edge)
        return 'P4' if sorted(deg.values())==[1,1,2,2] else None
    if len(edges)!=2 or len({a for e in edges for a in e})!=4:return None
    a,b=edges
    da=t(a[0])^t(a[1]); db=t(b[0])^t(b[1])
    assert da.bit_count()==db.bit_count()==1
    if da!=db:return '2K2 skew'
    sep=(t(a[0])^t(b[0])) & ~da
    assert sep.bit_count() in (2,3)
    return '2K2 parallel sep '+str(sep.bit_count())

S=[]; counts=Counter()
for X in combinations(V,4):
    typ=sorttype(X)
    if typ is not None:
      S.append(frozenset(X));counts[typ]+=1
assert counts==Counter({'P4':192,'2K2 skew':96,'2K2 parallel sep 2':48,'C4':24,'2K2 parallel sep 3':16})
assert len(S)==376
# Recover all five action orbits of the *ordinary* cube automorphism group.
Sset=set(S)
perms=list(permutations(range(4)))
def perm_vertex(v,p,b):
    r=b
    for i in range(4):
        if v>>i&1:r^=1<<p[i]
    return r
unchecked=Sset.copy();orbit_counts=Counter()
while unchecked:
    X=next(iter(unchecked))
    images={frozenset(perm_vertex(v,p,b) for v in X) for p in perms for b in V}
    assert images<=Sset
    assert all(sorttype(tuple(sorted(Y)))==sorttype(tuple(sorted(X))) for Y in images)
    orbit_counts[(sorttype(tuple(sorted(X))),len(images))]+=1
    unchecked.difference_update(images)
assert orbit_counts==Counter({('P4',192):1,('2K2 skew',96):1,('2K2 parallel sep 2',48):1,('C4',24):1,('2K2 parallel sep 3',16):1})

M={X:i for i,X in enumerate(S)}
adj=[[] for _ in S]
sliding=0
for i,X in enumerate(S):
    for u in X:
      for v in V:
        if v not in X:
          Y=(X-{u})|{v}
          j=M.get(Y)
          if j is not None:
            adj[i].append(j)
            sliding+=D(u,v)==1
assert sliding==0
assert sum(len(e) for e in adj)//2==2496
assert Counter(map(len,adj))==Counter({14:192,12:160,16:24})
ecc=Counter();hist=Counter()
for src in range(len(S)):
    distance={src:0};q=deque([src])
    while q:
      i=q.popleft()
      for j in adj[i]:
        if j not in distance:
          distance[j]=distance[i]+1;q.append(j)
    assert len(distance)==376
    e=max(distance.values());ecc[(sorttype(tuple(sorted(S[src]))),e)]+=1
    for j,d in distance.items():
      if src<j:hist[d]+=1
assert sum(n for (typ,e),n in ecc.items() if e==6)==48
assert hist==Counter({1:2496,2:13536,3:29520,4:22992,5:1932,6:24})
print('STRUCTURAL_VERIFIED 376, five orbits, all connected by jumps of diameter 6, zero legal slides')
