#!/usr/bin/env python3
"""Direct finite tests for higher-independence complexes of subdivided stars.

Requires only Python 3 standard library. Proof for arbitrary parameters is in RESULT.md.
"""
from collections import defaultdict
from itertools import permutations
from math import comb


def faces(k, r):
    """Enumerate induced-component-bounded subsets without using theorem formulas."""
    n = 2 * k + 1
    adj = [0] * n
    for i in range(k):
        a, b = 1 + i, 1 + k + i
        adj[0] |= 1 << a
        adj[a] |= (1 << 0) | (1 << b)
        adj[b] |= 1 << a
    out = defaultdict(list)
    for subset in range(1 << n):
        seen = 0
        valid = True
        for i in range(n):
            if not (subset & (1 << i)) or (seen & (1 << i)):
                continue
            seen |= 1 << i
            queue = [i]
            for u in queue:
                rem = (adj[u] & subset) & ~seen
                while rem:
                    bit = rem & -rem
                    rem -= bit
                    seen |= bit
                    queue.append(bit.bit_length() - 1)
            if len(queue) > r:
                valid = False
                break
        if valid:
            out[subset.bit_count() - 1].append(subset)
    return out


def f2rank(vectors):
    pivots = {}
    for x in vectors:
        while x:
            j = x.bit_length() - 1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    return len(pivots)


def homology_mod_two(by_dim):
    ranks = {}
    counts = {q: len(rows) for q, rows in by_dim.items()}
    for d in range(0, max(counts) + 1):
        low = {simplex: j for j, simplex in enumerate(by_dim[d - 1])}
        cols = []
        for simplex in by_dim[d]:
            residue = simplex
            boundary = 0
            while residue:
                bit = residue & -residue
                residue -= bit
                boundary ^= 1 << low[simplex ^ bit]
            cols.append(boundary)
        ranks[d] = f2rank(cols)
    return {d: count - ranks.get(d, 0) - ranks.get(d + 1, 0)
            for d, count in counts.items() if d >= 0 and count - ranks.get(d, 0) - ranks.get(d + 1, 0)}


def permutation_sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def exterior_augmentation_trace(p, h):
    """Coefficient of t^h in det(1+t P)/(1+t)."""
    k = len(p)
    cycles = []
    seen = set()
    for i in range(k):
        if i in seen:
            continue
        u = i
        length = 0
        while u not in seen:
            seen.add(u)
            length += 1
            u = p[u]
        cycles.append(length)
    coefficients = [1]
    for length in cycles:
        next_poly = [0] * (len(coefficients) + length)
        for i, value in enumerate(coefficients):
            next_poly[i] += value
            next_poly[i + length] += value * ((-1) ** (length - 1))
        coefficients = next_poly
    quotient = []
    for value in coefficients[:-1]:
        quotient.append(value - (quotient[-1] if quotient else 0))
    return quotient[h]


def reduced_lefschetz(by_dim, k, p):
    perm = [0] + [1 + p[i] for i in range(k)] + [1 + k + p[i] for i in range(k)]
    result = 0
    for d, simplices in by_dim.items():
        for simplex in simplices:
            ids = [i for i in range(2 * k + 1) if simplex & (1 << i)]
            image = [perm[i] for i in ids]
            if {i for i in ids} != {i for i in image}:
                continue
            orientation = (-1) ** sum(image[a] > image[b]
                                      for a in range(len(image))
                                      for b in range(a + 1, len(image)))
            result += ((-1) ** d) * orientation
    return result


def check_matching(k, r):
    """Check the face-pair matching on the hub link, including acyclicity."""
    n = 2 * k
    faces_link = []
    for s in range(1 << n):
        W = s & ((1 << k) - 1)
        Z = (s >> k) & ((1 << k) - 1)
        if 1 + W.bit_count() + (W & Z).bit_count() <= r:
            faces_link.append(s)
    face_set = set(faces_link)
    matched = {}
    all_W = (1 << k) - 1
    h = r - k - 1
    for s in faces_link:
        W = s & all_W
        Z = s >> k
        if W != all_W:
            missing = next(i for i in range(k) if not (W & (1 << i)))
            bit = 1 << (k + missing)
            paired = s ^ bit
            if paired not in face_set:
                raise AssertionError('invalid link matching')
            matched[s] = paired
        elif h >= 0:
            if (Z & 1) or Z.bit_count() < h:
                paired = s ^ (1 << k)
                if paired not in face_set:
                    raise AssertionError('invalid full-hub matching')
                matched[s] = paired
    for s, t in matched.items():
        assert matched.get(t) == s
    # Directed Hasse edges: ordinary downward arrows, reversed on matched edges.
    arcs = {s: [] for s in face_set}
    indeg = {s: 0 for s in face_set}
    for s in face_set:
        bits = s
        while bits:
            bit = bits & -bits
            bits -= bit
            t = s ^ bit
            if matched.get(s) == t:
                a, b = t, s
            else:
                a, b = s, t
            arcs[a].append(b)
            indeg[b] += 1
    stack = [s for s, degree in indeg.items() if degree == 0]
    count = 0
    while stack:
        s = stack.pop()
        count += 1
        for t in arcs[s]:
            indeg[t] -= 1
            if indeg[t] == 0:
                stack.append(t)
    assert count == len(face_set), 'acyclicity failure'
    critical = [s for s in face_set if s not in matched]
    if 2 <= r <= k or r >= 2 * k + 1:
        expected = 0
    else:
        expected = comb(k - 1, h)
    assert len(critical) == expected, (k, r, len(critical), expected)
    return len(face_set)


def main():
    total_faces = total_lef = total_links = tests = 0
    for k in range(2, 6):
        for r in range(1, 2 * k + 2):
            d = faces(k, r)
            got = homology_mod_two(d)
            if r == 1:
                predicted = {k - 1: 1}
            elif k + 1 <= r <= 2 * k:
                predicted = {r - 1: comb(k - 1, r - k - 1)}
            else:
                predicted = {}
            assert got == predicted, (k, r, got, predicted)
            tests += 1
            total_faces += sum(len(v) for v in d.values()) - 1
            if r >= 2:
                total_links += check_matching(k, r)
            for p in permutations(range(k)):
                trace = reduced_lefschetz(d, k, p)
                if r == 1:
                    top_trace = permutation_sign(p)
                elif k + 1 <= r <= 2 * k:
                    top_trace = permutation_sign(p) * exterior_augmentation_trace(p, r - k - 1)
                else:
                    top_trace = 0
                predicted_lef = ((-1) ** (r - 1 if r != 1 else k - 1)) * top_trace
                assert trace == predicted_lef, (k, r, p, trace, predicted_lef)
                total_lef += 1
    print('ALL_VERIFY_OK cases=%d simplices=%d signed_lefschetz=%d link_faces=%d' %
          (tests, total_faces, total_lef, total_links))


if __name__ == '__main__':
    main()
