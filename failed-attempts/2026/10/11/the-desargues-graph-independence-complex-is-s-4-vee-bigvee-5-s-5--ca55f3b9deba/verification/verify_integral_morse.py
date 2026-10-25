#!/usr/bin/env python3
"""Exact integral discrete Morse certificate for the Desargues independence complex.

Only Python 3 standard library is required. All pairs, directed cover relations,
critical cells and signed boundary coefficients are recomputed, not loaded.
"""
from collections import Counter, deque
from functools import lru_cache

N = 20
ORDER = (9, 2, 5, 17, 19, 3, 18, 6, 10, 11, 12, 4, 8, 16, 1, 15, 7, 13, 14, 0)
CRITICAL = (0x3891, 0x7141, 0x18512, 0x1c089, 0x80c48, 0x8e082)
COUNTS = (1, 20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2)

def lowbits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit

def graph():
    a = [0] * N
    for i in range(10):
        for x, y in ((i, (i + 1) % 10), (10 + i, 10 + (i + 3) % 10), (i, 10 + i)):
            assert x != y
            a[x] |= 1 << y
            a[y] |= 1 << x
    assert len(set(tuple(sorted((u, v))) for u in range(N) for v in range(N) if (a[u] >> v) & 1)) == 30
    assert [z.bit_count() for z in a] == [3] * N
    return a

def enumerate_faces(a):
    result = [0]
    def extend(face, available):
        while available:
            bit = available & -available
            available ^= bit
            v = bit.bit_length() - 1
            nxt = face | bit
            result.append(nxt)
            extend(nxt, available & ~a[v])
    extend(0, (1 << N) - 1)
    return result

def matched_complex(faces):
    active = set(faces)
    paired_up = {}
    allpairs = []
    for vertex in ORDER:
        b = 1 << vertex
        # Staged matching: both faces must remain at this stage.
        lowers = sorted(s for s in active if not s & b and s | b in active)
        for s in lowers:
            t = s | b
            assert s in active and t in active
            paired_up[s] = t
            allpairs.append((s, t))
            active.remove(s)
            active.remove(t)
    return active, paired_up, allpairs

def acyclicity(faces, pairs):
    remaining = {s: 0 for s in faces}
    out = {s: [] for s in faces}
    arcs = 0
    for upper in faces:
        for bit in lowbits(upper):
            lower = upper ^ bit
            if pairs.get(lower) == upper:
                start, end = lower, upper
            else:
                start, end = upper, lower
            out[start].append(end)
            remaining[end] += 1
            arcs += 1
    queue = deque(s for s in faces if remaining[s] == 0)
    topological = 0
    while queue:
        s = queue.popleft()
        topological += 1
        for t in out[s]:
            remaining[t] -= 1
            if remaining[t] == 0:
                queue.append(t)
    assert topological == len(faces), (topological, len(faces))
    return arcs

def incidence(upper, index):
    assert (upper >> index) & 1
    return -1 if (upper & ((1 << index) - 1)).bit_count() % 2 else 1

def integral_morse_boundary(critical, up):
    lowcrit = [s for s in critical if s.bit_count() == 5]
    highcrit = sorted(s for s in critical if s.bit_count() == 6)
    assert len(lowcrit) == 1 and len(highcrit) == 5
    target = lowcrit[0]
    @lru_cache(None)
    def reduced_coordinate(s):
        assert s.bit_count() == 5
        if s in critical:
            return int(s == target)
        # A lower face of a matched dimension-4/dimension-5 pair is
        # eliminated using its matching partner's cellular boundary.
        if s not in up:
            return 0
        t = up[s]
        assert t.bit_count() == 6
        missing = (t ^ s).bit_length() - 1
        denominator = incidence(t, missing)
        total = 0
        for bit in lowbits(t):
            v = bit.bit_length() - 1
            if v != missing:
                total += incidence(t, v) * reduced_coordinate(t ^ bit)
        return -total * denominator   # incidence is always +/- 1
    vals = []
    for t in highcrit:
        d = sum(incidence(t, bit.bit_length()-1) * reduced_coordinate(t ^ bit)
                for bit in lowbits(t))
        vals.append(d)
    assert vals == [0, 0, 0, 0, 0], vals
    return vals, reduced_coordinate.cache_info()

def main():
    assert len(ORDER) == N and sorted(ORDER) == list(range(N))
    adj = graph()
    faces = enumerate_faces(adj)
    assert len(faces) == len(set(faces)) == sum(COUNTS) == 6212
    count = Counter(s.bit_count() for s in faces)
    assert tuple(count[k] for k in range(11)) == COUNTS
    crit, up, pairs = matched_complex(faces)
    assert len(pairs) == 3103
    assert tuple(sorted(crit)) == tuple(sorted(CRITICAL))
    assert len(crit) == 6
    assert len(faces) == 2*len(pairs) + len(crit)
    assert sum(1 for s in crit if s.bit_count() == 5) == 1
    assert sum(1 for s in crit if s.bit_count() == 6) == 5
    arc_count = acyclicity(faces, up)
    assert arc_count == 30380
    matrix, info = integral_morse_boundary(crit, up)
    # Empty face is matched with a vertex. In the ordinary face poset
    # (empty removed), this vertex becomes the sole critical 0-simplex.
    assert 0 in up and up[0].bit_count() == 1
    print('DESARGUES_INTEGRAL_MORSE_OK', 'faces_including_empty=6212',
          'nonempty=6211', 'pairs=3103', 'critical_dimensions=(4,5,5,5,5,5)',
          'incidences=30380', 'morse_boundary=', matrix, 'cache=', info.currsize)

if __name__ == '__main__':
    main()
