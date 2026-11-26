"""Finite checks of the fold and the orbit-face correspondence."""
from itertools import combinations, permutations


def graph(k, ell):
    vertices = {(0,0)} | {(a,j) for a in range(1,k+1) for j in range(1,ell+1)}
    edges = [(0,0,a,1) for a in range(1,k+1)]
    edges += [(a,j,a,j+1) for a in range(1,k+1) for j in range(1,ell)]
    return vertices, {frozenset(((a,j),(b,h))) for a,j,b,h in edges}


def faces(k, ell):
    vertices, edges = graph(k, ell)
    return {frozenset(f) for t in range(len(vertices)+1) for f in combinations(vertices,t)
            if not any(e.issubset(f) for e in edges)}


for k,ell in ((3,3),(3,4),(3,5),(4,3)):
    fs = faces(k,ell)
    def fold(v):
        a,j = v
        return (a,ell) if j==ell-2 else v
    for f in fs:
        g = frozenset(map(fold,f))
        assert (f | g) in fs and all(fold(v)==v for v in g)

    identity = tuple(range(k+1))
    swap = (0,2,1)+tuple(range(3,k+1))
    groups = [(identity,), (identity,swap)]
    groups += [tuple((0,)+p for p in permutations(range(1,k+1)))]
    if k==4:
        swap34 = (0,1,2,4,3)
        groups.append((identity,swap,swap34,(0,2,1,4,3)))
    for group in groups:
        orbits = sorted({tuple(sorted({p[a] for p in group})) for a in range(1,k+1)})
        orbit_of = {a:i for i,orbit in enumerate(orbits,1) for a in orbit}
        orbit_of[0]=0
        observed = {frozenset((orbit_of[a],j) for a,j in f)
                    for f in fs if all(frozenset((p[a],j) for a,j in f)==f for p in group)}
        assert observed == faces(len(orbits),ell)
    print(k,ell,len(fs),len(groups))
print('FINITE_CHECKS_OK')
