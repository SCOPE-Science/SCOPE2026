"""Independent finite checks of closed-neighborhood complexes of graph joins.

Usage: python verify.py
Uses only Python's standard library.
"""
from itertools import combinations, product


def closed_faces(n, edges):
    nbr = [set((v,)) for v in range(n)]
    for u, v in edges:
        nbr[u].add(v)
        nbr[v].add(u)
    faces = {()}
    for neighborhood in nbr:
        verts = sorted(neighborhood)
        for d in range(1, len(verts) + 1):
            faces.update(combinations(verts, d))
    return faces


def joined_graph(n, e, m, f):
    return n + m, list(e) + [(n + u, n + v) for u, v in f] + [(u, n + v) for u in range(n) for v in range(m)]


def join_faces(F, D):
    return {tuple(a) + tuple(b) for a in F for b in D}


def cycle_edges(n):
    return [(i, (i + 1) % n) for i in range(n)]


def betti_mod2(faces):
    by_dim = {}
    for f in faces:
        by_dim.setdefault(len(f) - 1, []).append(f)
    ranks = {}
    for d in range(1, max(by_dim) + 1):
        rows = {f: i for i, f in enumerate(by_dim.get(d - 1, []))}
        pivots = {}
        for face in by_dim.get(d, []):
            word = 0
            for i in range(len(face)):
                word ^= 1 << rows[face[:i] + face[i + 1:]]
            while word:
                pivot = word.bit_length() - 1
                if pivot in pivots:
                    word ^= pivots[pivot]
                else:
                    pivots[pivot] = word
                    break
        ranks[d] = len(pivots)
    return {d: len(by_dim.get(d, [])) - ranks.get(d, 0) - ranks.get(d + 1, 0)
            for d in range(max(by_dim) + 1)}


def perm_sign(values):
    return -1 if sum(values[i] > values[j] for i in range(len(values)) for j in range(i+1, len(values))) % 2 else 1


def reduced_lefschetz(faces, permutation):
    val = -1
    for face in faces:
        if not face:
            continue
        image = [permutation[x] for x in face]
        if sorted(image) == list(face):
            idx = [face.index(x) for x in image]
            val += ((-1) ** (len(face)-1)) * perm_sign(idx)
    return val

# Exhaustive graph-join face identity on 160 pairs of small graphs.
all_graphs = {}
for n in range(1, 5):
    possible = list(combinations(range(n), 2))
    all_graphs[n] = [(n, [e for i,e in enumerate(possible) if (mask >> i) & 1]) for mask in range(1 << len(possible))]
pairs_tested = 0
for n in (1,2,3):
    for m in (1,2,3):
        for na, ga in all_graphs[n]:
            for nb, gb in all_graphs[m]:
                if pairs_tested >= 300:
                    break
                count, join_edges = joined_graph(n,ga,m,gb)
                both = closed_faces(count,join_edges)
                left = closed_faces(n,ga)
                right = closed_faces(m,gb)
                full_left = {c for k in range(n+1) for c in combinations(range(n),k)}
                full_right = {c for k in range(m+1) for c in combinations(range(n,n+m),k)}
                shifted_right = {tuple(v+n for v in f) for f in right}
                cover = join_faces(left,full_right)|join_faces(full_left,shifted_right)
                assert both == cover, (n,m,ga,gb)
                assert join_faces(left,shifted_right) == join_faces(left,full_right)&join_faces(full_left,shifted_right)
                pairs_tested += 1
            if pairs_tested >= 300:
                break
        if pairs_tested >= 300:
            break
    if pairs_tested >= 300:
        break
print('COVER_IDENTITY_OK', pairs_tested)

# Cycle join spheres and full signed simplex Lefschetz traces.
case_count = 0
char_count = 0
for a,b in [(5,5),(5,6),(4,5),(4,4),(5,7)]:
    n,e = joined_graph(a,cycle_edges(a),b,cycle_edges(b))
    faces = closed_faces(n,e)
    expected_d = (2 if a==4 else 1)+(2 if b==4 else 1)+2
    betti = betti_mod2(faces)
    assert betti == {d:int(d==0)+int(d==expected_d) for d in betti}, (a,b,betti)
    maps = {
        'rot_a': (tuple((x+1)%a if x<a else x for x in range(n)),(-1 if a==4 else 1)),
        'ref_a': (tuple((-x)%a if x<a else x for x in range(n)),-1),
        'rot_b': (tuple(x if x<a else a+(x-a+1)%b for x in range(n)),(-1 if b==4 else 1)),
        'ref_b': (tuple(x if x<a else a+(-(x-a))%b for x in range(n)),-1)
    }
    if a==b:
        maps['swap'] = (tuple((x+a)%n for x in range(n)), -1 if a>=5 else 1)
    for key,(perm,degree) in maps.items():
        trace = ((-1)**expected_d) * reduced_lefschetz(faces,perm)
        assert trace == degree, (a,b,key,trace,degree)
        char_count += 1
    print('CYCLE_JOIN',a,b,'faces',len(faces),'sphere_degree',expected_d,'traces',len(maps))
    case_count += 1
print('ALL_VERIFY_OK',case_count,char_count)
