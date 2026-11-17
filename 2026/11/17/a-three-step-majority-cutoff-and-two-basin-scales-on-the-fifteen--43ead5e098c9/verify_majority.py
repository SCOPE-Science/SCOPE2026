"""Independent exact labelled graph/set iteration and orbit certificate."""
from itertools import combinations
from collections import Counter, defaultdict, deque

V = tuple(combinations(range(6),2))
assert len(V)==15
nb = tuple(tuple(j for j, v in enumerate(V) if set(u).isdisjoint(v)) for u in V)
assert all(len(a)==6 for a in nb)
N=2**len(V)

def rule(s):
    # Read a set of occupied edges, not a precomputed bit-neighbor mask.
    occupied={e for i,e in enumerate(V) if (s>>i)&1}
    new=set()
    for e in V:
        supporters=sum(V[j] in occupied for j in nb[V.index(e)])
        if supporters>3 or (supporters==3 and e in occupied): new.add(e)
    return sum(1<<i for i,e in enumerate(V) if e in new)

F=tuple(rule(s) for s in range(N))
entry=Counter()
basins=Counter()
period={}
for s in range(N):
    u=s
    for t in range(4):
        if F[F[u]]==u:break
        u=F[u]
    else:raise ValueError('not periodic within three updates')
    p=1 if F[u]==u else 2
    key=min(u,F[u])
    basins[key]+=1
    period[key]=p
    entry[(t,p)]+=1
    if F[F[F[F[F[s]]]]]!=F[F[F[s]]]:raise ValueError('iterate identity')
assert any(F[F[F[F[s]]]]!=F[F[s]] for s in range(N))
hist=Counter((period[k],v) for k,v in basins.items())

# Orbits under relabelling generators: the same 15-dimensional action,
# implemented by permuting named edges rather than bit positions directly.
def swap(s,i):
    moved=set()
    for j,e in enumerate(V):
        if not (s>>j)&1:continue
        moved.add(tuple(sorted((i+1 if x==i else i if x==i+1 else x for x in e))))
    return sum(1<<j for j,e in enumerate(V) if e in moved)

unseen=set(basins)
classes=[]
while unseen:
    seed=min(unseen)
    orbit={seed};q=deque([seed])
    while q:
        s=q.popleft()
        for i in range(5):
            r=min(swap(s,i),swap(F[s],i))
            assert period[r]==period[seed]
            if r not in orbit:orbit.add(r);q.append(r)
    assert orbit<=unseen
    unseen-=orbit
    classes.append((period[seed],basins[seed],len(orbit)))
classes.sort()
assert entry==Counter({(0,1):502,(0,2):5340,(1,1):4426,(1,2):3780,(2,1):13680,(3,1):5040})
assert hist==Counter({(1,1):360,(1,10):140,(1,10944):2,(2,2):2460,(2,20):210})
assert Counter(x[0] for x in classes)==Counter({1:8,2:18})
print('states',N)
for (t,p),v in sorted(entry.items()): print('entry',t,'period',p,'states',v)
for (p,b),v in sorted(hist.items()): print('basin period',p,'size',b,'orbits',v)
for k in classes: print('sym period',k[0],'basin',k[1],'orbit',k[2])
print('summary fixed',sum(p==1 for p in period.values()), 'two_orbits',sum(p==2 for p in period.values()), 'geometric_fixed',sum(t==1 for t,_,_ in classes),'geometric_two',sum(t==2 for t,_,_ in classes), 'sharp_entry 3')
