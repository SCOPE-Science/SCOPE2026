#!/usr/bin/env python3
"""Exact rational and modular chain certificate for M(C5 square K2).

Python 3 and SymPy are required. No external data files are used.
The script enumerates all matchings in the 15-edge pentagonal prism.
"""
from collections import defaultdict
from itertools import combinations
from sympy import SparseMatrix

N = 5
VERTICES = range(2 * N)
EDGES = sorted(
    {tuple(sorted((a*N+i, a*N+(i+1)%N)))
     for a in range(2) for i in range(N)}
    | {(i, i+N) for i in range(N)}
)
assert len(EDGES) == 15
EDGENO = {e: j for j, e in enumerate(EDGES)}
# C[k] is the augmented simplicial chain group in dimension k-1.
FACES = [[()]]
for k in range(1, N+1):
    FACES.append([
        t for t in combinations(range(len(EDGES)), k)
        if len({v for j in t for v in EDGES[j]}) == 2*k
    ])
assert list(map(len, FACES)) == [1, 15, 75, 145, 95, 11]
INDEX = [{f: j for j, f in enumerate(row)} for row in FACES]


def boundary(k):
    """Integer entries of ∂: C[k] -> C[k-1]."""
    return {
        (INDEX[k-1][face[:i] + face[i+1:]], column): (-1)**i
        for column, face in enumerate(FACES[k])
        for i in range(k)
    }

BOUNDARY = [None] + [boundary(k) for k in range(1, 6)]
for k in range(2, 6):
    for s in FACES[k]:
        cancellation = defaultdict(int)
        for i in range(k):
            t = s[:i] + s[i+1:]
            for j in range(k-1):
                v = t[:j] + t[j+1:]
                cancellation[v] += (-1)**(i+j)
        assert all(v == 0 for v in cancellation.values())

# Exact ranks over Q (not merely finite-field estimates).
EXACT_RANKS = []
for k in range(1, 6):
    mat = SparseMatrix(len(FACES[k-1]), len(FACES[k]), BOUNDARY[k])
    EXACT_RANKS.append(int(mat.rank()))
assert EXACT_RANKS == [1, 14, 61, 82, 11], EXACT_RANKS
# Number of generators in C[k] less ranks of incoming/outgoing arrows.
BETTI_AUG = [
    len(FACES[k]) - (EXACT_RANKS[k-1] if k >= 1 else 0)
    - (EXACT_RANKS[k] if k < 5 else 0)
    for k in range(6)
]
assert BETTI_AUG == [0, 0, 0, 2, 2, 0], BETTI_AUG


