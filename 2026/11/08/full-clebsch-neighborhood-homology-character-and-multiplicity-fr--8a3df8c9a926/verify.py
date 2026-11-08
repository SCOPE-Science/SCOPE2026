#!/usr/bin/env python3
"""Exact finite check of the Clebsch-neighborhood homology character.

Requires only Python 3 standard library. All objects are reconstructed here.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

NVERT = 16
V = range(NVERT)
DIRECTIONS = (1, 2, 4, 8, 15)
BASIS = (1, 2, 4, 8)
NEIGHBORS = [frozenset(x ^ s for s in DIRECTIONS) for x in V]
NEIGHBOR_MASKS = [sum(1 << x for x in nb) for nb in NEIGHBORS]


def submasks(mask):
    x = mask
    while x:
        yield x
        x = (x - 1) & mask


def faces_by_neighborhoods():
    return frozenset(m for nb in NEIGHBOR_MASKS for m in submasks(nb))


def faces_by_witnesses():
    out = set()
    for mask in range(1, 1 << NVERT):
        if any(mask & ~nb == 0 for nb in NEIGHBOR_MASKS):
            out.add(mask)
    return frozenset(out)


FACES = faces_by_neighborhoods()
assert FACES == faces_by_witnesses()
assert len(FACES) == 352
F_BY_SIZE = [tuple(sorted(f for f in FACES if f.bit_count() == size))
             for size in range(1, 6)]
assert [len(a) for a in F_BY_SIZE] == [16, 80, 160, 80, 16]
assert all(len(nb) == 5 for nb in NEIGHBORS)
assert all(len(NEIGHBORS[x] & NEIGHBORS[y]) ==
           (0 if x ^ y in DIRECTIONS else 2)
           for x in V for y in range(x + 1, NVERT))


def morse_matching():
    remaining = set(FACES)
    matched = set()
    for vertex in V:
        bit = 1 << vertex
        for face in sorted(remaining):
            coface = face | bit
            if face in remaining and (face & bit) == 0 and coface in remaining:
                remaining.remove(face)
                remaining.remove(coface)
                matched.add((face, coface))
    assert len(matched) == 160
    assert Counter(face.bit_count() - 1 for face in remaining) == {0: 1, 2: 31}
    vertices = tuple(sorted(FACES))
    in_degree = {f: 0 for f in vertices}
    arrows = {f: [] for f in vertices}
    incidence_count = 0
    for f in vertices:
        for vertex in V:
            if f & (1 << vertex):
                continue
            coface = f | (1 << vertex)
            if coface not in FACES:
                continue
            incidence_count += 1
            low, high = (coface, f) if (f, coface) in matched else (f, coface)
            arrows[low].append(high)
            in_degree[high] += 1
    assert incidence_count == 1040
    todo = deque(f for f in vertices if in_degree[f] == 0)
    processed = 0
    while todo:
        f = todo.popleft()
        processed += 1
        for g in arrows[f]:
            in_degree[g] -= 1
            if in_degree[g] == 0:
                todo.append(g)
    assert processed == len(FACES), "The Morse matching must be acyclic"
    return (len(matched), incidence_count, Counter(f.bit_count()-1 for f in remaining))


def invert_sign(values):
    inv = sum(values[i] > values[j] for i in range(len(values))
              for j in range(i + 1, len(values)))
    return -1 if inv & 1 else 1


def sign_on_subset(q, subset):
    order = sorted(subset)
    image = [q[i] for i in order]
    assert set(image) == set(order)
    return invert_sign(image)


def lin_map(generator_permutation):
    result = []
    for v in V:
        y = 0
        for i, base in enumerate(BASIS):
            if v & base:
                y ^= generator_permutation[i]
        result.append(y)
    assert result[15] == generator_permutation[4]
    return tuple(result)


def permute_face(face, map_v):
    out = 0
    while face:
        bit = face & -face
        out |= 1 << map_v[bit.bit_length() - 1]
        face -= bit
    return out


def trace_fixed_faces(map_v):
    lefschetz = 0
    for face in FACES:
        if permute_face(face, map_v) != face:
            continue
        vertices = [i for i in V if face & (1 << i)]
        sign = invert_sign([map_v[i] for i in vertices])
        lefschetz += (-1 if len(vertices) % 2 == 0 else 1) * sign
    return lefschetz - 1


def cycle_blocks(map_v):
    unseen = set(V)
    blocks = []
    while unseen:
        first = min(unseen)
        cycle = []
        v = first
        while v not in cycle:
            cycle.append(v)
            unseen.remove(v)
            v = map_v[v]
        assert v == first
        blocks.append(sum(1 << k for k in cycle))
    return tuple(blocks)


def trace_cycle_union(map_v):
    """Independent Lefschetz sum using invariant unions of vertex cycles.

    A union of b cycles contributes (-1)^(b-1), regardless of cycle lengths.
    """
    cycles = cycle_blocks(map_v)
    total = 0
    for count in range(1, min(5, len(cycles)) + 1):
        for inds in combinations(range(len(cycles)), count):
            mask = 0
            for i in inds:
                mask |= cycles[i]
            if mask in FACES:
                total += (-1 if count % 2 == 0 else 1)
    return total - 1


def character_negatives(w):
    return frozenset(i for i, d in enumerate(DIRECTIONS)
                     if (w & d).bit_count() & 1)


def perm_on_five(q):
    return tuple(DIRECTIONS.index(a) for a in q)


def sign_of_square(cycle_permutation):
    return invert_sign(cycle_permutation)


def expected_fiber_character(w, q):
    """Expected little-group character, or None if the character is moved."""
    neg = character_negatives(w)
    p = perm_on_five(q)
    if frozenset(p[i] for i in neg) != neg:
        return None
    n = len(neg)
    if n == 0:
        fix1 = sum(p[i] == i for i in range(5))
        fix2 = sum(p[p[i]] == i for i in range(5))
        return ((fix1 - 1) ** 2 - (fix2 - 1)) // 2
    if n == 2:
        positive = frozenset(range(5)) - neg
        return sign_on_subset(p, positive)
    assert n == 4
    fixed = sum(p[i] == i for i in neg)
    return sign_on_subset(p, neg) * (fixed - 1)



def translate_affine_map(x):
    cols = (14, 13, 11, 7)
    ans = 15
    for i in range(4):
        if x & (1 << i):
            ans ^= cols[i]
    return ans


def prior_four_cube_character(p, b):
    """Previously established closed-radius-one 4-cube Cech character."""
    from fractions import Fraction
    seen = set()
    cycles = []
    for i in range(4):
        if i in seen:
            continue
        cycle = []
        cur = i
        while cur not in seen:
            seen.add(cur)
            cycle.append(cur)
            cur = p[cur]
        assert cur == i
        cycles.append(cycle)
    r = len(cycles)
    a1 = sum(p[i] == i for i in range(4))
    a2 = sum(len(c) == 2 for c in cycles)
    D = a1 + a1 * (a1 - 1)//2 + a2
    def consistent(z):
        return all(sum(((b ^ z) >> i) & 1 for i in c) % 2 == 0
                   for c in cycles)
    F = (2 ** r) if consistent(0) else 0
    tau = sum(consistent(z) and all((z >> p[i] & 1) == (z >> i & 1)
                                    for i in range(4))
              for z in range(1, 16) if z.bit_count() in (1, 2))
    result = Fraction(F) * (1 - Fraction(D, 2) +
         a1*(a1-1)//2 - a2) + 2 ** (r-1)*tau - 1
    assert result.denominator == 1
    return int(result)


def check_closed_cube_correspondence(chars):
    # The closed stars of Q4 are affine translates of {0,1,2,4,8}.
    # This affine coordinate change converts their entire face system to the
    # open neighborhood complex of the Clebsch graph.
    A = (0, 1, 2, 4, 8)
    phi = tuple(translate_affine_map(x) for x in V)
    assert len(set(phi)) == 16
    assert {phi[x] for x in A} == set(DIRECTIONS)
    inverse = [0] * 16
    for x, y in enumerate(phi):
        inverse[y] = x
    Q4_F = frozenset(mask for b in V
        for mask in submasks(sum(1 << (b ^ a) for a in A)))
    assert len(Q4_F) == 352
    assert {permute_face(face,phi) for face in Q4_F} == FACES
    for p in permutations(range(4)):
        for b in V:
            def cube_action(x):
                z = b
                for i in range(4):
                    if x & (1 << i): z ^= 1 << p[i]
                return z
            g = tuple(phi[cube_action(inverse[x])] for x in V)
            assert g in CHECKED_GROUP_MAPS
            assert trace_fixed_faces(g) == prior_four_cube_character(p, b)
    return 384

def main():
    pairs, incidences, critical = morse_matching()
    assert (pairs, incidences, critical) == (160, 1040, {0: 1, 2: 31})
    # The distinct sums of two generator vectors exhaust the ten non-neighbors
    # of zero, so an automorphism fixing zero and its five neighbors is identity.
    assert len({DIRECTIONS[i] ^ DIRECTIONS[j]
                for i in range(5) for j in range(i + 1, 5)}) == 10
    assert set(DIRECTIONS) | {0} | {DIRECTIONS[i] ^ DIRECTIONS[j]
        for i in range(5) for j in range(i+1, 5)} == set(V)

    all_perms = tuple(permutations(DIRECTIONS))
    assert len(all_perms) == 120
    global CHECKED_GROUP_MAPS
    chars = {}
    maps = set()
    hist = Counter()
    for q in all_perms:
        lin = lin_map(q)
        for t in V:
            g = tuple(y ^ t for y in lin)
            assert g not in maps
            maps.add(g)
            assert all((g[x] ^ g[y] in DIRECTIONS) ==
                       (x ^ y in DIRECTIONS) for x in V for y in range(x + 1, NVERT))
            h = trace_fixed_faces(g)
            assert h == trace_cycle_union(g), (q, t, h)
            chars[(q, t)] = h
            hist[h] += 1
    assert len(maps) == 1920
    CHECKED_GROUP_MAPS = maps
    assert check_closed_cube_correspondence(chars) == 384
    assert hist == {-5: 80, -1: 825, 1: 944, 3: 60, 7: 10, 31: 1}
    assert sum(h * c for h, c in hist.items()) == 0

    mult = {}
    for w in V:
        neg = character_negatives(w)
        assert len(neg) in (0, 2, 4)
        theta = lambda t: (-1 if (w & t).bit_count() & 1 else 1)
        ident = DIRECTIONS
        coeff = sum(theta(t) * chars[(ident, t)] for t in V)
        assert coeff % 16 == 0
        mult[w] = coeff // 16
        assert mult[w] == {0: 6, 2: 1, 4: 3}[len(neg)]

    # Compare the Fourier-projected characters on all little-group elements.
    projected = 0
    for q in all_perms:
        for w in V:
            expect = expected_fiber_character(w, q)
            if expect is None:
                continue
            actual = sum((1 if (w & t).bit_count() % 2 == 0 else -1)
                         * chars[(q, t)] for t in V)
            assert actual == 16 * expect, (q, w, actual, expect)
            projected += 1
    assert projected == 120 + 10*12 + 5*24

    # Recover the character of every affine group element independently from
    # the three induced little-group representations.
    for q in all_perms:
        for t in V:
            pred = 0
            for w in V:
                term = expected_fiber_character(w, q)
                if term is not None:
                    pred += (1 if (w & t).bit_count() % 2 == 0 else -1) * term
            assert pred == chars[(q, t)], (q, t, pred, chars[(q, t)])

    trans = [chars[(DIRECTIONS,t)] for t in V]
    assert Counter(trans) == {31: 1, -1: 5, 7: 10}
    assert sum(trans) == 16*6
    assert sum(chars.values()) == 0
    print("GRAPH=16 vertices,40 edges,5-regular Clebsch graph")
    print("NEIGHBORHOOD_F_VECTOR=16,80,160,80,16")
    print("DISCRETE_MORSE=160 matched pairs,1040 incidences,critical (1 vertex,31 two-cells)")
    print("AUTOMORPHISMS=1920=16*120, exhaustive")
    print("LEFSCHETZ_AND_CYCLE_UNION=agree for all 1920")
    print("FULL_CHARACTER_DISTRIBUTION=-5:80,-1:825,1:944,3:60,7:10,31:1")
    print("TRANSLATION_CHARACTER=31:1,-1:5,7:10")
    print("DUAL_ORBITS=0:1,2:10,4:5; FIBER_DIMENSIONS=6,1,3")
    print("LITTLE_GROUP_TRACES=all 360 stabilizing pairs pass")
    print("FULL_INDUCED_CHARACTER=all 1920 group elements pass")
    print("Q4_CLOSED_CECH=affine isomorphism; 384 prior subgroup character checks pass")
    print("INVARIANT_RANK_G=0, INVARIANT_RANK_TRANSLATIONS=6")
    print("ALL_CHECKS_PASS")

if __name__ == "__main__":
    main()
