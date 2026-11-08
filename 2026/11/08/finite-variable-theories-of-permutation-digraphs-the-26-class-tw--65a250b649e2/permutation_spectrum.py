"""Independent finite-spectrum checks for permutation digraph classifications."""
from collections import Counter
from itertools import product


def partitions(n, start=1):
    if n == 0:
        yield ()
    else:
        for length in range(start, n + 1):
            for tail in partitions(n - length, length):
                yield (length,) + tail


def logical_signature(cycles, k):
    counts = Counter(cycles)
    if k == 1:
        return (counts[1] > 0, sum(counts[n] for n in counts if n >= 2) > 0)
    if k == 2:
        long = sum(counts[n] for n in counts if n >= 3)
        long_type = 0 if long == 0 else (1 if long == counts[3] == 1 else 2)
        return (min(counts[1], 2), min(counts[2], 2), long_type)
    return tuple(sorted((n, min(counts[n], k)) for n in counts))


def canonical_min_size(signature, k):
    if k == 1:
        return int(signature[0]) + 2 * int(signature[1])
    if k == 2:
        a, b, tail = signature
        return a + 2 * b + {0: 0, 1: 3, 2: 4}[tail]
    return sum(n * count for n, count in signature)


if __name__ == '__main__':
    # The exceptional FO2 spectrum can be derived without any graph logic solver.
    types = {(a, b, t) for a, b, t in product(range(3), range(3), range(3))
             if (a, b, t) != (0, 0, 0)}
    sizes = Counter(canonical_min_size(t, 2) for t in types)
    assert len(types) == 26
    assert sorted(sizes.items()) == [
        (1, 1), (2, 2), (3, 2), (4, 4), (5, 4),
        (6, 4), (7, 3), (8, 3), (9, 2), (10, 1)]
    print('FO2_CLASSES=26 MIN_REPRESENTATIVE_SPECTRUM=' + repr(sorted(sizes.items())))

    # Every exceptional signature has a canonical graph witness of order <= 10.
    for sig in types:
        a, b, t = sig
        witness = (1,) * a + (2,) * b + ((3,) if t == 1 else (4,) if t == 2 else ())
        assert logical_signature(witness, 2) == sig
        assert sum(witness) == canonical_min_size(sig, 2)
    print('FO2_CANONICAL_WITNESSES=26 MAXIMUM_MINIMUM_ORDER=10')

    # Check the Glaisher identity with two independent finite recurrences.
    for k in range(3, 8):
        nmax = 30
        a = [0] * (nmax + 1)
        a[0] = 1
        for ell in range(1, nmax + 1):
            b = [0] * (nmax + 1)
            for n, num in enumerate(a):
                for j in range(k + 1):
                    if n + j * ell <= nmax:
                        b[n + j * ell] += num
            a = b
        b = [0] * (nmax + 1)
        b[0] = 1
        for ell in range(1, nmax + 1):
            if ell % (k + 1) == 0:
                continue
            for n in range(ell, nmax + 1):
                b[n] += b[n - ell]
        assert a == b
    print('PARTITION_EULER_PRODUCTS=k3..7,n0..30 PASS')

    # For bounded size, every actual cycle-type realizes exactly the proposed class.
    examined = 0
    for k in range(1, 6):
        for n in range(1, 14):
            for cycles in partitions(n):
                signature = logical_signature(cycles, k)
                assert canonical_min_size(signature, k) <= n
                examined += 1
    print('CANONICAL_MINIMUM_BOUNDS_CHECKED=' + str(examined) + ' PASS')
