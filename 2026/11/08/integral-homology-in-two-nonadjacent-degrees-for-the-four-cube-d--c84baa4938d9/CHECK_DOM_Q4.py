#!/usr/bin/env python3
"""Independent finite arithmetic checks for a four-cube dominance-complex calculation.

Python 3, standard library only. Every asserted numerical quantity is recomputed.
The matching is a face-poset matching, not a claim of simplicial collapsibility.
"""
from collections import Counter, deque


def closed_neighborhoods(d):
    n = 1 << d
    return [sum(1 << u for u in range(n) if u == v or (u ^ v).bit_count() == 1)
            for v in range(n)]


def all_faces(d):
    """Independent equivalent definitions, tested for every one of 2^(2^d) subsets."""
    n = 1 << d
    N = closed_neighborhoods(d)
    all_mask = (1 << n) - 1
    a, b = set(), set()
    dominating = []
    for s in range(1 << n):
        # Face means none of the closed neighborhoods is wholly in s.
        is_face_a = all((s & nv) != nv for nv in N)
        # Complement must meet each closed neighborhood.
        comp = all_mask ^ s
        is_face_b = all((comp & nv) != 0 for nv in N)
        assert is_face_a == is_face_b, (d, s)
        if is_face_a and s:
            a.add(s)
        if is_face_b and s:
            b.add(s)
        if is_face_a:
            # Direct domination via closed-neighborhood union; includes s=0.
            cover = 0
            selected = comp
            while selected:
                bit = selected & -selected
                selected -= bit
                cover |= N[bit.bit_length() - 1]
            assert cover == all_mask
        if all((s & nv) for nv in N):
            dominating.append(s)
    assert a == b
    # Sum over dominating sets, independently checking the reduced Euler characteristic.
    euler_by_dom = sum(1 if s.bit_count() % 2 == 0 else -1 for s in dominating)
    euler_by_faces = -sum(1 if s.bit_count() % 2 == 0 else -1 for s in (a | {0}))
    assert euler_by_dom == -euler_by_faces, (euler_by_dom, euler_by_faces)
    return a, dominating, euler_by_faces


def staged_toggle_matching(faces, d, order):
    n = 1 << d
    assert sorted(order) == list(range(n))
    unmatched = set(faces)
    lower_to_upper = {}
    for v in order:
        b = 1 << v
        # Stage-specific matching uses exactly the faces remaining at this stage.
        lower = [s for s in unmatched if not (s & b) and (s | b) in unmatched]
        for s in lower:
            assert s in unmatched and (s | b) in unmatched
            assert (s | b).bit_count() == s.bit_count() + 1
            lower_to_upper[s] = s | b
        for s in lower:
            unmatched.remove(s)
            unmatched.remove(s | b)
    covered = set(lower_to_upper) | set(lower_to_upper.values())
    assert len(covered) == 2 * len(lower_to_upper)
    assert covered.isdisjoint(unmatched)
    assert covered | unmatched == faces
    return lower_to_upper, unmatched


def verify_acyclicity(faces, matching):
    """Construct and topologically sort the ENTIRE directed Hasse diagram."""
    indegree = {s: 0 for s in faces}
    adj = {s: [] for s in faces}
    edges = 0
    for hi in faces:
        bits = hi
        while bits:
            bit = bits & -bits
            bits -= bit
            lo = hi ^ bit
            if lo not in faces:
                continue
            if matching.get(lo) == hi:
                src, dst = lo, hi
            else:
                src, dst = hi, lo
            adj[src].append(dst)
            indegree[dst] += 1
            edges += 1
    q = deque(s for s in faces if indegree[s] == 0)
    seen = 0
    while q:
        s = q.popleft()
        seen += 1
        for dst in adj[s]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                q.append(dst)
    assert seen == len(faces), (seen, len(faces))
    return edges


def run_dimension(d):
    faces, dominating, reduced_euler = all_faces(d)
    n = 1 << d
    primary = list(range(n))
    if d == 4:
        secondary = [2, 3, 10, 4, 15, 12, 9, 8, 5, 11, 14, 7, 1, 0, 13, 6]
    else:
        secondary = list(range(n - 1, -1, -1))
    p, c = staged_toggle_matching(faces, d, primary)
    p2, c2 = staged_toggle_matching(faces, d, secondary)
    edges = verify_acyclicity(faces, p)
    edges2 = verify_acyclicity(faces, p2)
    assert edges == edges2
    dims = dict(sorted(Counter(s.bit_count() - 1 for s in c).items()))
    dims2 = dict(sorted(Counter(s.bit_count() - 1 for s in c2).items()))
    fvec = dict(sorted(Counter(s.bit_count() - 1 for s in faces).items()))
    critical_euler = sum(((-1)**dim) * mult for dim,mult in dims.items())
    assert reduced_euler == critical_euler - 1
    print('DIMENSION', d)
    print('FACE_COUNT', len(faces))
    print('FACE_VECTOR', fvec)
    print('HASSE_COVERS', edges)
    print('MATCHED_PAIRS', len(p))
    print('CRITICAL', dims)
    print('SECOND_MATCHED_PAIRS', len(p2))
    print('SECOND_CRITICAL', dims2)
    print('REDUCED_EULER', reduced_euler)
    if d == 4:
        assert len(faces) == 45706
        assert edges == 329552
        assert len(p) == 22847
        assert dims == {0: 1, 7: 10, 9: 1}
        assert dims2 == dims
        assert reduced_euler == -11
        assert len(dominating) == 45707
        assert min(x.bit_count() for x in dominating) == 4
        facets = [s for s in faces if all(
            (s & (1 << v)) or (s | (1 << v)) not in faces for v in range(n))]
        facet_dimensions = dict(sorted(Counter(s.bit_count() - 1 for s in facets).items()))
        assert facet_dimensions == {7: 10, 10: 80, 11: 40}
        print('DOMINATION_NUMBER', 4)
        print('FACET_DIMENSIONS', facet_dimensions)
        print('INTEGRAL_REDUCED_HOMOLOGY', {7: 10, 9: 1})
    elif d == 3:
        assert len(faces) == 182 and dims == {0: 1, 3: 7}
    elif d == 2:
        assert len(faces) == 10 and dims == {0: 1, 1: 3}
    elif d == 1:
        assert len(faces) == 2 and dims == {0: 2}


if __name__ == '__main__':
    for dimension in (1, 2, 3, 4):
        run_dimension(dimension)
    print('FOUR_CUBE_DOMINANCE_EXHAUSTIVE_CHECK_PASS')
