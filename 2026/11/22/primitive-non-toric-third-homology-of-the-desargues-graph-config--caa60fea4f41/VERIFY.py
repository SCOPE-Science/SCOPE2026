"""Reproduce exact degree-three Desargues graph configuration homology certificates.

Python 3.10+ standard library only. Run next to desargues_certificate.json.
"""
import itertools
import json
from collections import defaultdict
from pathlib import Path

V = tuple(itertools.combinations(range(5), 2)) + tuple(itertools.combinations(range(5), 3))
vi = {v: i for i, v in enumerate(V)}
E = tuple((vi[s], vi[t]) for s in V[:10] for t in V[10:] if set(s) <= set(t))
edge_id = {tuple(sorted(e)): i for i, e in enumerate(E)}
A = [[] for _ in V]
for i, (u, v) in enumerate(E):
    A[u].append((v, i)); A[v].append((u, i))
base = [x[0][1] for x in A]
local = [(v, e) for v in range(20) for _, e in A[v][1:]]
C3 = [x for x in itertools.combinations(local, 3) if len({z[0] for z in x}) == 3]
C2 = [(a, b, e) for a, b in itertools.combinations(local, 2) if a[0] != b[0] for e in range(30)]
ix2 = {c: i for i, c in enumerate(C2)}
ix3 = {c: i for i, c in enumerate(C3)}
assert (len(V), len(E), len(C3), len(C2)) == (20, 30, 9120, 22800)

def boundary3(c):
    out = defaultdict(int)
    for j, (v, e) in enumerate(c):
        rem = c[:j] + c[j + 1:]
        out[ix2[(*rem, e)]] += (-1) ** j
        out[ix2[(*rem, base[v])]] -= (-1) ** j
    return {k: v for k, v in out.items() if v}

def rank_mod_prime(columns, p):
    pivots = {}
    for c in columns:
        d = {k: v % p for k, v in boundary3(c).items() if v % p}
        while d:
            shared = [r for r in d if r in pivots]
            if not shared:
                break
            r = max(shared); a = d[r]
            for k, v in pivots[r].items():
                nv = (d.get(k, 0) - a * v) % p
                if nv: d[k] = nv
                else: d.pop(k, None)
        if d:
            r = max(d); inverse = pow(d[r], -1, p)
            pivots[r] = {k: v * inverse % p for k, v in d.items()}
    return len(pivots)

cert = json.loads((Path(__file__).parent / 'desargues_certificate.json').read_text('utf-8'))
free = cert['free_column_ids']
assert len(free) == 21 and len(set(free)) == 21
assert rank_mod_prime((c for i, c in enumerate(C3) if i not in set(free)), 3) == 9099
assert rank_mod_prime(iter(C3), 2) == 9094

basis = [{int(k): int(v) for k, v in d.items()} for d in cert['extra_basis']]
assert len(basis) == 21
for i, vec in enumerate(basis):
    assert [vec.get(f, 0) for f in free] == [int(i == j) for j in range(21)]
    result = defaultdict(int)
    for k, a in vec.items():
        for r, b in boundary3(C3[k]).items(): result[r] += a * b
    assert all(v == 0 for v in result.values()), ('nonzero boundary', i)
print('DESARGUES_TOP_INTEGER_KERNEL_21_OK')

cycles = []
for first in range(20):
    def walk(v, used, path):
        for w, _ in A[v]:
            if w == first and len(path) >= 6:
                if path[1] < path[-1]: cycles.append(tuple(path))
            elif w > first and w not in used:
                walk(w, used | {w}, path + [w])
    walk(first, {first}, [first])
assert len(cycles) == 1456
triples = []
for i in range(len(cycles)):
    si = set(cycles[i])
    for j in range(i + 1, len(cycles)):
        sj = set(cycles[j])
        if si & sj: continue
        for k in range(j + 1, len(cycles)):
            if si & set(cycles[k]) or sj & set(cycles[k]): continue
            triples.append((cycles[i], cycles[j], cycles[k]))
assert len(triples) == 20 and all(tuple(map(len, t)) == (6, 6, 6) for t in triples)
assert [[list(x) for x in t] for t in triples] == cert['tori_triples']

def single_loop(C):
    result = defaultdict(int)
    for i, v in enumerate(C):
        a = edge_id[tuple(sorted((v, C[i - 1])))]
        b = edge_id[tuple(sorted((v, C[(i + 1) % len(C)])))]
        if a != base[v]: result[(v, a)] += 1
        if b != base[v]: result[(v, b)] -= 1
    return {k: v for k, v in result.items() if v}

def torus_chain(C1, C2, C3_):
    result = defaultdict(int)
    for z1, z2, z3 in itertools.product(single_loop(C1).items(), single_loop(C2).items(), single_loop(C3_).items()):
        xyz = (z1[0], z2[0], z3[0]); coeff = z1[1] * z2[1] * z3[1]
        order = sorted(range(3), key=lambda k: xyz[k])
        sign = (-1) ** sum(order[i] > order[j] for i in range(3) for j in range(i + 1, 3))
        result[ix3[tuple(xyz[i] for i in order)]] += sign * coeff
    return {k: v for k, v in result.items() if v}

M = [[0] * 20 for _ in range(21)]
for j, t in enumerate(triples):
    z = torus_chain(*t)
    bdy = defaultdict(int)
    for k, a in z.items():
        for r, b in boundary3(C3[k]).items(): bdy[r] += a * b
    assert all(v == 0 for v in bdy.values())
    for i, f in enumerate(free): M[i][j] = z.get(f, 0)
assert M == cert['torus_free_coordinate_matrix']

def bareiss_det(A):
    A = [row[:] for row in A]; n = len(A); sign = 1; old = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            j = next((j for j in range(k + 1, n) if A[j][k]), None)
            if j is None: return 0
            A[k], A[j] = A[j], A[k]; sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * pivot - A[i][k] * A[k][j]
                assert num % old == 0
                A[i][j] = num // old
        for i in range(k + 1, n): A[i][k] = 0
        old = pivot
    return sign * A[-1][-1]
assert bareiss_det([row for i, row in enumerate(M) if i != 7]) == 1
print('DESARGUES_TWENTY_PRIMITIVE_HEXAGON_TORI_OK')
print('DESARGUES_GRAPH_THREE_POINT_TOPOLOGY_CERTIFICATE_OK')
