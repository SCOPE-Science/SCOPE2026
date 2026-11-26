"""Exact verifier for the node--trope incidence map of a genus-two Kummer quartic.

Requires SymPy. No finite-field sampling is used for the structural identities.
"""
import itertools
from collections import Counter
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

E = tuple(range(6))
PAIRS = tuple(frozenset(t) for t in itertools.combinations(E, 2))
TRIPLES = tuple(sorted(
    {frozenset((frozenset(t), frozenset(set(E)-set(t))))
     for t in itertools.combinations(E, 3)},
    key=lambda partition: tuple(sorted(tuple(sorted(t)) for t in partition))))
NODES = (None,) + PAIRS
TROPES = tuple(frozenset((i,)) for i in E) + TRIPLES
assert len(NODES) == len(TROPES) == 16

# M maps the free module on tropes into the free module on nodes.
M = sp.Matrix([
    [int(node is None or (node is not None and i in node))
     for i in E] +
    [int(node is not None and any(node <= block for block in triple))
     for triple in TRIPLES]
    for node in NODES
])
assert all(sum(M.row(i)) == 6 for i in range(16))
assert all(sum(M.col(i)) == 6 for i in range(16))
assert M*M.T == 4*sp.eye(16) + 2*sp.ones(16)
assert M.T*M == 4*sp.eye(16) + 2*sp.ones(16)
assert abs(M.det()) == 3*2**16

def factors(B):
    D = smith_normal_form(B, domain=sp.ZZ)
    d = tuple(abs(int(D[i, i])) for i in range(min(B.shape)))
    assert all(d[i+1] % d[i] == 0 for i in range(len(d)-1))
    return d

f = factors(M)
assert f == (1,)*6 + (2,)*4 + (4,)*5 + (12,)

def node_image(o, perm):
    return None if o is None else frozenset(perm[i] for i in o)

def trope_image(o, perm):
    if len(o) == 1 and isinstance(next(iter(o)), int):
        return frozenset(perm[i] for i in o)
    return frozenset(frozenset(perm[i] for i in block) for block in o)

def permutation_matrix(objects, perm, map_func):
    names = {o: i for i, o in enumerate(objects)}
    p = sp.zeros(len(objects))
    for j, o in enumerate(objects):
        p[names[map_func(o, perm)], j] = 1
    return p

def cycle_profile(P):
    nxt = [next(i for i in range(P.rows) if P[i,j]) for j in range(P.cols)]
    seen = set()
    result = []
    for k in range(len(nxt)):
        if k in seen: continue
        v = k; size = 0
        while v not in seen:
            seen.add(v); size += 1; v = nxt[v]
        result.append(size)
    return tuple(sorted(Counter(result).items()))

# Every element of S_6 preserves incidence and has equal node/trope
# permutation character, hence the same cycle profile for every power.
for perm in itertools.permutations(E):
    PN = permutation_matrix(NODES, perm, node_image)
    PT = permutation_matrix(TROPES, perm, trope_image)
    assert PN*M == M*PT
    assert cycle_profile(PN) == cycle_profile(PT)


def cycle_representative(part):
    perm = []
    j = 0
    for length in part:
        perm.extend(list(range(j+1, j+length)) + [j])
        j += length
    return tuple(perm)

def integer_partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for a in range(minimum, n+1):
            for rest in integer_partitions(n-a, a):
                yield (a,) + rest

EXPECTED = {
    (1,1,1,1,1,1): ((1,16),),
    (1,1,1,1,2): ((1,8),(2,4)),
    (1,1,1,3): ((1,4),(3,4)),
    (1,1,2,2): ((1,4),(2,6)),
    (1,1,4): ((1,2),(2,1),(4,3)),
    (1,2,3): ((1,2),(2,1),(3,2),(6,1)),
    (1,5): ((1,1),(5,3)),
    (2,2,2): ((1,4),(2,6)),
    (2,4): ((1,2),(2,1),(4,3)),
    (3,3): ((1,1),(3,5)),
    (6,): ((1,1),(3,1),(6,2)),
}
COINVARIANTS = {
    (1,1,1,1,1,1): (2,2,2,2,4,4,4,4,4,12),
    (1,1,1,1,2): (2,2,4,4,4,4,12),
    (1,1,1,3): (4,4,4,12),
    (1,1,2,2): (2,2,4,4,4,12),
    (1,1,4): (2,2,4,12),
    (1,2,3): (4,4,12),
    (1,5): (4,12),
    (2,2,2): (2,2,2,2,4,4,12),
    (2,4): (2,2,4,12),
    (3,3): (2,2,4,12),
    (6,): (2,2,12),
}
assert len(COINVARIANTS) == len(EXPECTED) == 11
for part in integer_partitions(6):
    perm = cycle_representative(part)
    PN = permutation_matrix(NODES, perm, node_image)
    assert cycle_profile(PN) == EXPECTED[part]
    # Q_F = Z^N / (im M + im(F-1)); the 16x32 integral matrix
    # has full row rank because det(M) is nonzero.
    all_f = factors(M.row_join(PN-sp.eye(16)))
    actual = tuple(x for x in all_f if x != 1)
    assert actual == COINVARIANTS[part], (part, actual)
    print('cycle-type',part,'profile',cycle_profile(PN),
          'coinvariants',actual)
assert COINVARIANTS[(1,1,2,2)] != COINVARIANTS[(2,2,2)]
print('VERIFY_OK: 720 equivariant incidence actions, Kummer 16x16 Smith form, 11 exact Frobenius coinvariant groups')
