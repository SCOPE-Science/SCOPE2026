"""Independent finite checks of the three-step Pell cycle-spectrum theorem.

Requires Python 3.9 or later. No external dependencies.
"""

from collections import Counter

M = ((2, 1, 1), (1, 0, 0), (0, 1, 0))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def mul(a, b):
    return tuple(tuple(sum(a[i][r] * b[r][j] for r in range(3))
                       for j in range(3)) for i in range(3))


def powmat(a, n):
    out = I
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


def det(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def v2(x):
    assert x
    return (x & -x).bit_length() - 1


assert det(M) == 1
m7 = powmat(M, 7)
assert m7 == ((545, 298, 214), (214, 117, 84), (84, 46, 33))
b = tuple(tuple((m7[i][j] - I[i][j]) // 2 for j in range(3))
          for i in range(3))
assert det(b) == 87
bb = mul(b, b)
c = tuple(tuple(b[i][j] + bb[i][j] for j in range(3))
          for i in range(3))
assert det(c) == 7569
assert powmat(M, 14) == tuple(tuple(I[i][j] + 4*c[i][j]
                                       for j in range(3)) for i in range(3))
print('Exact matrix and odd-determinant base identities: PASS')

# Independently check each predicted 2-adic matrix valuation through depth 14.
for j in range(14):
    p = powmat(M, 7*(1 << j))
    d = tuple(tuple(p[i][r]-I[i][r] for r in range(3))
              for i in range(3))
    assert min(v2(x) for row in d for x in row if x) == j + 1
    leading = tuple(tuple(x // (1 << (j+1)) for x in row) for row in d)
    assert all(x % (1 << (j+1)) == 0 for row in d for x in row)
    assert det(leading) & 1
print('Matrix lifting valuations at fourteen successive depths: PASS')


def shift(v, q):
    a, b, c = v
    return ((2*a + b + c) % q, a, b)


for k in range(1, 6):
    q = 1 << k
    seen = set()
    cycles = Counter()
    total_states = 0
    for a in range(q):
        for b0 in range(q):
            for c0 in range(q):
                start = (a, b0, c0)
                if start in seen:
                    continue
                orbit = []
                v = start
                while v not in seen:
                    orbit.append(v)
                    seen.add(v)
                    v = shift(v, q)
                assert v == start, 'Unexpected preperiodic trajectory'
                d = len(orbit)
                cycles[d] += 1
                total_states += d
                for w in orbit:
                    t = min((v2(x) if x else k) for x in w)
                    expected_d = 1 if t == k else 7 * (1 << (k - t - 1))
                    assert d == expected_d, (k, w, d, expected_d)
    expected = Counter({1: 1})
    expected.update({7 * (1 << j): 4 ** j for j in range(k)})
    assert cycles == expected, (k, cycles, expected)
    assert total_states == q**3
    assert sum(cycles.values()) == (4**k + 2)//3
    print(f'k={k}: {total_states} states, {sum(cycles.values())} cycles, '
          f'period-counts={dict(sorted(cycles.items()))}: PASS')
print('All standalone checks passed.')
