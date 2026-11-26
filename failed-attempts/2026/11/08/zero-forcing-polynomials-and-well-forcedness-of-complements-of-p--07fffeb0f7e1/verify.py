"""Independent exhaustive zero-forcing checker for path/cycle complements.

Run: python verify.py . Requires only Python 3 standard library.
"""
from collections import Counter
from math import comb


def complement_adjacency(n, cyclic):
    original = [set() for _ in range(n)]
    for i in range(n - 1):
        original[i].add(i + 1)
        original[i + 1].add(i)
    if cyclic:
        original[0].add(n - 1)
        original[n - 1].add(0)
    return [set(range(n)) - {i} - original[i] for i in range(n)]


def forces_everything(adjacency, initially_blue):
    n = len(adjacency)
    blue = {i for i in range(n) if initially_blue & (1 << i)}
    while len(blue) < n:
        new_blue = None
        for i in sorted(blue):
            whites_seen = adjacency[i] - blue
            if len(whites_seen) == 1:
                new_blue = next(iter(whites_seen))
                break
        if new_blue is None:
            return False
        blue.add(new_blue)
    return True


def expected_minimum_count(n, cyclic):
    return n * (n - 4) + (2 if n == 6 else 0) if cyclic else (n - 3) ** 2 + 1


def test_profile(n, cyclic):
    g = complement_adjacency(n, cyclic)
    zf = [forces_everything(g, mask) for mask in range(1 << n)]
    counts = Counter(mask.bit_count() for mask, success in enumerate(zf) if success)
    a = expected_minimum_count(n, cyclic)
    predicted = {n - 3: a, n - 2: comb(n, 2), n - 1: n, n: 1}
    assert dict(counts) == predicted, (n, cyclic, counts, predicted)
    minimal = [mask for mask, success in enumerate(zf) if success and
               all(not zf[mask & ~(1 << i)] for i in range(n) if mask & (1 << i))]
    assert len(minimal) == a
    assert all(x.bit_count() == n - 3 for x in minimal)
    # Characterization: the white triple contains both neighbors of a blue
    # degree-two vertex in the original path or cycle.
    for mask, success in enumerate(zf):
        whites = set(range(n)) - {i for i in range(n) if mask & (1 << i)}
        if len(whites) != 3:
            continue
        candidate_centers = range(n) if cyclic else range(1, n - 1)
        witness = any(i not in whites and
                      {(i - 1) % n, (i + 1) % n} <= whites
                      for i in candidate_centers)
        assert success == witness, (n, cyclic, mask)
    return (n, 'cycle' if cyclic else 'path', sum(counts.values()), a)


def main():
    results = [test_profile(n, cyclic)
               for n in range(5, 13) for cyclic in (False, True)]
    for n, kind, total, minimum in results:
        print('PROFILE_OK', kind, n, 'total', total, 'minimum', minimum)
    print('VERIFY_OK', 'profiles', len(results), 'literal_subsets',
          sum(2 ** n for n in range(5, 13)) * 2,
          'full_zero_forcing_polynomial=PASS',
          'minimum_set_classification=PASS',
          'well_forcedness=PASS', 'exceptional_six_cycle=PASS')


if __name__ == '__main__':
    main()
