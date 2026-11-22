"""Exact power-domination reconfiguration census on the Tutte--Coxeter 8-cage.

This independent implementation uses 2-subsets (duads) and perfect matchings
(synthemes) of a six-element set. It exhaustively enumerates all candidate
four-sets, then uses verified incidence automorphisms to reduce shortest-path
checks to one BFS per orbit. Python 3 standard library only.
"""
from itertools import combinations, permutations
from collections import Counter, deque

SYMBOLS = tuple(range(6))
DUADS = tuple(combinations(SYMBOLS, 2))

def perfect_matchings(xs):
    if not xs:
        yield ()
        return
    a = xs[0]
    for b in xs[1:]:
        rest = tuple(v for v in xs if v != a and v != b)
        for tail in perfect_matchings(rest):
            yield tuple(sorted(((a, b),) + tail))

SYNTHEMES = tuple(sorted(set(perfect_matchings(SYMBOLS))))
assert len(DUADS) == len(SYNTHEMES) == 15
D_index = {x: i for i, x in enumerate(DUADS)}
L_index = {x: i + 15 for i, x in enumerate(SYNTHEMES)}
NEIGHBORS = [set() for _ in range(30)]
for i, p in enumerate(DUADS):
    for j, l in enumerate(SYNTHEMES):
        if p in l:
            NEIGHBORS[i].add(j + 15)
            NEIGHBORS[j + 15].add(i)
assert all(len(n) == 3 for n in NEIGHBORS)
assert sum(len(n) for n in NEIGHBORS) // 2 == 45
# Direct structural checks: the incidence graph is connected, has diameter 4 and girth 8.
def graph_structure():
    girth=999
    diameter=0
    for root in range(30):
        D={root:0};par={root:-1};Q=deque([root])
        while Q:
            u=Q.popleft()
            for v in NEIGHBORS[u]:
                if v not in D:
                    D[v]=D[u]+1;par[v]=u;Q.append(v)
                elif par[u]!=v:
                    girth=min(girth,D[u]+D[v]+1)
        assert len(D)==30
        diameter=max(diameter,max(D.values()))
    return girth,diameter
assert graph_structure()==(8,4)


# An explicit checked isomorphism to the symplectic-line realization.
# Vertex i on the duad side maps to ISO[i] in the symplectic representation.
ISO = (0,14,1,10,6,13,2,9,5,12,3,7,8,4,11,
       17,15,16,23,24,26,20,19,18,25,22,27,28,21,29)
assert sorted(ISO) == list(range(30))
def symp(x,y):
    return (((x&1)*((y>>1)&1)) ^ (((x>>1)&1)*(y&1)) ^
            (((x>>2)&1)*((y>>3)&1)) ^ (((x>>3)&1)*((y>>2)&1)))
iso_lines = tuple(sorted({tuple(sorted((x,y,x^y)))
    for x in range(1,16) for y in range(x+1,16) if symp(x,y)==0}))
assert len(iso_lines)==15
iso_neighbors=[set() for _ in range(30)]
for i in range(15):
    for j, line in enumerate(iso_lines):
        if (i+1) in line:
            iso_neighbors[i].add(15+j)
            iso_neighbors[15+j].add(i)
assert all(set(ISO[j] for j in NEIGHBORS[i]) == iso_neighbors[ISO[i]]
           for i in range(30))


def power_dominates(S):
    observed = set(S)
    for v in S:
        observed.update(NEIGHBORS[v])
    while True:
        new = {next(iter(NEIGHBORS[v] - observed)) for v in observed
               if len(NEIGHBORS[v] - observed) == 1}
        if not new:
            break
        observed.update(new)
    return len(observed) == 30


MINIMUM = ()
for k in range(1, 5):
    valid = [s for s in combinations(range(30), k) if power_dominates(s)]
    print(f"successful_size_{k}={len(valid)}")
    if k < 4:
        assert not valid
    else:
        assert len(valid) == 6540
        MINIMUM = tuple(valid)

INDEX = {s: i for i, s in enumerate(MINIMUM)}

def moves(restricted):
    adj = [set() for _ in MINIMUM]
    for i, S in enumerate(MINIMUM):
        keep = set(S)
        for old in S:
            for new in (NEIGHBORS[old] if restricted else set(range(30))):
                if new in keep:
                    continue
                target = tuple(sorted((keep - {old}) | {new}))
                if target in INDEX:
                    adj[i].add(INDEX[target])
    assert all(i in adj[j] for i, ns in enumerate(adj) for j in ns)
    return adj

JUMP = moves(False)
SLIDE = moves(True)

# A named self-duality of the incidence graph, explicitly checked below.
DUAL = (15,22,20,28,24,27,25,19,23,16,26,18,21,29,17,
        0,9,14,11,7,2,12,1,8,4,6,10,5,3,13)
