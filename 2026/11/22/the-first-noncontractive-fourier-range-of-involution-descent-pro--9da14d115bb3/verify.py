"""Exact finite certification of Fourier recovery for involution descent sets.

Run with Python >=3.9: python verify.py
Only standard-library integer arithmetic is used.
"""

from collections import Counter
from pathlib import Path


def involutions(n):
    """Generate every involution on {1,...,n}, once, by fixing or pairing its least unused point."""
    perm = [-1] * n

    def visit():
        i = next((i for i in range(n) if perm[i] == -1), None)
        if i is None:
            yield tuple(perm)
            return
        perm[i] = i
        yield from visit()
        perm[i] = -1
        for j in range(i + 1, n):
            if perm[j] == -1:
                perm[i], perm[j] = j, i
                yield from visit()
                perm[i] = perm[j] = -1

    yield from visit()


def descent_mask(perm):
    return sum(1 << i for i in range(len(perm) - 1) if perm[i] > perm[i + 1])


def permutation_histogram(n):
    hist = [0] * (1 << (n - 1))
    for perm in involutions(n):
        hist[descent_mask(perm)] += 1
    return hist


def tableau_histogram(n):
    """Independently count SYT descent masks by growing partition shapes.

    Each standard tableau corresponds to a unique path of addable Young
    diagram corners.  Its descent at i occurs when i+1 is in a lower row.
    """
    hist = [0] * (1 << (n - 1))
    shape = []

    def visit(t, previous_row, mask):
        if t == n:
            hist[mask] += 1
            return
        for r in range(len(shape) + 1):
            if r == len(shape):
                shape.append(1)
            elif r == 0 or shape[r] < shape[r - 1]:
                shape[r] += 1
            else:
                continue
            next_mask = mask | ((1 << (t - 1)) if t > 0 and r > previous_row else 0)
            visit(t + 1, r, next_mask)
            shape[r] -= 1
            if shape[-1] == 0:
                shape.pop()

    visit(0, 0, 0)
    return hist


def hadamard(a):
    """Unnormalized Walsh-Hadamard transform, entirely exact."""
    a = list(a)
    width = 1
    while width < len(a):
        for k in range(0, len(a), 2 * width):
            for j in range(k, k + width):
                x, y = a[j], a[j + width]
                a[j], a[j + width] = x + y, x - y
        width *= 2
    return a


def signed_sums_direct(n):
    """Direct character sums, deliberately not using Hadamard recursion."""
    signatures = [descent_mask(p) for p in involutions(n)]
    return [sum(1 if (s & m).bit_count() % 2 == 0 else -1
                for m in signatures) for s in range(1 << (n - 1))]


SPECTRUM_7 = (
    232, 0, 0, -64, 0, 8, -64, 0, 0, 8, 8, 0, -64, 0, 0, 16,
    0, 8, 8, 0, 8, 0, 0, -8, -64, 0, 0, 24, 0, -8, 16, 0,
    0, 8, 8, 0, 8, 0, 0, -8, 8, 0, 0, 0, 0, 0, -8, 0,
    -64, 0, 0, 24, 0, 0, 24, 0, 0, -8, -8, 0, 16, 0, 0, 0,
)
EXTRA_ZERO_MASKS_7 = {43, 45, 53, 63}
EXPECTED_INVOLUTION_COUNTS = [1, 2, 4, 10, 26, 76, 232, 764, 2620, 9496]
EXPECTED_EARLY_RANKS = [1, 1, 1, 4, 8, 16, 28, 64]


def verify():
    checks = 0
    for n in range(1, 11):
        from_permutations = permutation_histogram(n)
        from_tableaux = tableau_histogram(n)
        assert from_permutations == from_tableaux, ('RSK', n)
        checks += len(from_permutations)
        assert sum(from_permutations) == EXPECTED_INVOLUTION_COUNTS[n - 1], n
        checks += 1
        spectral = hadamard(from_permutations)
        if n <= 7:
            assert spectral == signed_sums_direct(n), ('direct character sums', n)
            checks += len(spectral)
        for s, value in enumerate(spectral):
            if s.bit_count() % 2:
                assert value == 0, ('complement symmetry', n, s)
                checks += 1
            elif n in (1, 2, 4, 5, 6, 8, 9, 10):
                assert value != 0, ('no additional cancellation', n, s)
                checks += 1
        if n <= 8:
            assert sum(v != 0 for v in spectral) == EXPECTED_EARLY_RANKS[n - 1]
            checks += 1
            if n != 7:
                projection = hadamard([int(v != 0) for v in spectral])
                assert sum(map(abs, projection)) == len(spectral)
                checks += 1
        if n == 3:
            assert spectral == [4, 0, 0, 0]
            checks += 4
        if n == 7:
            assert tuple(spectral) == SPECTRUM_7
            checks += 64
            zeros = {s for s, v in enumerate(spectral) if v == 0}
            expected = {s for s in range(64) if s.bit_count() % 2} | EXTRA_ZERO_MASKS_7
            assert zeros == expected
            checks += 64
            assert sum(1 for v in spectral if v != 0) == 28
            checks += 1
            assert min(abs(v) for v in spectral if v) == 8
            checks += 1
            active = [int(v != 0) for v in spectral]
            numerator = hadamard(active)
            assert Counter(numerator) == Counter({0: 24, 2: 16, -2: 16, 4: 4, 28: 2, -4: 2})
            checks += 64
            assert sum(map(abs, numerator)) == 144
            # The four exceptional frequency vectors are linearly independent.
            span = {0}
            for freq in sorted(EXTRA_ZERO_MASKS_7):
                span |= {v ^ freq for v in tuple(span)}
            assert len(span) == 16
            checks += 1
            checks += 1
            assert 4 * sum(map(abs, numerator)) == 9 * 64
            checks += 1
            expected_path = Path(__file__).with_name('spectrum_n7.tsv')
            if expected_path.is_file():
                table = [line.strip().split('\t') for line in expected_path.read_text(encoding='utf-8').splitlines()]
                assert table[0] == ['mask', 'multiplier']
                assert [(int(i), int(v)) for i,v in table[1:]] == list(enumerate(spectral))
                checks += 64
    print('PASS: independent involution and tableau enumerations, Walsh transforms,')
    print('symmetry-forced and exceptional zero sets, and sharp endpoint norm.')
    print(f'Exact integer comparisons/assertions: {checks}')
    print('n=7 zero even masks:', sorted(EXTRA_ZERO_MASKS_7))
    print('n=7 convolution rank: 28; nullity: 36; least nonzero eigenvalue magnitude: 8')
    print('n=7 sharp unrestricted endpoint projection norm: 9/4')
    print('Orders 1..6 and 8 have norm-one projections.')


if __name__ == '__main__':
    verify()