def vertex_action(shift=0, reverse=0, switch=0):
    def fn(x):
        return ((-1 if reverse else 1)*(x % N) + shift) % N + N*((x//N + switch) % 2)
    edge_action = tuple(EDGENO[tuple(sorted(map(fn, e)))] for e in EDGES)
    assert sorted(edge_action) == list(range(15))
    return edge_action


def chain_action(k, edge_action):
    result = []
    for s in FACES[k]:
        t = [edge_action[i] for i in s]
        inversions = sum(t[i] > t[j] for i in range(k) for j in range(i+1, k))
        result.append((INDEX[k][tuple(sorted(t))], (-1)**inversions))
    return result

# Every generator acts by an actual signed chain automorphism.
for shift in range(5):
    for reverse in range(2):
        for switch in range(2):
            p = vertex_action(shift, reverse, switch)
            action = [chain_action(k, p) for k in range(6)]
            for k in range(1, 6):
                for col, s in enumerate(FACES[k]):
                    target, sign = action[k][col]
                    lhs = defaultdict(int)
                    rhs = defaultdict(int)
                    for a in range(k):
                        s_del = INDEX[k-1][s[:a] + s[a+1:]]
                        j, sg = action[k-1][s_del]
                        lhs[j] += (-1)**a * sg
                        j2 = INDEX[k-1][FACES[k][target][:a] + FACES[k][target][a+1:]]
                        rhs[j2] += sign*(-1)**a
                    assert dict(lhs) == dict(rhs)
            # Reduced Lefschetz formula using the augmented chain complex.
            alt_trace = 0
            for k in range(6):
                alt_trace += (-1 if k % 2 == 0 else 1) * sum(sgn for j, (new_j, sgn) in enumerate(action[k]) if new_j == j)
            predicted = -4 if reverse and switch else 0
            assert alt_trace == predicted, (shift, reverse, switch, alt_trace)


def modular_rank(columns, prime=1000003):
    # Sparse column Gaussian elimination over a finite field.
    pivots = {}
    for row in columns:
        work = {k: v % prime for k, v in row.items() if v % prime}
        while work:
            j = min(work)
            if j not in pivots:
                inverse = pow(work[j], -1, prime)
                pivots[j] = {u: (v * inverse) % prime for u, v in work.items()}
                break
            mul = work[j]
            for u, v in pivots[j].items():
                work[u] = (work.get(u, 0) - mul * v) % prime
                if work[u] == 0:
                    del work[u]
    return len(pivots)


def eigen_boundary_ranks(p, eigenvalue):
    """For involution p, compute ±-eigencomplex boundary ranks mod prime.

    An orbit basis for a two-cycle i->sign*j is e_i + eigenvalue*sign*e_j.
    Invariant boundaries are projected by reading the representative coefficient.
    """
    eigbases = []
    representatives = []
    for k in range(6):
        act = chain_action(k, p)
        assert all(act[act[i][0]][0] == i and act[act[i][0]][1]*act[i][1] == 1
                   for i in range(len(act)))
        used = set()
        vecs = []
        representatives_k = {}
        for i, (j, sign) in enumerate(act):
            if i in used:
                continue
            used.update((i, j))
            if i == j:
                if sign == eigenvalue:
                    representatives_k[i] = len(vecs)
                    vecs.append({i: 1})
            else:
                representatives_k[i] = len(vecs)
                vecs.append({i: 1, j: eigenvalue * sign})
        eigbases.append(vecs)
        representatives.append(representatives_k)
    ranks = []
    for k in range(1, 6):
        target = representatives[k-1]
        columns = []
        for basis_vector in eigbases[k]:
            col = defaultdict(int)
            for i, coef in basis_vector.items():
                face = FACES[k][i]
                for a in range(k):
                    j = INDEX[k-1][face[:a] + face[a+1:]]
                    if j in target:
                        col[target[j]] += (-1)**a * coef
            columns.append(dict(col))
        ranks.append(modular_rank(columns))
    betti = [
        len(eigbases[k]) - (ranks[k-1] if k > 0 else 0)
        - (ranks[k] if k < 5 else 0)
        for k in range(6)
    ]
    return ranks, betti, list(map(len, eigbases))

# Exact rank of each rational eigen-boundary is proved by combining the
# certified modular LOWER bounds with their exact sum over Q.
INVOLUTIONS = {
    'reflection': vertex_action(reverse=1),
    'layer swap': vertex_action(switch=1),
    'reflection then swap': vertex_action(reverse=1, switch=1),
}
EXPECTED = {
    'reflection': ([1, 8, 29, 39, 6], [0, 6, 32, 43, 5]),
    'layer swap': ([1, 9, 31, 38, 6], [0, 5, 30, 44, 5]),
    'reflection then swap': ([1, 7, 27, 43, 7], [0, 7, 34, 39, 4]),
}
for name, perm in INVOLUTIONS.items():
    (plus, bp, cp) = eigen_boundary_ranks(perm, 1)
    (minus, bm, cm) = eigen_boundary_ranks(perm, -1)
    assert (plus, minus) == EXPECTED[name]
    assert [x+y for x, y in zip(plus, minus)] == EXACT_RANKS
    # Since rank_modp <= rank_Q and the Q eigenranks sum to exact global
    # rank_Q, all these lower bounds are equalities over Q.
    assert [x+y for x, y in zip(bp, bm)] == BETTI_AUG
    if name == 'reflection then swap':
        assert bp[3:5] == [0, 2] and bm[3:5] == [2, 0]
    else:
        assert bp[3:5] == [1, 1] and bm[3:5] == [1, 1]
    print(f'{name}: (+) boundary ranks {plus}; (-) {minus}; ' 
          f'H2+/H2-={bp[3]}/{bm[3]}, H3+/H3-={bp[4]}/{bm[4]}')

print('face counts including empty:', [len(f) for f in FACES])
print('exact rational boundary ranks:', EXACT_RANKS)
print('reduced rational Betti numbers H0..H4:', BETTI_AUG[1:])
print('group order: 20; all chain equivariances and Lefschetz traces verified')
print('rotations act trivially on two-dimensional rational modules: cyclotomic degree 4')
print('H2 = reflection-sign + layer-sign; H3 = trivial + product-sign')
print('rational quotient cohomology: Q in degrees 0 and 3 only')
print('PENTAGONAL_PRISM_MATCHING_REPRESENTATIONS_EXACT_PASS')
