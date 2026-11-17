"""Independent finite checks for orbit-matching fixed chessboard models.

Only the Python standard library is required. These checks corroborate finite
examples; the general equivalence is proved separately.
"""
from itertools import combinations, permutations
from collections import defaultdict
from math import comb, factorial


def close_group(nr, nc, generators):
    identity = (tuple(range(nr)), tuple(range(nc)))
    seen = {identity}
    stack = [identity]
    while stack:
        a, b = stack.pop()
        for g, h in generators:
            z = (tuple(g[a[i]] for i in range(nr)),
                 tuple(h[b[j]] for j in range(nc)))
            if z not in seen:
                seen.add(z)
                stack.append(z)
    return sorted(seen)


def orbit_sets(length, permutations):
    unseen = set(range(length))
    result = []
    while unseen:
        x = min(unseen)
        o = frozenset(p[x] for p in permutations)
        result.append(o)
        unseen -= o
    return result


def equivariant_bijections(ri, cj, group):
    x = min(ri)
    all_maps = set()
    for y in cj:
        mapping = {}
        good = True
        for pr, pc in group:
            a, b = pr[x], pc[y]
            if a in mapping and mapping[a] != b:
                good = False
                break
            mapping[a] = b
        if good and len(mapping) == len(ri) == len(cj) and set(mapping.values()) == set(cj):
            if all(mapping[pr[u]] == pc[mapping[u]] for pr, pc in group for u in ri):
                all_maps.add(frozenset(mapping.items()))
    return all_maps


def check_case(label, nr, nc, generators):
    group = close_group(nr, nc, generators)
    rr = orbit_sets(nr, [p for p, _ in group])
    cc = orbit_sets(nc, [q for _, q in group])
    ri_of = {u: i for i, orbit in enumerate(rr) for u in orbit}
    cj_of = {v: j for j, orbit in enumerate(cc) for v in orbit}
    missing = {(i, j) for i in range(nr) for j in range(nc)}
    edge_orbits = []
    while missing:
        a, b = min(missing)
        o = frozenset((p[a], q[b]) for p, q in group)
        assert o <= missing
        edge_orbits.append(o)
        missing -= o
    eligible = []
    for o in edge_orbits:
        if len({u for u, v in o}) == len(o) == len({v for u, v in o}):
            eligible.append(o)
    eigens = defaultdict(set)
    for o in eligible:
        u, v = next(iter(o))
        ii, jj = ri_of[u], cj_of[v]
        assert {x for x, _ in o} == rr[ii] and {y for _, y in o} == cc[jj]
        eigens[(ii, jj)].add(frozenset(o))
    for i, ri in enumerate(rr):
        for j, cj in enumerate(cc):
            maps = equivariant_bijections(ri, cj, group)
            assert maps == eigens.get((i, j), set()), (label, i, j, maps, eigens.get((i, j)))
    # Check the face criterion by exhaustive independent union-matching tests.
    N = len(eligible)
    assert N <= 14
    face_count = 0
    for bits in range(1 << N):
        selected = [eligible[t] for t in range(N) if bits >> t & 1]
        union = set().union(*selected) if selected else set()
        actual = len({u for u, v in union}) == len(union) == len({v for u, v in union})
        endpoints = []
        for orbit in selected:
            u, v = next(iter(orbit))
            endpoints.append((ri_of[u], cj_of[v]))
        model = (len({i for i, j in endpoints}) == len(endpoints)
                 and len({j for i, j in endpoints}) == len(endpoints))
        assert actual == model, (label, bits)
        face_count += actual
    print(f'{label}: |G|={len(group)}, row_orbits={len(rr)}, column_orbits={len(cc)}, '
          f'eligible_edge_orbits={N}, faces_with_empty={face_count} OK')
    return len(group), N


def pair_flip(n, pairs):
    p = list(range(n))
    for a, b in pairs:
        p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle(n, blocks):
    p = list(range(n))
    for block in blocks:
        for j, value in enumerate(block):
            p[value] = block[(j + 1) % len(block)]
    return tuple(p)


def permutation(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def check_ordinary_retract(n=5, multiplicity=2):
    counts = [0] * (n+1)
    instances = 0
    def recur(row, taken, colored, plain):
        nonlocal instances
        if row == n:
            counts[len(colored)] += 1
            instances += 1
            assert len(plain) == len(set(plain))
            assert len(colored) == len(plain)
            # Forgetting colors then choosing the zero-colored section is a retraction.
            section = {(i, j, 0) for i, j in plain}
            assert all(c == 0 for _, _, c in section)
            assert {(i, j) for i, j, _ in section} == set(plain)
            return
        recur(row + 1, taken, colored, plain)
        for col in range(n):
            if col not in taken:
                for color in range(multiplicity):
                    recur(row+1, taken | {col}, colored+[(row,col,color)], plain+[(row,col)])
    recur(0, set(), [], [])
    expected = [comb(n,k)**2 * factorial(k) * multiplicity**k for k in range(n+1)]
    assert counts == expected, (counts, expected)
    print(f'{n}x{n} board with {multiplicity} parallel edges per square: '
          f'face_counts_by_size={counts}, total={instances}; retraction OK')


def main():
    idr = tuple(range(3)); idc = tuple(range(4))
    check_case('trivial 3x4', 3, 4, [(idr, idc)])
    flip4 = pair_flip(4, [(0,1),(2,3)])
    check_case('C2, two free orbits each shore', 4,4, [(flip4,flip4)])
    flip5 = pair_flip(5, [(0,1),(2,3)])
    check_case('C2, two free plus one fixed on each shore', 5,5, [(flip5,flip5)])
    flipr5 = pair_flip(5, [(0,1),(2,3)])
    flipc4 = pair_flip(4, [(0,1)])
    check_case('C2, mixed orbit multiplicities', 5,4, [(flipr5,flipc4)])
    c3 = cycle(6, [(0,1,2),(3,4,5)])
    check_case('C3, two regular orbits on each shore', 6,6, [(c3,c3)])
    t = pair_flip(6,[(0,1),(3,4)])
    c = cycle(6,[(0,1,2),(3,4,5)])
    check_case('S3, two natural orbits on each shore',6,6,[(t,t),(c,c)])
    # Build the regular left action of S3 without relying on any graph model.
    universe = sorted(permutations(range(3)))
    index = {p:i for i,p in enumerate(universe)}
    tg = (1,0,2)
    cg = (1,2,0)
    def left_regular(g):
        return tuple(index[tuple(g[p[k]] for k in range(3))] for p in universe)
    treg, creg = left_regular(tg), left_regular(cg)
    check_case('S3, one regular orbit on each shore', 6,6, [(treg,treg),(creg,creg)])
    nat_t = (1,0,2)
    nat_c = (1,2,0)
    pt = nat_t + tuple(k+3 for k in treg)
    pc = nat_c + tuple(k+3 for k in creg)
    check_case('S3, natural plus regular orbit on each shore', 9,9,[(pt,pt),(pc,pc)])
    check_ordinary_retract()
    print('ALL_ORBIT_CHESSBOARD_FIXED_CHECKS_PASS')


if __name__ == '__main__':
    main()
