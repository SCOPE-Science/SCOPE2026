#!/usr/bin/env python3
"""Exact finite checks for four total four-cut complexes of Möbius ladders.
Only Python standard library. Execute: python3 verify.py
"""
from itertools import combinations
from collections import Counter, defaultdict, deque
import hashlib

EXPECTED = {
    6: (48, (12, 66, 220, 495, 780, 648, 276, 48), 30, 4),
    7: (154, (14, 91, 364, 1001, 2002, 3003, 3432, 2450, 952, 154), 64, 6),
    8: (384, (16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 7040, 2512, 384), 93, 8),
    9: (810, (18, 153, 816, 3060, 8568, 18564, 31824, 43758, 48620, 43758, 31824, 17016, 5580, 810), 130, 10),
}

def construct(n):
    """Enumerate ALL independent four-sets; a face lies in a complement facet."""
    N = 2 * n
    adj = [0] * N
    for v in range(N):
        for w in ((v - 1) % N, (v + 1) % N, (v + n) % N):
            adj[v] |= 1 << w
    independent = []
    for C in combinations(range(N), 4):
        if all(not (adj[a] & (1 << b)) for a, b in combinations(C, 2)):
            independent.append(sum(1 << v for v in C))
    full = (1 << N) - 1
    faces = {0}
    for I in independent:
        facet = full ^ I
        s = facet
        while s:
            faces.add(s)
            s = (s - 1) & facet
    return independent, faces

def field_homology(faces):
    """Reduced simplicial boundary ranks over F2, computed independently of matching."""
    bysize = defaultdict(list)
    for s in faces:
        bysize[s.bit_count()].append(s)
    for a in bysize.values():
        a.sort()
    ranks = {}
    for size in range(1, max(bysize) + 1):
        positions = {s: j for j, s in enumerate(bysize[size - 1])}
        pivots = {}
        for s in bysize[size]:
            v = 0
            bits = s
            while bits:
                e = bits & -bits
                bits -= e
                v ^= (1 << positions[s ^ e])
            while v:
                j = v.bit_length() - 1
                old = pivots.get(j)
                if old is None:
                    pivots[j] = v
                    break
                v ^= old
        ranks[size] = len(pivots)
    # Empty face at size zero gives augmented/reduced H0.
    return {d:len(bysize[d+1])-ranks.get(d+1, 0)-ranks.get(d+2, 0)
            for d in range(max(bysize))}

def matching(faces, N):
    """Greedy vertex-toggle matching: process vertices 0..N-1, never reuse a face."""
    available = set(faces) - {0}
    pairs = []
    for v in range(N):
        bit = 1 << v
        # Deterministic ordering; each step uses only still-unpaired faces.
        for s in sorted(available, key=lambda x: (-x.bit_count(), x)):
            if s not in available or (s & bit):
                continue
            t = s | bit
            if t in available:
                pairs.append((s, t))
                available.remove(s)
                available.remove(t)
    return pairs, available

def acyclic(faces, pairs):
    """Directed Hasse graph: ordinary incidences downward, matched ones upward.
    Kahn's exact integer topological sort visits EVERY nonempty face iff acyclic.
    """
    nonempty = set(faces) - {0}
    matched = set(pairs)
    assert len(matched) == len(pairs)
    indegree = {f: 0 for f in nonempty}
    outgoing = defaultdict(list)
    incidences = 0
    for high in nonempty:
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            low = high ^ bit
            if low == 0:
                continue
            incidences += 1
            if (low, high) in matched:
                src, dst = low, high
            else:
                src, dst = high, low
            outgoing[src].append(dst)
            indegree[dst] += 1
    q = deque(v for v, deg in indegree.items() if deg == 0)
    visited = 0
    while q:
        x = q.popleft()
        visited += 1
        for y in outgoing[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert visited == len(nonempty), ("CYCLE", visited, len(nonempty))
    return incidences

def main():
    for n, (facets_expected, f_expected, spheres, dim) in EXPECTED.items():
        indep, faces = construct(n)
        fvec = tuple(sum(s.bit_count() == d + 1 for s in faces) for d in range(2*n - 4))
        assert len(indep) == facets_expected
        assert fvec == f_expected, (n, fvec)
        pairs, critical = matching(faces, 2*n)
        assert set(x for p in pairs for x in p).isdisjoint(critical)
        assert 2*len(pairs)+len(critical)==len(faces)-1
        critvec = Counter(c.bit_count()-1 for c in critical)
        assert critvec == {0: 1, dim:spheres}, (n, critvec)
        inc = acyclic(faces, pairs)
        betti = field_homology(faces)
        assert betti == {d:(spheres if d == dim else 0) for d in range(2*n - 4)}, (n,betti)
        fingerprint = hashlib.sha256(
            ''.join(f'{a},{b}\n' for a,b in pairs).encode('ascii')
        ).hexdigest()[:16]
        print(f'n={n} indep4={len(indep)} faces={len(faces)-1} '
              f'hasse={inc} pairs={len(pairs)} critical={dict(sorted(critvec.items()))} '
              f'F2=OK DAG=OK matching_sha16={fingerprint}')
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
