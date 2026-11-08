#!/usr/bin/env python3
"""Exact reproducibility certificate for the I6+I3+I2+I1 rational elliptic surface.
Run with Python 3 and its standard library. No symbolic/numerical dependencies.
Checks the complete 17-curve principal-minor census and an independent
15-orbit forbidden-support characterization by integer determinants.
"""
from collections import Counter

FIBERS = (6, 3, 2)
N = 17
NAMES = tuple([f'C{n}_{i}' for n in FIBERS for i in range(n)]
              + [f'S{i}' for i in range(6)])
INDEX = {name: i for i, name in enumerate(NAMES)}
assert len(INDEX) == N

# Minus the intersection form, ordered as 6+3+2 fibre components, 6 sections.
A = [[0] * N for _ in range(N)]
for i in range(N):
    A[i][i] = 2 if i < 11 else 1
start = 0
for n in FIBERS:
    for i in range(n):
        j = (i + 1) % n
        A[start+i][start+j] -= 1
        A[start+j][start+i] -= 1
    start += n
for i in range(6):
    for j in (i % 6, 6 + i % 3, 9 + i % 2):
        A[11+i][j] -= 1
        A[j][11+i] -= 1

# A set of 15 pattern representatives for the complete obstruction family.
# Each index pattern is closed under simultaneous cyclic translation by 1.
PATTERNS = (
    ('C6_0','C6_1','C6_2','C6_3','C6_4','C6_5'),
    ('C3_0','C3_1','C3_2'),
    ('C2_0','C2_1'),
    ('C6_0','C6_1','C6_5','S0'),
    ('C6_0','C3_0','S0'),
    ('C6_0','C2_0','S0'),
    ('C3_0','C2_0','S0'),
    ('C6_0','C6_1','S0','S1'),
    ('C3_0','C3_1','S0','S1'),
    ('C6_0','C6_1','C6_2','S0','S2'),
    ('C6_0','C6_2','C6_3','C6_4','C6_5','S0','S2'),
    ('C3_0','C3_2','S0','S2'),
    ('C2_0','S0','S2'),
    ('C6_0','C6_1','C6_2','C6_3','S0','S3'),
    ('C3_0','S0','S3'),
)

def det_exact(indices):
    """Fraction-free Bareiss determinant with exact division and pivoting."""
    m = len(indices)
    if m == 0:
        return 1
    b = [[A[i][j] for j in indices] for i in indices]
    denominator = 1
    sign = 1
    for k in range(m-1):
        if b[k][k] == 0:
            r = next((i for i in range(k+1,m) if b[i][k] != 0), None)
            if r is None:
                return 0
            b[k], b[r] = b[r], b[k]
            sign *= -1
        pivot = b[k][k]
        for i in range(k+1, m):
            for j in range(k+1, m):
                numerator = b[i][j] * pivot - b[i][k] * b[k][j]
                assert numerator % denominator == 0
                b[i][j] = numerator // denominator
        for i in range(k+1, m):
            b[i][k] = 0
        denominator = pivot
    return sign * b[-1][-1]

def indices(mask):
    return [i for i in range(N) if mask & (1 << i)]

def mask_of(names):
    return sum(1 << INDEX[n] for n in names)

def translate(name, step):
    if name[0] == 'S':
        return f'S{(int(name[1:]) + step) % 6}'
    n, i = name[1:].split('_')
    return f'C{n}_{(int(i)+step) % int(n)}'

def main():
    assert all(A[i][j] == A[j][i] for i in range(N) for j in range(N))
    assert all(A[i][i] in (1,2) for i in range(N))
    for step in range(6):
        p = [INDEX[translate(name,step)] for name in NAMES]
        assert all(A[i][j] == A[p[i]][p[j]] for i in range(N) for j in range(N))

    # Method I: every subset is visited; a failed principal submatrix
    # excludes all supersets. If every codimension-one principal block is
    # positive definite, positivity of the determinant is equivalent to PD.
    good = bytearray(1 << N)
    good[0] = 1
    counts = Counter({0:1})
    minimal_bad = set()
    for mask in range(1, 1 << N):
        x = mask
        while x:
            bit = x & -x
            x ^= bit
            if not good[mask ^ bit]:
                break
        else:
            determinant = det_exact(indices(mask))
            if determinant > 0:
                good[mask] = 1
                counts[mask.bit_count()] += 1
            else:
                assert determinant == 0, (mask, determinant)
                minimal_bad.add(mask)
    assert sum(counts.values()) == 17853
    assert len(minimal_bad) == 72

    # Method II: independently construct 15 cyclic orbit representatives,
    # and test all 2^17 subsets against the resulting forbidden hypergraph.
    forbidden = set()
    orbit_sizes = []
    for rep in PATTERNS:
        orbit = {mask_of(translate(name,step) for name in rep)
                 for step in range(6)}
        orbit_sizes.append(len(orbit))
        assert not forbidden.intersection(orbit)
        forbidden.update(orbit)
    assert len(forbidden) == 72
    assert Counter(orbit_sizes) == {1:3, 3:1, 6:11}
    assert forbidden == minimal_bad
    for f in forbidden:
        assert det_exact(indices(f)) == 0
        assert all(good[f ^ (1 << i)] for i in indices(f))
    counts2 = Counter()
    for mask in range(1 << N):
        admissible = all((mask & f) != f for f in forbidden)
        assert admissible == bool(good[mask])
        if admissible:
            counts2[mask.bit_count()] += 1
    assert counts2 == counts

    expected = (1,17,135,637,1929,3852,5039,4111,1836,296)
    assert tuple(counts[k] for k in range(10)) == expected
    assert not any(counts[k] for k in range(10,18))
    assert Counter(f.bit_count() for f in forbidden) == {2:1,3:28,4:24,5:6,6:7,7:6}
    print('CLASSIFICATION: 17 curves; 131072 possible supports')
    print('EXACT_CHAMBER_POLYNOMIAL',list(enumerate(expected)))
    print('TOTAL_CHAMBERS',sum(expected))
    print('MAXIMAL_SUPPORT_SIZE',9,'MAXIMAL_SUPPORTS',expected[-1])
    print('MINIMAL_FORBIDDEN_SUPPORTS',len(forbidden))
    print('OBSTRUCTION_ORBITS',len(PATTERNS),'SIZES',dict(Counter(orbit_sizes)))
    print('OBSTRUCTION_SIZE_COUNTS',dict(sorted(Counter(f.bit_count() for f in forbidden).items())))
    print('EXACT_PRINCIPAL_MINORS_AND_ORBIT_AVOIDANCE_AGREE')

if __name__ == '__main__':
    main()
