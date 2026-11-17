"""Exact finite-ring check for the reversible second-order Rule 54."""
from collections import Counter


def rule54_word(y, n):
    out = 0
    for i in range(n):
        a = (y >> ((i - 1) % n)) & 1
        b = (y >> i) & 1
        c = (y >> ((i + 1) % n)) & 1
        out |= (b ^ (a | c)) << i
    return out


def expected_histogram(n):
    # Enumerate independent subsets of the step-two cycle, weighted by
    # three choices of temporal phase at every marked position.
    h = Counter()
    for mask in range(1 << n):
        if all(not ((mask >> i) & 1 and (mask >> ((i+2) % n)) & 1)
               for i in range(n)):
            h[mask.bit_count()] += 3 ** mask.bit_count()
    h[0] += 1  # All-zero temporal history; all-seven already counted.
    return h


def actual_histogram(n):
    size = 1 << n
    f = [rule54_word(y, n) for y in range(size)]
    hist = Counter()
    for a in range(size):
        for b in range(size):
            c = a ^ f[b]
            d = b ^ f[c]
            e = c ^ f[d]
            if d == a and e == b:
                defect_count = 0
                for i in range(n):
                    temporal_column = (((a >> i) & 1) |
                                       (((b >> i) & 1) << 1) |
                                       (((c >> i) & 1) << 2))
                    if temporal_column not in (0, 7):
                        defect_count += 1
                hist[defect_count] += 1
    return hist


def lucas3(m):
    s0, s1 = 2, 1
    if m == 0:
        return s0
    for _ in range(1, m):
        s0, s1 = s1, s1 + 3 * s0
    return s1


if __name__ == '__main__':
    for n in range(3, 11):
        a = actual_histogram(n)
        b = expected_histogram(n)
        assert a == b, (n, a, b)
        z = lucas3(n) if n % 2 else lucas3(n // 2) ** 2
        assert sum(a.values()) == 1 + z
        assert (sum(a.values()) - 2) % 3 == 0
        print(f'n={n}: fixed_R3={sum(a.values())}, primitive3_orbits={(sum(a.values())-2)//3}, defect_hist={dict(sorted(a.items()))}')
    print('DIRECT_EXHAUSTIVE_PASS')
