#!/usr/bin/env python3
"""Independent labeled enumeration of commuting idempotent pairs through six points."""
from itertools import product, permutations

EXPECTED_LABELED = (1, 7, 58, 601, 7616, 113989)
EXPECTED_ORBITS = (1, 4, 12, 37, 105)


def canonical_pair(f, g, perms):
    n = len(f)
    # Relabel old vertex i as pi[i]. An isomorphism acts on both maps.
    best = None
    for pi in perms:
        inv = [0] * n
        for old, new in enumerate(pi):
            inv[new] = old
        key = (tuple(pi[f[inv[j]]] for j in range(n)),
               tuple(pi[g[inv[j]]] for j in range(n)))
        if best is None or key < best:
            best = key
    return best


def main():
    for n in range(1, 7):
        idempotents = [a for a in product(range(n), repeat=n)
                       if all(a[a[i]] == a[i] for i in range(n))]
        labeled = 0
        orbit_reps = set()
        perms = list(permutations(range(n))) if n <= 5 else None
        for f in idempotents:
            for g in idempotents:
                if any(f[g[i]] != g[f[i]] for i in range(n)):
                    continue
                labeled += 1
                if perms is not None:
                    orbit_reps.add(canonical_pair(f, g, perms))
        assert labeled == EXPECTED_LABELED[n - 1]
        if perms is not None:
            assert len(orbit_reps) == EXPECTED_ORBITS[n - 1]
        print(f'LABELED_BRUTE {n}: labeled={labeled} '
              + (f'isomorphism_types={len(orbit_reps)}' if perms else
                 'isomorphism_types=not_tested'))
    print('BRUTE_OK')


if __name__ == '__main__':
    main()
