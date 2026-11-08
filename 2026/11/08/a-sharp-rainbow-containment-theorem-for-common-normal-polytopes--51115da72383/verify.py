"""Finite independent checks for common-normal colorful containment.

Run with Python 3.9+: python verify.py
These checks are diagnostics, not substitutes for the general proof.
"""
import itertools
import random


def matching_witness(matrix):
    m = len(matrix)
    assert all(len(row) == m for row in matrix)
    # Maps constraint j to its assigned color.
    assignment = max(
        itertools.permutations(range(m)),
        key=lambda p: sum(matrix[p[j]][j] for j in range(m)),
    )
    sinks = [
        i for i in range(m)
        if all(matrix[i][j] <= matrix[assignment[j]][j] for j in range(m))
    ]
    assert sinks, 'Every maximum matching must have a sink color'
    return assignment, sinks[0]


def run():
    checks = 0
    rng = random.Random(271828)
    # Matrix-only proof premise: exhaustive small alphabet and randomized larger tests.
    for entries in itertools.product((-1, 0, 1), repeat=4):
        a = [entries[:2], entries[2:]]
        matching_witness(a)
        checks += 1
    for m, rounds in [(2, 500), (3, 500), (4, 400), (5, 150), (6, 100)]:
        for _ in range(rounds):
            M = [[rng.randint(-10, 10) for j in range(m)] for i in range(m)]
            assignment, winner = matching_witness(M)
            assert all(M[assignment[j]][j] >= M[winner][j] for j in range(m))
            checks += 1
    # Actual axis-aligned boxes: each color has between one and four nonempty boxes.
    # Constraint coordinate order is upper x_1, lower x_1, ..., upper x_d, lower x_d.
    for d in (1, 2, 3):
        m = 2 * d
        for _ in range(250):
            families = []
            for i in range(m):
                fam = []
                for _ in range(rng.randint(1, 4)):
                    bounds = []
                    for j in range(d):
                        lo = rng.randint(-8, 8)
                        hi = lo + rng.randint(0, 12)
                        bounds.extend([hi, -lo])
                    fam.append(tuple(bounds))
                families.append(fam)
            severity = [[max(-b[j] for b in family) for j in range(m)]
                        for family in families]
            assignment, winner = matching_witness(severity)
            selected = []
            for j, i in enumerate(assignment):
                selected.append(min(families[i], key=lambda b: b[j]))
            rainbow_caps = [min(b[j] for b in selected) for j in range(m)]
            monochrome_caps = [min(b[j] for b in families[winner])
                               for j in range(m)]
            assert all(r <= q for r, q in zip(rainbow_caps, monochrome_caps))
            checks += 1
    # Sharpness: for 2d-1 colors, every chosen facet-relaxation misses some
    # essential facet of a small box. Checking every choice for small dimensions.
    for d in (1, 2, 3):
        m = 2 * d
        base = [1] * m  # x_j <= 1 and -x_j <= 1
        relaxed = [tuple(1 if k == j else 100 for k in range(m))
                   for j in range(m)]
        for choice in itertools.product(range(m), repeat=m - 1):
            caps = [min(relaxed[z][j] for z in choice) for j in range(m)]
            assert any(caps[j] > base[j] for j in range(m))
            checks += 1
    print('PASS: %s deterministic checks (including all reduced-color tuples).'%checks)

if __name__ == '__main__':
    run()
