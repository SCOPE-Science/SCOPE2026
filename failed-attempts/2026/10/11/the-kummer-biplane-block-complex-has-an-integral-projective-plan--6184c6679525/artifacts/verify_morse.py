#!/usr/bin/env python3
"""Exact discrete-Morse certificate for the block complex of the 16_6 biplane.

Uses only Python's standard library. The construction begins with two distinct
16-vertex graphs and proves their open-neighborhood complexes agree by an
explicit incidence-system isomorphism. All faces, Hasse incidences, gradients
and integral Morse differentials are computed anew.
"""
from collections import Counter
from functools import lru_cache

N = 16
POINT_MAP = (0, 8, 2, 10, 7, 3, 5, 1, 14, 6, 12, 4, 9, 13, 11, 15)
BLOCK_MAP = (11, 1, 9, 3, 2, 4, 0, 6, 5, 15, 7, 13, 12, 10, 14, 8)


def neighborhoods(graph):
    cells = [(a, b) for a in range(4) for b in range(4)]
    shifts = {(1,0), (3,0), (0,1), (0,3), (1,1), (3,3)}
    ans = []
    for x, y in cells:
        if graph == "rook":
            row = {4*u+v for u, v in cells if (u == x or v == y) and (u, v) != (x, y)}
        else:
            row = {4*u+v for u, v in cells if ((u-x) % 4, (v-y) % 4) in shifts}
        assert len(row) == 6
        ans.append(row)
    return ans


def all_faces(blocks):
    F = set()
    for B in blocks:
        bits = [1 << i for i in sorted(B)]
        for sub in range(1, 64):
            mask = 0
            for i, bit in enumerate(bits):
                if sub & (1 << i):
                    mask |= bit
            F.add(mask)
    return F


def incidence(higher, lower):
    assert (higher & lower) == lower and higher.bit_count() == lower.bit_count() + 1
    extra = higher ^ lower
    assert extra.bit_count() == 1
    return (-1 if (higher & (extra-1)).bit_count() % 2 else 1)


def matching(faces):
    remaining = set(faces)
    pairs = []
    for v in range(N):
        bit = 1 << v
        for lo in sorted(remaining):
            hi = lo | bit
            if lo & bit == 0 and hi in remaining:
                remaining.remove(lo)
                remaining.remove(hi)
                pairs.append((lo, hi))
    return pairs, remaining


def verify_directed_hasse(faces, pairs):
    paired = set(pairs)
    successors = {s: [] for s in faces}
    indeg = {s: 0 for s in faces}
    count = 0
    for hi in faces:
        if hi.bit_count() == 1:
            continue
        for vertex in range(N):
            if not (hi & (1 << vertex)):
                continue
            lo = hi ^ (1 << vertex)
            if (lo, hi) in paired:
                a, b = lo, hi
            else:
                a, b = hi, lo
            successors[a].append(b)
            indeg[b] += 1
            count += 1
    assert count == 2736, count
    queue = [s for s in faces if indeg[s] == 0]
    pos = 0
    while pos < len(queue):
        s = queue[pos]
        pos += 1
        for nxt in successors[s]:
            indeg[nxt] -= 1
            if not indeg[nxt]:
                queue.append(nxt)
    assert pos == len(faces) == 808, (pos, len(faces))
    return count


def morse_degrees(faces, pairs, critical):
    upwards = {lo: hi for lo, hi in pairs}
    upper_ones = {hi for lo, hi in pairs}
    critical_one = [c for c in critical if c.bit_count() == 2]
    critical_two = [c for c in critical if c.bit_count() == 3]
    assert len(critical_one) == 1 and len(critical_two) == 56
    target = critical_one[0]

    @lru_cache(maxsize=None)
    def projected_boundary(edge):
        """Signed projection of a 1-simplex to critical 1-cells along gradient paths."""
        assert edge.bit_count() == 2
        if edge in critical:
            return 1 if edge == target else 0
        if edge in upper_ones:
            return 0
        assert edge in upwards
        tri = upwards[edge]
        total = 0
        for vert in range(N):
            if tri & (1 << vert):
                other = tri ^ (1 << vert)
                if other != edge:
                    total += incidence(tri, other) * projected_boundary(other)
        return -incidence(tri, edge) * total

    degrees = {}
    for tri in critical_two:
        coef = 0
        for vert in range(N):
            if tri & (1 << vert):
                edge = tri ^ (1 << vert)
                coef += incidence(tri, edge) * projected_boundary(edge)
        degrees[tri] = coef
    return critical_one[0], degrees


def verify_graph(name):
    B = neighborhoods(name)
    assert all(i not in B[i] for i in range(N))
    assert all((i in B[j]) == (j in B[i]) for i in range(N) for j in range(N))
    assert all(len(B[i] & B[j]) == 2 for i in range(N) for j in range(i + 1, N))
    F = all_faces(B)
    vector = tuple(sum(f.bit_count() == i for f in F) for i in range(1, 7))
    assert vector == (16, 120, 320, 240, 96, 16), vector
    pairs, critical = matching(F)
    assert len(pairs) == 375 and len(critical) == 58
    assert Counter(c.bit_count()-1 for c in critical) == Counter({0: 1, 1: 1, 2: 56})
    arcs = verify_directed_hasse(F, pairs)
    crit_one, degrees = morse_degrees(F, pairs, critical)
    assert arcs == 2736
    assert set(degrees.values()) <= {-2, 0, 2}
    assert Counter(degrees.values()) == (
        Counter({0:39, 2:13, -2:4}) if name == 'shrikhande'
        else Counter({0:38, 2:9, -2:9})
    ), Counter(degrees.values())
    import math
    from functools import reduce
    assert reduce(math.gcd, (abs(v) for v in degrees.values()), 0) == 2
    print(f"{name}: faces={len(F)} face_vector={vector} matched_pairs={len(pairs)} "
          f"hasse_arcs={arcs} critical=(1,1,56) critical_one={crit_one} "
          f"boundary_coefficients={dict(sorted(Counter(degrees.values()).items()))} gcd=2")
    return B, F


def main():
    S, SF = verify_graph('shrikhande')
    R, RF = verify_graph('rook')
    assert sorted(POINT_MAP) == sorted(BLOCK_MAP) == list(range(16))
    for center, block in enumerate(S):
        assert {POINT_MAP[v] for v in block} == R[BLOCK_MAP[center]]
    assert {sum(1 << POINT_MAP[v] for v in range(16) if face & (1 << v))
            for face in SF} == RF
    print('point_block_isomorphism=verified_all_sixteen_blocks')
    print('HOMOTOPY=RP2_wedge_55_S2')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
