#!/usr/bin/env python3
"""Exact signed orbit-chain verification for the rank-four wheel-to-whirl inclusion."""
from itertools import combinations
from collections import defaultdict
from math import gcd

N = 4
RIM = (0, 1, 2, 3)
SPOKES = (4, 5, 6, 7)
EDGES = tuple((i, (i + 1) % N) for i in range(N)) + tuple((i, N) for i in range(N))


def sign(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))


def forest(face):
    parent = list(range(N + 1))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for e in face:
        a, b = EDGES[e]
        a, b = root(a), root(b)
        if a == b:
            return False
        parent[a] = b
    return True


def dihedral():
    for a in range(N):
        for eps in (1, -1):
            p = tuple((a + i) % N if eps == 1 else (a - i - 1) % N for i in range(N)) + tuple(N + (a + eps * i) % N for i in range(N))
            yield p, sign(p[:N])


def transform(face, p):
    word = tuple(p[i] for i in face)
    return tuple(sorted(word)), sign(word)


def orbit_cycle(seed):
    result = {}
    for p, character in dihedral():
        face, orient = transform(seed, p)
        coeff = character * orient
        if face in result:
            assert result[face] == coeff, ('inconsistent signed orbit', seed, face)
        result[face] = coeff
    return result


def boundary(chain):
    ans = defaultdict(int)
    for face, coeff in chain.items():
        for i in range(len(face)):
            ans[face[:i] + face[i + 1:]] += coeff * (-1)**i
    return {face: coeff for face, coeff in ans.items() if coeff}


def check():
    independent = {k:tuple(t for t in combinations(range(8), k) if forest(t)) for k in range(5)}
    whirl = tuple(sorted(independent[4] + (RIM,)))
    assert [len(independent[k]) for k in range(5)] == [1, 8, 28, 52, 45]
    assert len(whirl) == 46
    group = tuple(dihedral())
    assert len(group) == 8 and len({g[0] for g in group}) == 8
    # All eight permutations preserve both independence complexes.
    for p, char in group:
        assert char in (-1, 1)
        assert {transform(t, p)[0] for t in whirl} == set(whirl)
    unseen = set(whirl)
    orbit_seeds = []
    orbit_sizes = []
    while unseen:
        seed = min(unseen)
        images = {transform(seed, p)[0] for p, char in group}
        unseen -= images
        try:
            orb = orbit_cycle(seed)
        except AssertionError:
            continue
        orbit_seeds.append(seed)
        orbit_sizes.append(len(orb))
    assert len(orbit_seeds) == 6
    assert set(orbit_seeds) == {(0,1,2,3),(0,1,2,4),(0,1,2,5),(0,1,4,7),(0,2,4,6),(0,4,6,7)}
    weights = {(0,1,2,3):-2, (0,1,2,4):1, (0,1,4,7):1, (0,2,4,6):-1, (0,4,6,7):1}
    z = defaultdict(int)
    for seed, scalar in weights.items():
        for face, c in orbit_cycle(seed).items():
            z[face] += scalar * c
    z = {t:c for t,c in z.items() if c}
    assert set(z).issubset(set(whirl))
    assert z[RIM] == -2
    assert not boundary(z), boundary(z)
    for p, character in group:
        transformed = defaultdict(int)
        for face, coefficient in z.items():
            image, s = transform(face, p)
            transformed[image] += s * coefficient
        assert transformed == {t:character*c for t,c in z.items()}
    # A reflection fixing missing rim edge 0 pairs all four spokes.
    reflected, chi = next((p,c) for p,c in group if p[:4] == (0,3,2,1))
    missing = (1,2,3)
    assert chi == -1 and transform(missing, reflected) == (missing,-1)
    cofaces = [t for t in whirl if set(missing).issubset(t)]
    assert len(cofaces) == 5 and RIM in cofaces
    others = [t for t in cofaces if t != RIM]
    assert {transform(t, reflected)[0] for t in others} == set(others)
    assert all(transform(t, reflected)[0] != t for t in others)
    # In a chi-equivariant cycle, reflected coface pairs contribute equally
    # to the missing-rim-edge boundary. Thus any rim coefficient is even.
    # The explicitly verified z achieves the lower positive multiplier two.
    print('INDEPENDENT_FACE_COUNTS', [len(independent[k]) for k in range(5)])
    print('WHIRL_TOP_FACE_COUNT', len(whirl))
    print('D4_ORDER', len(group))
    print('SIGNED_TOP_ORBIT_SEEDS_AND_SIZES', list(zip(orbit_seeds,orbit_sizes)))
    print('CYCLE_TERMS', len(z))
    print('SIGNED_RIM_COEFFICIENT',z[RIM])
    print('BOUNDARY_ZERO',not boundary(z))
    print('REFLECTION_PAIR_OBSTRUCTION', len(others)//2)
    print('EXACT_INTEGRAL_EQUIVARIANT_LIFTING_INDEX',2)
    print('WHEEL_WHIRL_FOUR_DIHEDRAL_INDEX_TWO_PASS')

if __name__ == '__main__':
    check()
