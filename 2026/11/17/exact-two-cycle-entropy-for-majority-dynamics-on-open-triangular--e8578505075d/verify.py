"""Exact finite transfer certificate for periodic majority dynamics on P_n square K_3.
Run with Python 3 standard library: python3 verify.py.
"""
from fractions import Fraction


def majority(a, left, right, is_endpoint):
    out = 0
    degree = 3 if is_endpoint else 4
    for row in range(3):
        ones = (a & (7 ^ (1 << row))).bit_count()
        ones += (right >> row) & 1
        if not is_endpoint:
            ones += (left >> row) & 1
        if 2 * ones > degree or (2 * ones == degree and (a >> row) & 1):
            out |= 1 << row
    return out


def endpoint(a, b, paired):
    if paired:
        x, y, u, v = a & 7, a >> 3, b & 7, b >> 3
        return majority(x, 0, u, True) == y and majority(y, 0, v, True) == x
    return majority(a, 0, b, True) == a


def interior(a, b, c, paired):
    if paired:
        x, y = b & 7, b >> 3
        return (majority(x, a & 7, c & 7, False) == y and
                majority(y, a >> 3, c >> 3, False) == x)
    return majority(b, a, c, False) == b


def transfer(paired):
    # States record two successive spatial columns; a column itself records
    # one time slice for fixed points, or a pair of time slices for periods <=2.
    symbols = 64 if paired else 8
    m = symbols ** 2
    starts = [0] * m
    ends = [0] * m
    arcs = [[] for _ in range(m)]
    for a in range(symbols):
        for b in range(symbols):
            k = symbols * a + b
            starts[k] = int(endpoint(a, b, paired))
            ends[k] = int(endpoint(b, a, paired))
            for c in range(symbols):
                if interior(a, b, c, paired):
                    arcs[k].append(symbols * b + c)
    return starts, ends, arcs


def advance(v, arcs):
    nxt = [0] * len(v)
    for u, value in enumerate(v):
        if value:
            for w in arcs[u]:
                nxt[w] += value
    return nxt


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def certificate(paired, coefficients, expected_first):
    start, end, arcs = transfer(paired)
    vectors = [start]
    for _ in range(len(coefficients) - 1):
        vectors.append(advance(vectors[-1], arcs))
    # c[0] M^d + c[1] M^(d-1) + ... + c[d] I
    degree = len(coefficients) - 1
    residual = [sum(coefficients[i] * vectors[degree-i][j]
                    for i in range(degree+1))
                for j in range(len(start))]
    assert all(z == 0 for z in residual), 'integer annihilator not zero'
    counts = [dot(v, end) for v in vectors]
    assert counts[:len(expected_first)] == expected_first
    print(('two-step' if paired else 'fixed'), 'states', len(start),
          'arcs', sum(map(len, arcs)), 'initial support', sum(start),
          'annihilator degree', degree, 'residual', sum(map(abs, residual)),
          'first counts', counts[:len(expected_first)])
    return counts


if __name__ == '__main__':
    P = certificate(True, [1, -6, 9, -6, 18, -12, -10, -3, -18, 27],
                    [22, 62, 232, 800, 3028, 11414, 43096, 162746, 614878])
    Q = certificate(False, [1, -4, 3, -1, 3], [4, 8, 22, 62])
    def numerator(initial, denominator):
        return [sum(denominator[j] * initial[k-j] for j in range(k+1))
                for k in range(len(initial))]

    assert numerator(P[:9], [1,-6,9,-6,18,-12,-10,-3,-18,27]) == [
        22,-70,58,-166,340,-94,276,-342,-216]
    assert numerator(Q[:4], [1,-4,3,-1,3]) == [4,-8,2,-6]
    assert (P[0] - Q[0])//2 == 9
    print('Both rational generating-function numerators and finite-vector identities hold.')
