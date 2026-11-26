"""Finite exact checks of graph-exclusion Fourier inverses on paths."""
from fractions import Fraction as F
from itertools import groupby, product


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def mul(a, b, q):
    x, y = a
    u, v = b
    if q == 3:  # omega^2 = -1 - omega
        return x*u - y*v, x*v + y*u - y*v
    return x*u - y*v, x*v + y*u


def conj(a, q):
    return (a[0] - a[1], -a[1]) if q == 3 else (a[0], -a[1])


ZERO, ONE = (F(0), F(0)), (F(1), F(0))


def phase(k, q):
    k %= q
    if q == 2:
        return ONE if k == 0 else (F(-1), F(0))
    if q == 3:
        return (ONE, (F(0), F(1)), (F(-1), F(-1)))[k]
    if q == 4:
        return (ONE, (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1)))[k]
    raise ValueError(q)


def states(n, q):
    return [t for t in product(range(q), repeat=n)
            if all(not (t[i] and t[i+1]) for i in range(n-1))]


def ipath(m, q):
    z = F(-(q-1), q)
    if m == 0:
        return F(1)
    a, b = F(1), F(1) + z
    for _ in range(2, m+1):
        a, b = b, b + z*a
    return b


def inv(a, b, q):
    n = len(a)
    union = {i for i in range(n) if a[i] or b[i]}
    if any(i+1 in union for i in union):
        return ZERO
    forbidden = union | {i-1 for i in union} | {i+1 for i in union}
    multiplier, run = F(1), 0
    for i in range(n+1):
        if i < n and i not in forbidden:
            run += 1
        elif run:
            multiplier *= ipath(run, q)
            run = 0
    z = conj(phase(sum(x*y for x, y in zip(a, b)), q), q)
    return tuple(v * multiplier / q**len(union) for v in z)


def integer_determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    prev, sign = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            r = next(r for r in range(k+1, n) if a[r][k])
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                val = a[i][j]*pivot - a[i][k]*a[k][j]
                assert val % prev == 0
                a[i][j] = val // prev
        for i in range(k+1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def check(q, n):
    points = states(n, q)
    m = len(points)
    h = [[phase(sum(x*y for x, y in zip(a, b)), q) for b in points] for a in points]
    v = [[inv(a, b, q) for b in points] for a in points]
    extra_zeros = 0
    for i, a in enumerate(points):
        for j, b in enumerate(points):
            total = ZERO
            for k in range(m):
                total = add(total, mul(h[i][k], v[k][j], q))
            assert total == (ONE if i == j else ZERO), (q, n, i, j, total)

            occupied = [bool(x or y) for x, y in zip(a, b)]
            compatible = not any(x and y for x, y in zip(occupied, occupied[1:]))
            if compatible:
                padded = [False, *occupied, False]
                remains = [not any(padded[k:k+3]) for k in range(n)]
                resonance = q == 2 and any(sum(run) % 4 == 2
                                              for bit, run in groupby(remains) if bit)
                assert (v[i][j] == ZERO) == resonance, (q, n, a, b)
                extra_zeros += int(resonance)
            else:
                assert v[i][j] == ZERO, (q, n, a, b)

    if q == 2 and n <= 6:
        num = sum(sum(bool(x) for x in a) for a in points)
        det = integer_determinant([[int(z[0]) for z in row] for row in h])
        assert abs(det) == 2**num, (q, n, det, num)
    if q == 2:
        assert (v[0][0] == ZERO) == (n % 4 == 2)
    assert h == [list(row) for row in zip(*h)]
    assert v == [list(row) for row in zip(*v)]
    print('EXACT_TWO_SIDED q=%d n=%d size=%d independent_union_zeros=%d'
          % (q, n, m, extra_zeros))


if __name__ == '__main__':
    for q, ns in [(2, range(2, 9)), (3, range(2, 6)), (4, range(2, 5))]:
        for n in ns:
            check(q, n)
    print('PATH_INDEPENDENCE_FOURIER_CHECKS_PASS')
