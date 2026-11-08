"""Exhaustive proof certificate: two-letter finite transition systems in a binary relational vocabulary.

Run: python3 verify.py. Only Python standard library is needed.
"""
import collections
import itertools
import math


def representatives(n):
    # The complete space has n^(2n) ordered transition-table pairs.
    perms = list(itertools.permutations(range(n)))
    seen = set()
    reps = []
    maps = itertools.product(range(n), repeat=n)
    for f in maps:
        for g in itertools.product(range(n), repeat=n):
            key = (f, g)
            if key in seen:
                continue
            reps.append(key)
            for p in perms:
                a = [0] * n
                b = [0] * n
                for x in range(n):
                    a[p[x]] = p[f[x]]
                    b[p[x]] = p[g[x]]
                seen.add((tuple(a), tuple(b)))
    assert len(seen) == n ** (2 * n)
    return reps


def burnside_count(n):
    # Independently count conjugation orbits of pairs of endomaps.
    total = 0
    for p in itertools.permutations(range(n)):
        seen = set()
        cycles = []
        for x in range(n):
            if x in seen:
                continue
            y, length = x, 0
            while y not in seen:
                seen.add(y)
                y = p[y]
                length += 1
            cycles.append(length)
        # Explicit formula without symbolic cycle-index manipulation.
        choices = 1
        for length in cycles:
            fixed = 0
            for x in range(n):
                y = x
                for _ in range(length):
                    y = p[y]
                fixed += y == x
            choices *= fixed
        total += choices ** 2
    assert total % math.factorial(n) == 0
    return total // math.factorial(n)


def atomic_type(f, g, x, y):
    # Complete atomic 2-type, including equality and both orientations.
    return (x == y, f[x] == y, f[y] == x, g[x] == y, g[y] == x)


def signatures(pairs):
    """Joint C2/counting-refinement color histograms, globally normalized."""
    n = len(pairs[0][0])
    colors = [[0] * n for _ in pairs]
    # n+4 rounds suffice here because full pairwise separation is verified
    # by this cutoff; no unverified general global stabilization is assumed.
    for _ in range(n + 4):
        keys = []
        for (f, g), col in zip(pairs, colors):
            for x in range(n):
                counts = collections.Counter(
                    (atomic_type(f, g, x, y), col[y]) for y in range(n)
                )
                keys.append((col[x], tuple(sorted(counts.items()))))
        ids = {key: i for i, key in enumerate(sorted(set(keys)))}
        nxt = [[ids[k] for k in keys[i*n:(i+1)*n]]
               for i in range(len(pairs))]
        if nxt == colors:
            break
        colors = nxt
    return [tuple(sorted(collections.Counter(c).items())) for c in colors]


def main():
    expected = {1: 1, 2: 10, 3: 129, 4: 2836}
    for n in range(1, 5):
        reps = representatives(n)
        profiles = signatures(reps)
        assert len(reps) == expected[n] == burnside_count(n)
        assert len(set(profiles)) == expected[n]
        print(f'ORDER {n}: isomorphism_types={len(reps)} counting_types={len(set(profiles))} burnside={burnside_count(n)}')

    n = 5
    f = tuple((x+1) % n for x in range(n))
    g2 = tuple((x+2) % n for x in range(n))
    g3 = tuple((x+3) % n for x in range(n))
    assert signatures([(f,g2), (f,g3)])[0] == signatures([(f,g2), (f,g3)])[1]
    assert not any(all(p[f[x]] == f[p[x]] and p[g2[x]] == g3[p[x]] for x in range(n))
                   for p in itertools.permutations(range(n)))
    print('WITNESS: n=5 (shift1,shift2) vs (shift1,shift3), nonisomorphic and C2-equivalent')
    print('VERIFY_OK first_C2_collision=5 types_at_4=2836')

if __name__ == '__main__':
    main()
