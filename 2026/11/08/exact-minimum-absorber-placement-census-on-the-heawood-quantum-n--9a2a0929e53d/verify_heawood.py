"""Exact census of six-absorber sets on the Fano-plane incidence graph.

Run: python3 verify_heawood.py  (Python 3.9+, standard library).
The geometric rank certificate uses exact integer elimination; the independently
constructed adjacency Krylov ranks are checked modulo the prime 1000003.
"""
from collections import Counter
from itertools import combinations, product

POINTS = tuple(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a, b in combinations(POINTS, 2)}))
assert len(LINES) == 7 and all(len(l) == 3 for l in LINES)
line_index = {l: i for i, l in enumerate(LINES)}
ROWS = ([[int(i == p) for i in POINTS] for p in POINTS] +
        [[int(p in l) for p in POINTS] for l in LINES])
ONES = [1] * 7
N = 14
A = [[0] * N for _ in range(N)]
for p in range(7):
    for l in range(7):
        A[p][l + 7] = A[l + 7][p] = ROWS[7 + l][p]
assert sum(sum(row) for row in A) == 42
assert all(sum(row) == 3 for row in A)

# Pivot-free rank over the rationals, using fraction-free integer elimination.
def rank_exact(rows):
    m = [list(r) for r in rows]
    rank = 0
    for j in range(len(m[0])):
        pivot = next((k for k in range(rank, len(m)) if m[k][j]), None)
        if pivot is None:
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        v = m[rank][j]
        for k in range(rank + 1, len(m)):
            if m[k][j]:
                w = m[k][j]
                m[k] = [v*x - w*y for x, y in zip(m[k], m[rank])]
        rank += 1
        if rank == len(m):
            break
    return rank

# A separate Krylov construction for the full adjacency Hamiltonian.
# The minimal polynomial divides (x^2-9)(x^2-2), so powers 0,1,2,3 suffice.
# The rank is computed over a large prime, independently of rank_exact.
PRIME = 1000003

def rank_mod_p(rows):
    m = [list(r) for r in rows]
    r = 0
    for j in range(len(m[0])):
        pivot = next((k for k in range(r, len(m)) if m[k][j] % PRIME), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inv = pow(m[r][j] % PRIME, -1, PRIME)
        for k in range(r + 1, len(m)):
            x = m[k][j] % PRIME
            if x:
                f = (x * inv) % PRIME
                for c in range(j + 1, len(m[0])):
                    m[k][c] = (m[k][c] - f*m[r][c]) % PRIME
                m[k][j] = 0
        r += 1
        if r == len(m):
            break
    return r

def krylov_full(sites):
    cols = []
    for s in sites:
        v = [int(i == s) for i in range(N)]
        for _ in range(4):
            cols.append(v)
            v = [sum(A[i][j]*v[j] for j in range(N)) for i in range(N)]
    return rank_mod_p([[col[i] for col in cols] for i in range(N)]) == N

SIX = tuple(combinations(range(N), 6))
assert len(SIX) == 3003
classified = {}
counts = Counter()
for sites in SIX:
    success = rank_exact([ONES] + [ROWS[i] for i in sites]) == 7
    assert krylov_full(sites) == success, sites
    classified[sites] = success
    counts[sum(i < 7 for i in sites), success] += 1
EXPECTED_SUCCESS = (7, 84, 420, 868, 420, 84, 7)
EXPECTED_FAILURE = (0, 63, 315, 357, 315, 63, 0)
assert tuple(counts[k, True] for k in range(7)) == EXPECTED_SUCCESS
assert tuple(counts[k, False] for k in range(7)) == EXPECTED_FAILURE

# Check the complete order-336 incidence-graph symmetry action and classify
# all six-site sets into exactly 24 orbits (14 good, 10 bad).
perms = set()
for a, b, c in product(POINTS, repeat=3):
    if len({a, b, c}) != 3 or a ^ b ^ c == 0:
        continue
    def f(x):
        return ((a if x & 1 else 0) ^ (b if x & 2 else 0)
                ^ (c if x & 4 else 0))
    perm = (tuple(f(x)-1 for x in POINTS) +
            tuple(7 + line_index[tuple(sorted(f(x) for x in l))]
                  for l in LINES))
    assert sorted(perm) == list(range(N))
    perms.add(perm)
assert len(perms) == 168
# Orthogonality polarity interchanges Fano points with lines.
pol = [None]*N
for p in POINTS:
    l = tuple(x for x in POINTS if (p & x).bit_count() % 2 == 0)
    pol[p-1] = 7 + line_index[l]
    pol[7 + line_index[l]] = p-1
assert sorted(pol) == list(range(N))
perms |= {tuple(pol[x] for x in g) for g in tuple(perms)}
assert len(perms) == 336
for g in perms:
    assert all(A[i][j] == A[g[i]][g[j]] for i in range(N) for j in range(N))
remaining = set(SIX)
orbits = []
while remaining:
    representative = min(remaining)
    orbit = {tuple(sorted(g[i] for i in representative)) for g in perms}
    assert orbit <= remaining
    remaining -= orbit
    assert all(classified[s] == classified[representative] for s in orbit)
    orbits.append((len(orbit), classified[representative]))
assert len(orbits) == 24
assert sum(n for n, good in orbits if good) == 1890
assert sum(good for _, good in orbits) == 14
assert sum(not good for _, good in orbits) == 10

print('VERIFY_OK vertices=14 edges=21 spectral_threshold=6')
print('VERIFY_OK six_subsets=3003 successful=1890 unsuccessful=1113')
print('VERIFY_OK success_by_points=7,84,420,868,420,84,7')
print('VERIFY_OK symmetry_order=336 orbits=24 good_orbits=14')
print('VERIFY_OK independent_Krylov_modular_crosschecks=3003')
