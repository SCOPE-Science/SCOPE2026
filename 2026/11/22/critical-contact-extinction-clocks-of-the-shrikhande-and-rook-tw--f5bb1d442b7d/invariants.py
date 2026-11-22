"""Elementary checks of the two strongly regular graph representations."""
from fractions import Fraction
from itertools import combinations
from collections import Counter
N=16
MOVES={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
def adjacent(g,v,w):
    if v==w:return False
    a,b=v%4,v//4
    c,d=w%4,w//4
    if g==0:return a==c or b==d
    return ((c-a)%4,(d-b)%4) in MOVES
for g in [0,1]:
    rows=[{w for w in range(N) if adjacent(g,v,w)} for v in range(N)]
    assert all(len(x)==6 for x in rows)
    assert all(len(rows[v]&rows[w])==2 for v,w in combinations(range(N),2))
    assert all((v in rows[w])==(w in rows[v]) for v in range(N) for w in range(N))
    sizes=[len(rows[v]&rows[w]) for v,w in combinations(range(N),2) if w in rows[v]]
    assert len(sizes)==48
    # Difference in the two induced six-neighbor graphs is an invariant.
    u=0
    induced_edges=sum(v<w and w in rows[v] for v,w in combinations(sorted(rows[u]),2))
    assert induced_edges==6
    components=[];unseen=set(rows[u])
    while unseen:
        todo=[unseen.pop()]; size=0
        while todo:
            a=todo.pop();size+=1
            for b in rows[a]&rows[u]&unseen:
                unseen.remove(b);todo.append(b)
        components.append(size)
    assert sorted(components)==([3,3] if g==0 else [6])
    others=set(range(N))-rows[u]-{u}
    traces=[tuple(sorted(rows[w]&rows[u])) for w in others]
    assert len(traces)==9 and len(set(traces))==9
    print(('Rook' if g==0 else 'Shrikhande')+': srg(16,6,2,2), neighbor components '+str(sorted(components)))
print('INVARIANTS_OK')
