"""Exact integer certificate for the finite-ring one-step image of ECA 73.

Run with Python 3.9+ and no third-party modules.
"""
from collections import deque

# Coefficients of f_1,...,f_6 in increasing powers of z; all have f(0)=1.
FACTORS = (
    (1, -1),
    (1, -1, 1),
    (1, 0, -1, 0, 0, -1),
    (1, 0, -1, -1, 0, -1),
    (1, -1, 0, -1, 1, -1, 1, -1),
    (1, -4, 5, -2, 1, -4, 9, -13, 12, -7, 1, 4, -6, 4, -2),
)
# F(z) = sum_{n>=1} a_n*z^n = 1/2 sum_i exp_i * (-z f_i'/f_i) - 2*z^2 - 5*z^5.
EXPONENTS = (-2, -1, 1, -2, -1, 2)


def convolution(left, right):
    r = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            r[i + j] += a * b
    return r


def denominator():
    q = [1]
    for f in FACTORS:
        q = convolution(q, f)
    assert len(q) == 35 and q[0] == 1
    return q


def predicted_counts(max_n):
    res = [0] * (max_n + 1)
    for f, exponent in zip(FACTORS, EXPONENTS):
        # Coefficients g_n of -z*f'(z)/f(z):
        # g_0=0 and g_n=-n*f_n-sum_{j>=1}f_j*g_{n-j}.
        g = [0] * (max_n + 1)
        d = len(f) - 1
        for n in range(1, max_n + 1):
            g[n] = -(n * f[n] if n <= d else 0)
            g[n] -= sum(f[j] * g[n - j] for j in range(1, min(d, n) + 1))
            res[n] += exponent * g[n]
    res[2] -= 4
    res[5] -= 10
    assert all(x % 2 == 0 for x in res[1:])
    return [0] + [x // 2 for x in res[1:]]


def relation_automaton():
    # States of the source de Bruijn graph are length-two blocks (a,b).
    edges = [0, 0]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                u, v = 2 * a + b, 2 * b + c
                label = (73 >> (4 * a + 2 * b + c)) & 1
                edges[label] |= 1 << (4 * u + v)

    def product(left, right):
        # Boolean relational composition, represented by a 16-bit integer.
        ans = 0
        for u in range(4):
            for v in range(4):
                if (left >> (4 * u + v)) & 1:
                    ans |= ((right >> (4 * v)) & 15) << (4 * u)
        return ans

    identity = sum(1 << (5 * u) for u in range(4))
    states = [identity]
    indexes = {identity: 0}
    rows = []
    queue = deque([identity])
    while queue:
        r = queue.popleft()
        row = []
        for label in range(2):
            nr = product(r, edges[label])
            if nr not in indexes:
                indexes[nr] = len(states)
                states.append(nr)
                queue.append(nr)
            row.append(indexes[nr])
        rows.append(row)
    accepting = tuple(i for i, r in enumerate(states) if r & identity)
    assert len(states) == len(rows) == 735
    assert len(accepting) == 631
    assert len(set(states)) == 735
    return rows, accepting


def actual_counts(rows, accepting, max_n):
    # The coefficient at length zero is included only to initialize the recurrence.
    d = len(rows)
    vec = [0] * d
    vec[0] = 1
    a = [1]
    for n in range(1, max_n + 1):
        new_vec = [0] * d
        for i, weight in enumerate(vec):
            if weight:
                v, w = rows[i]
                new_vec[v] += weight
                new_vec[w] += weight
        vec = new_vec
        a.append(sum(vec[j] for j in accepting))
    return a


def verify():
    rows, accept = relation_automaton()
    dimension = len(rows)
    q = denominator()
    degree = len(q) - 1
    # The finite implication is exact: Cayley-Hamilton ensures the scalar
    # sequence c_k = sum_j q_j a_{40+k-j} has order at most dimension.
    # If c_0,...,c_{dimension-1} vanish, then every c_k vanishes.
    first_recurrence_index = 40
    last = first_recurrence_index + dimension - 1
    measured = actual_counts(rows, accept, last)
    candidate = predicted_counts(first_recurrence_index)
    assert measured[1:first_recurrence_index] == candidate[1:first_recurrence_index]
    for n in range(first_recurrence_index, last + 1):
        lhs = sum(q[j] * measured[n - j] for j in range(degree + 1))
        assert lhs == 0, (n, lhs)
    # The proposed generating series has denominator q and has numerator
    # of degree <=39: logarithmic derivatives contribute numerator of degree
    # <=deg(q), while -2*z^2-5*z^5 contributes degree <=39.
    assert sum(len(f) - 1 for f in FACTORS) == 34
    assert first_recurrence_index > 34 + 5 - 1
    expected = (2, 2, 5, 12, 17, 34, 79, 140, 275, 544, 992, 1950)
    assert tuple(measured[1:13]) == expected
    print('VERIFY_OK: Rule 73 cyclic image exact rational series')
    print('relation_states=735 accepting=631 first_match=1..39 recurrence_checked=40..774')
    print('counts n=1..12:', *expected)
    print('denominator degree=34; distinct output words counted, not preimages')


if __name__ == '__main__':
    verify()
