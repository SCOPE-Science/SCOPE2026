"""Reconstruct fixed orbit complexes for three-robust clique complexes of cycles.

No external libraries or data are required. Run with Python >= 3.9.
"""
from itertools import combinations
from math import gcd


def admissible(n, subset):
    """The induced cycle subgraph has no independent triple."""
    return not any(
        all((u - v) % n not in (1, n - 1) for u, v in combinations(t, 2))
        for t in combinations(subset, 3)
    )


def orbit_faces(n, perm):
    unseen = set(range(n))
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        v = perm(seed)
        while v not in orbit:
            orbit.add(v)
            v = perm(v)
        assert v == seed, (n, seed, perm)
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    # Any selected set of five or more original vertices for n >= 6
    # contains an independent triple. Short-circuit but independently
    # test actual admissibility for each surviving subset.
    max_orig = n if n <= 5 else 4
    result = {0: set()}
    for k in range(1, min(len(orbits), max_orig) + 1):
        result[k] = set()
        for inds in combinations(range(len(orbits)), k):
            union = set()
            for j in inds:
                union.update(orbits[j])
            if len(union) <= max_orig and admissible(n, union):
                result[k].add(inds)
    return orbits, result


def is_cycle(faces, nvert):
    v = faces.get(1, set())
    e = faces.get(2, set())
    assert v == {(j,) for j in range(nvert)}
    assert len(e) == nvert
    assert all(not faces[k] for k in faces if k >= 3)
    adj = [set() for _ in range(nvert)]
    for i,j in e:
        adj[i].add(j)
        adj[j].add(i)
    assert all(len(a) == 2 for a in adj)
    seen = {0}
    queue = [0]
    for u in queue:
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    assert len(seen) == nvert


def check():
    cases = 0
    ref_circles = 0
    halfturn_circles = 0
    empty_rotations = 0
    small_simplex = 0
    for n in range(3, 36):
        # The canonical generators of the entire dihedral group.
        for a in range(n):
            for kind in ('reflection', 'rotation'):
                if kind == 'rotation' and a == 0:
                    continue
                perm = ((lambda j, a=a: (a - j) % n) if kind == 'reflection'
                        else (lambda j, a=a: (j + a) % n))
                orbits, faces = orbit_faces(n, perm)
                cases += 1
                if n <= 5:
                    assert all(
                        len(faces.get(k, ())) == (len(list(combinations(range(len(orbits)), k))))
                        for k in range(1, len(orbits) + 1)
                    )
                    small_simplex += 1
                    continue
                if kind == 'reflection':
                    expected = ((n + 1) // 2 if n % 2 else (n//2 + 1 if a % 2 == 0 else n//2))
                    assert len(orbits) == expected, (n,a,len(orbits),expected)
                    is_cycle(faces, expected)
                    ref_circles += 1
                elif n % 2 == 0 and a == n//2:
                    assert len(orbits) == n//2
                    is_cycle(faces, n//2)
                    halfturn_circles += 1
                else:
                    assert not any(faces.values()), (n,a,faces)
                    empty_rotations += 1
    print('ALL_DIHEDRAL_GEOMETRIC_FIXED_ORBIT_CHECKS_OK')
    print('cycle_lengths_checked=3..35')
    print('nonidentity_dihedral_actions_checked=', cases)
    print('small_simplex_action_cases=', small_simplex)
    print('reflection_circle_cases=', ref_circles)
    print('halfturn_circle_cases=', halfturn_circles)
    print('empty_rotation_cases=', empty_rotations)


if __name__ == '__main__':
    check()
