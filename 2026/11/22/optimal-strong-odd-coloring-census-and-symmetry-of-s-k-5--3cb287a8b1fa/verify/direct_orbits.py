"""Independent 15-vertex graph verification, colorings, and all S_5 orbits.
No external libraries. Run: python3 direct_orbits.py
"""
from itertools import combinations, permutations, product
from collections import Counter

ROOTS=tuple(range(5))
EDGES=tuple(combinations(ROOTS,2))
EDGE_POS={e:i for i,e in enumerate(EDGES)}
# Ten subdivision vertices are numbered 5,...,14 in this edge order.
NEIGHBORS=[[] for _ in range(15)]
for j,(u,v) in enumerate(EDGES):
    w=5+j
    NEIGHBORS[w].extend((u,v))
    NEIGHBORS[u].append(w)
    NEIGHBORS[v].append(w)


def check(labels):
    if any(labels[u] == labels[v] for u in range(15) for v in NEIGHBORS[u]):
        return False
    for v in range(15):
        counts=Counter(labels[w] for w in NEIGHBORS[v])
        if any(k%2 == 0 for k in counts.values()):
            return False
    return True


def is_square(labels):
    return all(len({labels[w] for w in NEIGHBORS[v]}) == len(NEIGHBORS[v])
               for v in range(15))


def change_names(edge_labels,perm):
    out=[-1]*len(EDGES)
    for j,(u,v) in enumerate(EDGES):
        new_edge=tuple(sorted((perm[u],perm[v])))
        out[EDGE_POS[new_edge]]=perm[edge_labels[j]]
    return tuple(out)


def local_profile(labels):
    signature=[]
    for v in ROOTS:
        counts=Counter(labels[w] for w in NEIGHBORS[v])
        signature.append(tuple(sorted(counts.values())))
    return tuple(sorted(signature))


if __name__=='__main__':
    choices=[[c for c in ROOTS if c not in e] for e in EDGES]
    seen={}; total=0; sq=0; profile_hist=Counter()
    for entry in product(*choices):
        labels=ROOTS+entry
        if not check(labels):
            continue
        seen[entry]=is_square(labels)
        sq+=seen[entry]
        profile_hist[local_profile(labels)]+=1
        total+=1
    print('Candidates checked:', 3**10)
    print('Strong odd valid fixed-root assignments:',total)
    print('Square valid fixed-root assignments:',sq)
    print('Local profile histogram:',sorted(profile_hist.items()))
    perms=list(permutations(ROOTS))
    uncovered=set(seen)
    orbits=[]
    while uncovered:
        a=min(uncovered)
        orbit={change_names(a,p) for p in perms}
        assert orbit<=set(seen)
        assert len({seen[b] for b in orbit})==1
        uncovered-=orbit
        orbits.append((len(orbit),seen[a],a))
    orbits.sort(key=lambda a:(-a[0],a[1],a[2]))
    print('Orbit data (size, square, representative edge-color tuple):')
    for orbit in orbits:
        print(orbit)
    print('Total orbits:',len(orbits))
    assert (total,sq)==(201,6)
    assert len(orbits)==6
    assert sorted(o[0] for o in orbits)==[6,15,30,30,60,60]
    assert sum(o[0] for o in orbits)==201
    assert sum(s for size,s,a in orbits)==1
