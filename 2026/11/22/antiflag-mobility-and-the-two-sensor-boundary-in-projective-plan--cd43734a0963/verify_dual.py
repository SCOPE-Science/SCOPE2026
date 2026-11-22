"""Independent, cyclic difference-set construction and local-move audit."""
from itertools import combinations
from collections import Counter

# Use a cyclic projective difference set, not the binary-vector construction.
D={0,1,3}
N=14
edges={(p,7+l) for p in range(7) for l in range(7) if ((p-l)%7 in D)}
neighbor=[set() for _ in range(N)]
for u,v in edges:
    neighbor[u].add(v);neighbor[v].add(u)
assert len(edges)==21 and all(len(x)==3 for x in neighbor)
def pd(s):
    yes=set(s)
    for x in s:yes.update(neighbor[x])
    for _ in range(N):
        before=len(yes)
        for x in tuple(yes):
            y=neighbor[x]-yes
            if len(y)==1: yes.update(y)
        if len(yes)==before:break
    return len(yes)==N
opt=[frozenset(c) for c in combinations(range(N),2) if pd(c)]
assert len(opt)==28
assert all(min(s)<7<=max(s) and (min(s),max(s)) not in edges for s in opt)
assert all(not pd([u]) for u in range(N))
A={s:set() for s in opt}
for x,y in combinations(opt,2):
    if len(x&y)==1:A[x].add(y);A[y].add(x)
assert all(len(A[x])==6 for x in opt)
# Structural graph equality: edges of a 4-regular nonincidence bipartite graph.
B={(p,7+l) for p in range(7) for l in range(7) if (p,7+l) not in edges}
assert set(tuple(sorted(x)) for x in opt)==B
assert all(len([e for e in B if v in e])==4 for v in range(N))
assert sum(len(q) for q in A.values())==168
profile=Counter(); npaths=Counter()
for ix,s in enumerate(opt):
    layer={s};done={s};distance={s:0};count={s:1}
    for depth in range(1,5):
        cand=set()
        for v in layer:
            for w in A[v]:
                if w not in done:cand.add(w)
        if not cand:break
        for w in cand:distance[w]=depth;count[w]=sum(count[v] for v in A[w] if distance.get(v)==depth-1)
        done|=cand;layer=cand
    assert len(done)==28 and max(distance.values())==3
    for t in opt[ix+1:]: profile[distance[t]]+=1;npaths[distance[t],count[t]]+=1
assert profile==Counter({1:84,2:210,3:84})
assert npaths==Counter({(1,1):84,(2,1):168,(2,2):42,(3,4):84})
print('PASS cyclic-design model; optimums=nonincidences, line-graph profile and geodesics confirmed')
