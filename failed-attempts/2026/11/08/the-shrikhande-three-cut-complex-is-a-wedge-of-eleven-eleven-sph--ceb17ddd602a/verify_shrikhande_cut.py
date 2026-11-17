#!/usr/bin/env python3
"""Finite integral homotopy certificate for the Shrikhande ordinary 3-cut complex.

No external packages or data. All faces are represented by bit masks, oriented in
increasing vertex order. The script fully checks a discrete Morse matching and
its signed boundary, independently cross-checking the Alexander dual.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 16
FULL = (1 << N) - 1
STEPS = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}


def shrikhande_adjacency():
    adj = [0] * N
    for a in range(N):
        x, y = divmod(a, 4)
        for b in range(N):
            u, v = divmod(b, 4)
            if ((u - x) % 4, (v - y) % 4) in STEPS:
                adj[a] |= 1 << b
    return adj


def popbits(mask):
    while mask:
        bit = mask & -mask
        mask ^= bit
        yield bit.bit_length() - 1


def is_connected(mask, adj):
    if mask == 0:
        return False
    seen = frontier = mask & -mask
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        u = bit.bit_length() - 1
        found = adj[u] & mask & ~seen
        seen |= found
        frontier |= found
    return seen == mask


def build_complex(adj):
    disconnected = []
    flags = bytearray(1 << N)
    for triple in combinations(range(N), 3):
        m = sum(1 << i for i in triple)
        if not is_connected(m, adj):
            disconnected.append(m)
            flags[m] = 1
    # Upward Boolean zeta transform: flags[T] = 1 iff T contains a bad triple.
    for i in range(N):
        bit = 1 << i
        for m in range(1 << N):
            if m & bit:
                flags[m] |= flags[m ^ bit]
    faces = bytearray(1 << N)
    for s in range(1, 1 << N):
        faces[s] = flags[FULL ^ s]
    assert not faces[0]  # empty face is omitted from the regular face poset
    # Independent direct test of every nonempty face, avoiding the zeta transform.
    for s in range(1, 1 << N):
        complement = FULL ^ s
        direct = any((t & complement) == t for t in disconnected)
        assert bool(faces[s]) == direct, s
    return faces, disconnected


def check_graph(adj):
    assert all(not (adj[i] & (1 << i)) for i in range(N))
    assert all((adj[i] >> j) & 1 == (adj[j] >> i) & 1
               for i in range(N) for j in range(N))
    assert all(x.bit_count() == 6 for x in adj)
    assert all((adj[i] & adj[j]).bit_count() == 2
               for i in range(N) for j in range(i + 1, N))
    triangles = sum(all(adj[i] & (1 << j) for i, j in combinations(t, 2))
                    for t in combinations(range(N), 3))
    assert triangles == 32
    for v in range(N):
        nbr = adj[v]
        assert all((adj[u] & nbr).bit_count() == 2 for u in popbits(nbr))
    return triangles


def dual_counts(adj, faces):
    # The Alexander dual contains S iff V\S is a nonface of the cut complex.
    # Its empty face is implicit; the full 16-set is excluded.
    counts = Counter()
    four_types = Counter()
    for s in range(1, FULL):
        if not faces[FULL ^ s]:
            k = s.bit_count()
            counts[k] += 1
            if k == 4:
                es = sum((adj[i] & s).bit_count() for i in popbits(s)) // 2
                four_types[es] += 1
    assert counts == Counter({1: 16, 2: 120, 3: 176, 4: 60})
    assert four_types == Counter({4: 12, 5: 48})
    return counts, four_types


def morse_matching(faces):
    remaining = bytearray(faces)
    upper_of_lower = {}
    lower_of_upper = {}
    for v in range(N):
        bit = 1 << v
        for s in range(1, 1 << N):
            t = s | bit
            if s != t and remaining[s] and remaining[t]:
                remaining[s] = remaining[t] = 0
                upper_of_lower[s] = t
                lower_of_upper[t] = s
    critical = [s for s in range(1, 1 << N) if remaining[s]]
    cd = Counter(s.bit_count() - 1 for s in critical)
    assert len(upper_of_lower) == 32573
    assert cd == Counter({0: 1, 11: 13, 12: 2})
    return upper_of_lower, lower_of_upper, critical, cd


def check_acyclicity(faces, upper_of_lower, lower_of_upper):
    indegree = [0] * (1 << N)
    incidences = 0
    for t in range(1, 1 << N):
        if not faces[t]:
            continue
        for v in popbits(t):
            s = t ^ (1 << v)
            if not s or not faces[s]:
                continue
            incidences += 1
            if lower_of_upper.get(t) == s:
                indegree[t] += 1  # matched arrow s -> t
            else:
                indegree[s] += 1  # unmatched arrow t -> s
    q = deque(s for s in range(1, 1 << N) if faces[s] and indegree[s] == 0)
    processed = 0
    while q:
        t = q.popleft()
        processed += 1
        # Unmatched down arrows.
        for v in popbits(t):
            s = t ^ (1 << v)
            if s and faces[s] and lower_of_upper.get(t) != s:
                indegree[s] -= 1
                if indegree[s] == 0:
                    q.append(s)
        # One matched up arrow, if present.
        u = upper_of_lower.get(t)
        if u is not None:
            indegree[u] -= 1
            if indegree[u] == 0:
                q.append(u)
    count = sum(faces)
    assert count == 65162
    assert processed == count, (processed, count)
    return count, incidences


def signed_morse_boundary(upper_of_lower, critical):
    low = [s for s in critical if s.bit_count() == 12]
    high = [s for s in critical if s.bit_count() == 13]
    position = {s: i for i, s in enumerate(low)}

    @lru_cache(None)
    def reduced_boundary(t):
        ans = {}
        for v in popbits(t):
            s = t ^ (1 << v)
            sign = -1 if (t & ((1 << v) - 1)).bit_count() % 2 else 1
            if s in position:
                j = position[s]
                ans[j] = ans.get(j, 0) + sign
            elif s in upper_of_lower:
                u = upper_of_lower[s]
                if u == t:
                    continue  # The matched incidence is the eliminated pivot.
                added_bit = u ^ s
                pivot = -1 if (u & (added_bit - 1)).bit_count() % 2 else 1
                for j, coeff in reduced_boundary(u).items():
                    ans[j] = ans.get(j, 0) - sign * pivot * coeff
        return {i: c for i, c in ans.items() if c}

    matrix = [[0] * len(high) for _ in low]
    for column, t in enumerate(high):
        for row, coeff in reduced_boundary(t).items():
            matrix[row][column] = coeff
    assert len(low) == 13 and len(high) == 2
    # Two independent unit pivots prove Smith invariants (1,1): all columns
    # primitive and their 2x2 determinantal divisor equals 1.
    assert matrix == [[-1, 0], [0, 0], [0, -1], [-1, 0],
                      [0, 0], [1, 0], [1, 0], [0, 0],
                      [0, 0], [0, 1], [0, 1], [0, 1], [0, 1]]
    assert matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0] == 1
    return matrix, len(low), len(high), reduced_boundary.cache_info().currsize


def main():
    adj = shrikhande_adjacency()
    triangles = check_graph(adj)
    faces, bad = build_complex(adj)
    assert len(bad) == 384
    counts, types = dual_counts(adj, faces)
    upper, lower, critical, cd = morse_matching(faces)
    nf, incidences = check_acyclicity(faces, upper, lower)
    matrix, a, b, rec = signed_morse_boundary(upper, critical)
    print('graph: vertices=16 edges=48 triangles=', triangles)
    print('disconnected triples=', len(bad), 'dual faces by cardinality=', dict(sorted(counts.items())))
    print('dual tetrahedra by edges=', dict(sorted(types.items())))
    print('cut nonempty faces=', nf, 'Hasse incidences=', incidences)
    print('matching pairs=', len(upper), 'critical by dimension=', dict(sorted(cd.items())))
    print('Morse boundary rows (13 x 2)=', matrix)
    print('Morse matrix Smith invariants=(1,1), remaining 11 degree-11 spheres')
    print('SHRIKHANDE_3CUT_INTEGRAL_VERIFY_OK')


if __name__ == '__main__':
    main()
