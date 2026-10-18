"""Finite checks of the explicit scale-two prism Rips collapse.

This program is a check at the displayed finite sizes, not an infinite proof.
The all-size argument uses the three families of maximal tetrahedra and
nine elementary free-face families documented in RESULT.md.
"""
from itertools import combinations

# A vertex (i,e) represents cycle index i and layer e in {0,1}.
# Each template is (free face, unique coface) in a fixed phase.
PHASES = [
    ([(0,0),(1,0),(2,0)], [(0,0),(1,0),(1,1),(2,0)]),
    ([(0,0),(0,1),(1,0)], [(0,0),(0,1),(1,0),(1,1)]),
    ([(0,0),(0,1),(-1,1)], [(0,0),(0,1),(1,1),(-1,1)]),
    ([(0,0),(2,0)], [(0,0),(1,1),(2,0)]),
    ([(0,0),(-1,1)], [(0,0),(1,1),(-1,1)]),
    ([(0,1),(2,1)], [(0,1),(1,1),(2,1)]),
    ([(0,1),(1,1)], [(0,0),(0,1),(1,1)]),
    ([(0,0),(0,1)], [(0,0),(0,1),(-1,0)]),
    ([(0,1)], [(0,1),(-1,0)]),
]


def canon(items):
    return tuple(sorted(items))


def translated(face, shift, n):
    return canon(((i + shift) % n, e) for i, e in face)


def distance(u, v, n):
    d = abs(u[0] - v[0])
    return min(d, n-d) + (u[1] != v[1])


def is_clique(s, n):
    return all(distance(u, v, n) <= 2 for u, v in combinations(s, 2))


def facelist(n):
    verts = [(i, e) for i in range(n) for e in (0, 1)]
    # Derive all 4-cliques from the metric, independently of PHASES.
    four = set()
    for s in combinations(verts, 4):
        if is_clique(s, n):
            four.add(canon(s))
    predicted = set()
    for i in range(n):
        predicted.add(translated([(0,0),(1,0),(2,0),(1,1)],i,n))
        predicted.add(translated([(0,1),(1,1),(2,1),(1,0)],i,n))
        predicted.add(translated([(0,0),(0,1),(1,0),(1,1)],i,n))
    assert four == predicted, (n, 'tetrahedron classification')
    for s in four:
        for v in verts:
            if v not in s:
                assert not is_clique(s + (v,), n), (n, '5-clique')
    for k in (1, 2, 3):
        for s in combinations(verts, k):
            if is_clique(s, n):
                assert any(set(s).issubset(t) for t in four), (n, 'small facet')
    faces = set()
    for t in four:
        for k in (1, 2, 3, 4):
            faces.update(combinations(t, k))
    return faces


def verify(n):
    assert n >= 7
    faces = facelist(n)
    assert [sum(len(s)==k for s in faces) for k in (1,2,3,4)] == [2*n,7*n,8*n,3*n]
    rim = {((i,0),) for i in range(n)}
    rim |= {canon(((i,0),((i+1)%n,0))) for i in range(n)}
    for stage, (f, t) in enumerate(PHASES, 1):
        # At the start of each phase all n translated faces must be free.
        cof = {}
        for s in faces:
            if len(s) <= 1:
                continue
            for j in range(len(s)):
                lower = s[:j] + s[j+1:]
                if lower:
                    cof.setdefault(lower, []).append(s)
        orbit = set()
        for i in range(n):
            low, high = translated(f, i, n), translated(t, i, n)
            assert low not in rim and high not in rim, (n, stage, 'rim altered')
            assert low in faces and high in faces, (n, stage, 'missing pair')
            assert cof.get(low) == [high], (n, stage, i, 'not free')
            assert low not in orbit and high not in orbit, (n, stage, 'duplicate')
            orbit.update((low, high))
        assert len(orbit) == 2*n
        faces.difference_update(orbit)
    assert faces == rim, (n, 'incorrect remainder')
    return n, 9*n


if __name__ == '__main__':
    for n in range(7, 21):
        x, pairs = verify(n)
        print('n=%s elementary_pairs=%s PASS' % (x, pairs))
    print('VERIFY_OK')