assert len(set(DUAL)) == 30
assert all(set(DUAL[j] for j in NEIGHBORS[i]) == NEIGHBORS[DUAL[i]] for i in range(30))
assert all(DUAL[DUAL[i]] == i for i in range(30))

AUT = []
for p in permutations(SYMBOLS):
    def map_pair(pair):
        return tuple(sorted((p[pair[0]], p[pair[1]])))
    action = [D_index[map_pair(x)] for x in DUADS]
    action += [L_index[tuple(sorted(map(map_pair, m)))] for m in SYNTHEMES]
    AUT.append(tuple(action))
    AUT.append(tuple(DUAL[x] for x in action))
assert len(AUT) == 1440 and len(set(AUT)) == 1440
assert all(all(set(a[j] for j in NEIGHBORS[i]) == NEIGHBORS[a[i]]
               for i in range(30)) for a in AUT)

unassigned = set(MINIMUM)
ORBITS = []
while unassigned:
    rep = min(unassigned)
    orbit = {tuple(sorted(g[x] for x in rep)) for g in AUT}
    assert orbit <= set(MINIMUM)
    unassigned.difference_update(orbit)
    ORBITS.append((rep, len(orbit)))
assert len(ORBITS) == 10 and sum(m for _, m in ORBITS) == 6540


def distances(A, start):
    dist = [-1] * len(A)
    parents = [-1] * len(A)
    dist[start] = 0
    Q = deque([start])
    while Q:
        v = Q.popleft()
        for w in sorted(A[v]):
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                parents[w] = v
                Q.append(w)
    assert -1 not in dist
    return dist, parents


def report(A, tag):
    degree = Counter(); ecc = Counter(); distance_sum = Counter()
    for oi, (rep, multiplicity) in enumerate(ORBITS):
        i = INDEX[rep]
        d, _ = distances(A, i)
        e = max(d)
        degree[len(A[i])] += multiplicity
        ecc[e] += multiplicity
        for k, v in Counter(d).items():
            distance_sum[k] += multiplicity * v
        print(f"{tag}_orbit_{oi}={rep},mult:{multiplicity},degree:{len(A[i])},ecc:{e}")
    assert distance_sum[0] == len(A)
    undirected = {k: v//2 for k, v in sorted(distance_sum.items()) if k}
    assert all(v % 2 == 0 for k,v in distance_sum.items() if k)
    assert sum(undirected.values()) == 6540 * 6539 // 2
    print(f"{tag}_edges={sum(len(x) for x in A)//2}")
    print(f"{tag}_degrees={dict(sorted(degree.items()))}")
    print(f"{tag}_eccentricities={dict(sorted(ecc.items()))}")
    print(f"{tag}_distance_pairs={undirected}")
    return degree, ecc, undirected

j_degrees, j_ecc, j_dist = report(JUMP, "jump")
s_degrees, s_ecc, s_dist = report(SLIDE, "slide")
assert j_ecc == {4:6540} and sum(j_degrees.values()) == 6540
assert s_ecc == {11:1680,12:3420,13:1440}
assert s_dist[13] == 1440 and s_dist[1] == 23040

# Explicit extremal 13-slide path, reconstructed from the actual adjacency.
rep = ORBITS[3][0]
d, parent = distances(SLIDE, INDEX[rep])
far = min(i for i, x in enumerate(d) if x == 13)
path = []
while far >= 0:
    path.append(MINIMUM[far]); far = parent[far]
path.reverse()
assert len(path) == 14 and path[0] == rep
print('extremal_13_slide_path=' + ';'.join(','.join(map(str, s)) for s in path))
print('status=PASS')

def locality_profile():
    c = Counter(); per_orbit = []
    for i, (rep, mult) in enumerate(ORBITS):
        jd, _ = distances(JUMP, INDEX[rep]); sd, _ = distances(SLIDE, INDEX[rep]);
        local = Counter(x-y for x,y in zip(sd,jd))
        assert all((sd[t],jd[t])==(13,4) for t in range(len(sd)) if sd[t]-jd[t]==9)
        assert min(local) == 0
        per_orbit.append((i,max(local),local[max(local)]))
        for k,v in local.items():c[k]+=mult*v
    assert c[0] >= 6540
    for k,v in c.items():
        if k:assert v%2==0
    out={k:(v-6540 if k==0 else v)//2 for k,v in sorted(c.items())}
    assert sum(out.values()) == 6540*6539//2
    print('locality_excess_pairs=' + repr(out))
    print('locality_max_by_orbit=' + repr(per_orbit))
    return out
LOCALITY = locality_profile()
print('locality_status=PASS')
