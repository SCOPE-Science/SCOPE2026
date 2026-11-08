"""Independent inclusion-exclusion in the Grothendieck ring for six coordinates.
Each intersection is a projective linear space determined by a signed graph.
Pure Python and characteristic-independent over fields with 2 invertible.
"""
from collections import Counter

def matchings(items):
    if not items:
        yield ()
        return
    a,*tail=items
    for j,b in enumerate(tail):
        for rest in matchings(tail[:j]+tail[j+1:]):
            yield ((a,b),)+rest

M=list(matchings(list(range(6))))
assert len(M)==15

def bipartite_components(edges):
    adj=[[] for _ in range(6)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    color={}
    good=0
    for i in range(6):
        if i in color: continue
        stack=[i]; color[i]=0; ok=True
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w not in color:
                    color[w]=1-color[v]
                    stack.append(w)
                elif color[w]==color[v]:
                    ok=False
        if ok: good+=1
    return good

coef=Counter()
for mask in range(1,1<<len(M)):
    edges=set()
    for j,matching in enumerate(M):
        if mask>>j&1: edges.update(tuple(sorted(e)) for e in matching)
    b=bipartite_components(edges)
    s=-1 if mask.bit_count()%2==0 else 1
    for j in range(b): coef[j]+=s
assert {j:coef[j] for j in range(3)}=={0:25,1:-30,2:15}
assert all(v==0 for j,v in coef.items() if j>=3)
print('Grothendieck class coefficients',dict(sorted(coef.items())))
print('PASS')
