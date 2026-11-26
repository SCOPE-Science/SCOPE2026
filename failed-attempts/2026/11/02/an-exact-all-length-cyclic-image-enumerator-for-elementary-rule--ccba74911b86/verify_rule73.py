#!/usr/bin/env python3
"""Exact finite-state certificate for cyclic one-step images of binary Rule 73.

Run: python3 verify_rule73.py
No external packages are required. All arithmetic in the certificate is integer.
"""

RULE = 73
DIAGONAL = sum(1 << (5 * i) for i in range(4))
IDENTITY = DIAGONAL

# All coefficients are in ascending powers of z, and each polynomial has constant 1.
FACTORS = [
    [1, -1],
    [1, -1, 1],
    [1, 0, -1, 0, 0, -1],
    [1, 0, -1, -1, 0, -1],
    [1, -1, 0, -1, 1, -1, 1, -1],
    [1, -4, 5, -2, 1, -4, 9, -13, 12, -7, 1, 4, -6, 4, -2],
]
# A(z) = 1-2 z^2-5 z^5 + sum_j (HALF_COEFFS[j]/2) * L(FACTORS[j]),
# L(f) = -z f'(z)/f(z).
HALF_COEFFS = [-2, -1, 1, -2, -1, 2]
EXPECTED_FIRST_40 = [
    1, 2, 2, 5, 12, 17, 34, 79, 140, 275,
    544, 992, 1950, 3668, 6983, 13345, 25156, 47908, 90520, 171287,
    324082, 611791, 1156357, 2182656, 4120610, 7777972, 14676588,
    27697442, 52258267, 98600611, 186030139, 350966409, 662142884,
    1249170818, 2356636139, 4445888749, 8387284578, 15822822600,
    29849970182, 56312354870,
]


def mats(rule):
    result = [0, 0]
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                v = (rule >> (4 * a + 2 * b + c)) & 1
                result[v] |= 1 << (4 * (2 * a + b) + (2 * b + c))
    return result


def compose(x, y):
    z = 0
    for i in range(4):
        row = (x >> (4 * i)) & 15
        resulting_row = 0
        while row:
            bit = row & -row
            k = bit.bit_length() - 1
            resulting_row |= (y >> (4 * k)) & 15
            row -= bit
        z |= resulting_row << (4 * i)
    return z


def closure(rule):
    letters = mats(rule)
    states = [IDENTITY]
    indices = {IDENTITY: 0}
    transitions = []
    for r in states:
        row = []
        for letter in letters:
            v = compose(r, letter)
            if v not in indices:
                indices[v] = len(states)
                states.append(v)
            row.append(indices[v])
        transitions.append(tuple(row))
    return states, transitions


def multiply_polynomials(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def logderivative_series(f, length):
    # The series d=-z*f'/f obeys f*d=-z*f', with d_0=0.
    d = [0] * length
    for n in range(1, length):
        t = -n * f[n] if n < len(f) else 0
        for j in range(1, min(n, len(f) - 1) + 1):
            t -= f[j] * d[n-j]
        d[n] = t
    return d


def forward_outputs(n):
    seen = set()
    for x in range(1 << n):
        y = 0
        for i in range(n):
            a = (x >> ((i-1) % n)) & 1
            b = (x >> i) & 1
            c = (x >> ((i+1) % n)) & 1
            y |= ((RULE >> (4*a+2*b+c)) & 1) << i
        seen.add(y)
    return len(seen)


def verify():
    states, transitions = closure(RULE)
    assert len(states) == 735, len(states)
    assert len(set(states)) == len(states)
    assert states[0] == IDENTITY
    assert all(len(row) == 2 and max(row) < 735 for row in transitions)

    q = [1]
    for factor in FACTORS:
        q = multiply_polynomials(q, factor)
    assert len(q) == 35 and q[0] == 1 and q[-1] == -2

    # For any relation R, g_k(R) counts accepted words of length k from R.
    g = [[int(bool(r & DIAGONAL)) for r in states]]
    for k in range(100):
        old = g[-1]
        g.append([old[p] + old[q0] for p, q0 in transitions])
    a = [g[k][0] for k in range(len(g))]
    assert a[:40] == EXPECTED_FIRST_40

    # Vector identity for every one of the 735 reachable Boolean relations.
    # As powers of the same transition operator commute, this single identity
    # implies the recurrence at ALL n>=40, not just n<=100.
    residual = [sum(q[j] * g[40-j][i] for j in range(35))
                for i in range(len(states))]
    assert residual == [0] * len(states), ('vector identity', max(map(abs, residual)))
    for n in range(40, 101):
        assert sum(q[j] * a[n-j] for j in range(35)) == 0

    # The proposed expression has denominator Q=product FACTORS and its
    # numerator has degree at most 39. Equality of 40 coefficients is decisive.
    d = [logderivative_series(f, 40) for f in FACTORS]
    rhs_twice = [2 * (int(n == 0)-2*int(n == 2)-5*int(n == 5))
                 + sum(c * dd[n] for c, dd in zip(HALF_COEFFS, d))
                 for n in range(40)]
    assert rhs_twice == [2 * t for t in EXPECTED_FIRST_40]

    # An independent exhaustive forward-image check uses literal ring updates,
    # without any Boolean-relation products or transfer-matrix code.
    for n in range(1, 15):
        assert a[n] == forward_outputs(n), (n, a[n], forward_outputs(n))
    print('VERIFY_OK; 735 relation states; Q degree 34; 735 exact vector identities;')
    print('40 generating-function coefficients; full ring enumeration n=1..14;')
    print('a_8=%d a_12=%d a_16=%d a_20=%d' % (a[8], a[12], a[16], a[20]))


if __name__ == '__main__':
    verify()
