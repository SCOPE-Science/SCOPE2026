from collections import Counter, defaultdict
from itertools import combinations

colors = [set(a) for a in combinations(range(5), 2)]
N = [frozenset(j for j,t in enumerate(colors) if s.isdisjoint(t)) for s in colors]
assert all(len(a)==3 for a in N)
assert all(len(a & b)<=1 for a,b in combinations(N,2))

def walks(w):
    if len(w)==6:
        if w[0] in N[w[-1]]:
            yield w
    else:
        for x in N[w[-1]]-set(w):
            yield from walks(w+(x,))

rooted = [w for a in range(10) for w in walks((a,))]
assert len(rooted)==120
hexagons = {min(w[k:]+w[:k] for k in range(6)) for w in rooted}
assert len(hexagons)==20
all_maps = set()
for w in sorted(hexagons):
    def triangle(i,j):
        v=[None]*8
        for k in range(7):
            v[(i+2+k)%8]=w[(j+k)%6]
        out=set()
        for color in N[w[j]]:
            v[(i+1)%8]=color
            out.add(tuple(v))
        return out
    for parity in (0,1):
        tt=[triangle(k%8,(k+parity)%6) for k in range(24)]
        membership=defaultdict(set)
        edges=set()
        for i,T in enumerate(tt):
            for v in T:membership[v].add(i)
            for e in combinations(T,2):edges.add(frozenset(e))
        assert len(edges)==72
        assert Counter(map(len,membership.values()))=={1:24,2:24}
        for i,T in enumerate(tt):
            assert Counter(len(membership[v]) for v in T)=={1:1,2:2}
            assert (set.union(*(membership[v] for v in T))-{i})=={(i-1)%24,(i+1)%24}
        assert not (set(membership) & all_maps)
        all_maps.update(membership)
        for v in membership:
            mutable=[]
            for k in range(8):
                possible=(N[v[k-1]] & N[v[(k+1)%8]])-{v[k]}
                if possible:mutable.append(k)
                for c in possible:
                    u=v[:k]+(c,)+v[k+1:]
                    assert frozenset((u,v)) in edges
            assert len(mutable)==1 or (len(mutable)==2 and (mutable[1]-mutable[0]) in (1,7))
assert len(all_maps)==1920
print('120 rooted directed hexagons; 20 oriented hexagons modulo rotation')
print('40 components checked: 24-triangle ring, 48 vertices, 72 edges each')
