"""Exact-integer checks of the zero-field separable-field automaton theorem.

Run: python3 checker.py
No external libraries are required. Finite checks are not a substitute for the proof.
"""


def nor_mask(a, n):
    """Radius-one closed-neighborhood NOR on a cyclic set."""
    return frozenset(j for j in range(n)
                     if all((j + d) % n not in a for d in (-1, 0, 1)))


def zero_field_update(x, height, width):
    """Full row/column integer update for equal small-zero selection intervals."""
    if not x:
        return frozenset()  # absorbing zero-state convention
    r = [sum((j, i) in x for i in range(width)) for j in range(height)]
    c = [sum((j, i) in x for j in range(height)) for i in range(width)]
    R = [sum(r[(j + d) % height] for d in (-1, 0, 1))
         for j in range(height)]
    C = [sum(c[(i + d) % width] for d in (-1, 0, 1))
         for i in range(width)]
    return frozenset((j, i) for j in range(height) for i in range(width)
                     if R[j] * C[i] == 0)


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def closed_word_count(n):
    m = [[1, 1, 0, 0], [0, 0, 1, 0],
         [0, 0, 0, 1], [1, 0, 0, 1]]
    p = [[int(i == j) for j in range(4)] for i in range(4)]
    for _ in range(n):
        p = matmul(p, m)
    return sum(p[i][i] for i in range(4)) - 2


def lucas_correction(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    # 2*cos(n*pi/3) is six-periodic and integer valued.
    return a + (2, 1, -1, -2, -1, 1)[n % 6] - 2


def check_one_dimensional():
    for n in range(4, 14):
        recurrent = 0
        for bits in range(1 << n):
            a = frozenset(j for j in range(n) if (bits >> j) & 1)
            t1 = nor_mask(a, n)
            t2 = nor_mask(t1, n)
            t3 = nor_mask(t2, n)
            assert t3 == t1, (n, bits, 'T3')
            if a and len(a) < n and t2 == a:
                recurrent += 1
                assert t1 and t1 != a
        assert recurrent == closed_word_count(n), (n, 'trace')
        assert recurrent == lucas_correction(n), (n, 'Lucas')
    print('Cyclic one-dimensional checks passed for lengths 4..13.')


def check_grid(height, width):
    population = [0, 0, 0]
    for bits in range(1 << (height * width)):
        x = frozenset((j, i) for j in range(height) for i in range(width)
                      if (bits >> (j * width + i)) & 1)
        x1 = zero_field_update(x, height, width)
        x2 = zero_field_update(x1, height, width)
        x3 = zero_field_update(x2, height, width)
        x4 = zero_field_update(x3, height, width)
        assert x2 == x4, (height, width, bits, 'F4=F2')
        if x == x1 or x == x2:
            population[0] += 1
        elif x1 == x2 or x1 == x3:
            population[1] += 1
        else:
            population[2] += 1
    expected = 1 + lucas_correction(height) + lucas_correction(width)
    assert population[0] == expected, (height, width, population, expected)
    assert population[2] > 0, (height, width, 'sharpness')
    print(f'{height}x{width}: {sum(population)} states; entry populations {population}; exact recurrent count {expected}.')


if __name__ == '__main__':
    check_one_dimensional()
    check_grid(4, 4)
    check_grid(4, 5)
    print('All exact checks passed.')
