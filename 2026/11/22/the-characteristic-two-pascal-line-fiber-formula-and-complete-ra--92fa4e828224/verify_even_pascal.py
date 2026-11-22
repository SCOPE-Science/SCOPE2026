"""Exact reproducible checks for binary-field Pascal-line multiplicities.

Uses only Python 3 standard library.  The general theorem is proved in RESULT.md;
these enumerations independently check specified finite fields.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict

MODULI = {8: 0b1011, 16: 0b10011, 32: 0b100101,
          64: 0b1000011, 128: 0b10000011, 256: 0x11b}


def field(q):
    modulus = MODULI[q]
    def multiply(a, b):
        v = 0
        while b:
            if b & 1:
                v ^= a
            b >>= 1
            a <<= 1
            if a & q:
                a ^= modulus
        return v
    times = [[multiply(i, j) for j in range(q)] for i in range(q)]
    inverse = [0] + [next(j for j in range(1, q)
                          if times[i][j] == 1) for i in range(1, q)]
    return times, inverse


def expected(q):
    rho = 2 if q % 3 == 1 else 0
    tangent = q * (q - 1) * (q - 2) * (q - 4) // 12
    secant = (q - 1) * ((q - 2) * (q - 5) * (q - 6) - 2 * rho) // 12
    exterior = (q + 1) * ((q - 2) * (q * q - 5 * q + 2) + 2 * rho) // 12
    return {'tangent': tangent, 'secant': secant, 'exterior': exterior}


def normalized_counts(q):
    """Independent parameter-root incidence, without enumerating hexagons."""
    m, _ = field(q)
    events = Counter()
    number_with_rational_intersection = 0
    for d in range(2, q):
        for e in range(2, q):
            if d == e:
                continue
            de = m[d][e]
            w = m[d][e ^ 1]
            for t in range(2, q):
                denominator = m[t][t ^ 1 ^ d] ^ de
                numerator = m[t][w]
                bad = (denominator == 0,
                       denominator == numerator,
                       m[d][denominator] == numerator,
                       m[e][denominator] == numerator)
                assert sum(bad) <= 1, 'Non-disjoint exceptional parameter loci'
                for name, flag in zip(('infinite', 'one', 'd', 'e'), bad):
                    if flag:
                        events[name] += 1
                if not any(bad):
                    number_with_rational_intersection += 1
    rho = 2 if q % 3 == 1 else 0
    assert events == Counter({
        'infinite': (q - 2) * (q - 5) + rho,
        'one': (q - 2) * (q - 4),
        'd': 2 * (q - 2) * (q - 3),
        'e': (q - 2) * (q - 5) + rho,
    })
    tangent_configs = (q - 2) * (q - 4)
    assert (number_with_rational_intersection - tangent_configs) % 2 == 0
    secant_configs = (number_with_rational_intersection - tangent_configs) // 2
    exterior_configs = (q - 2) * (q - 3) * (q - 4) - secant_configs - tangent_configs
    formulas = expected(q)
    assert tangent_configs * q * (q - 1) // 12 == formulas['tangent']
    assert secant_configs * (q - 1) // 6 == formulas['secant']
    assert exterior_configs * (q + 1) // 6 == formulas['exterior']
    print('normalized', q, 'tangent/secant/exterior',
          tangent_configs, secant_configs, exterior_configs,
          'exceptional', dict(events))


def full_hexagon_counts(q):
    """Direct projective cross-product census; independent of root-incidence derivation."""
    times, inverse = field(q)
    points = [(1, t, times[t][t]) for t in range(q)] + [(0, 0, 1)]
    def cross(a, b):
        return (times[a[1]][b[2]] ^ times[a[2]][b[1]],
                times[a[2]][b[0]] ^ times[a[0]][b[2]],
                times[a[0]][b[1]] ^ times[a[1]][b[0]])
    def standardize(v):
        nonzero = next(a for a in v if a)
        return tuple(times[inverse[nonzero]][a] for a in v)
    chords = [[standardize(cross(points[i], points[j])) if i != j else None
               for j in range(q + 1)] for i in range(q + 1)]
    arrangements = [p for p in permutations(range(1, 6)) if p[0] < p[-1]]
    assert len(arrangements) == 60
    output = Counter()
    for vertices in combinations(range(q + 1), 6):
        for permutation in arrangements:
            a, b, c, d, e, f = ((vertices[0],) +
                                tuple(vertices[i] for i in permutation))
            first = cross(chords[a][b], chords[d][e])
            second = cross(chords[b][c], chords[e][f])
            line = standardize(cross(first, second))
            output[line] += 1
    grouped = defaultdict(set)
    for line, multiplicity in output.items():
        a, b, c = line
        roots = sum((a ^ times[b][t] ^ times[c][times[t][t]]) == 0
                    for t in range(q)) + (1 if c == 0 else 0)
        assert roots in (0, 1, 2)
        grouped[('exterior', 'tangent', 'secant')[roots]].add(multiplicity)
    actual = {name: next(iter(values)) for name, values in grouped.items()}
    assert all(len(values) == 1 for values in grouped.values())
    assert actual == expected(q), (q, actual, expected(q))
    assert len(output) == q * q + q + 1
    assert sum(output.values()) == len(list(combinations(range(q + 1), 6))) * 60
    print('direct', q, 'line count', len(output), 'per-line multiplicities', actual)


if __name__ == '__main__':
    for q in (8, 16, 32, 64, 128, 256):
        normalized_counts(q)
    for q in (8, 16):
        full_hexagon_counts(q)
    print('All prescribed exact finite-field checks passed.')
