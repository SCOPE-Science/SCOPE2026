#!/usr/bin/env python3
"""Exact integer certificate for minimal super-dominating sets on paths.

Runs with Python 3 and the standard library. A 9-letter window tests
maximality of the complementary open-irredundant set. A second independent
implementation checks the graph definition on small paths.
"""
from collections import defaultdict

ABSENT = -1
Q = (1, 0, 0, -1, -1, -2, -2, -1, 1, 2, 1)
INITIAL = (1, 1, 2, 3, 2, 6, 7, 10, 16, 21, 32, 47)
P = (1, 1, 2, 2, 0, 1, -2, -2, -2, -1, 1, 1)


def witnessed(w):
    """Can the middle vertex of a five-letter word be witnessed?"""
    a, b, c, d, e = w
    if c != 1:  # absent or in the complementary super-dominating set
        return True
    return ((b == 0 and a in (0, ABSENT)) or
            (d == 0 and e in (0, ABSENT)))


def permitted(w):
    """Check completed central position of a nine-letter word."""
    assert len(w) == 9
    if w[4] == ABSENT:
        return True
    if not witnessed(w[2:7]):
        return False
    if w[4] == 1:
        return True
    changed = w[:4] + (1,) + w[5:]
    # Adding the center can change witnesses only at distance <= 2.
    # The proposed addition must destroy feasibility at one such place.
    return any(not witnessed(changed[j-2:j+3]) for j in range(2, 7))


def append(vectors, symbol):
    output = defaultdict(int)
    for old, count in vectors.items():
        nine = old + (symbol,)
        if permitted(nine):
            output[nine[1:]] += count
    return dict(output)


def close_and_count(v):
    for _ in range(4):
        v = append(v, ABSENT)
    return sum(v.values())


def count_by_graph_definition(n):
    """Exhaustively test the literal path graph without the window predicate."""
    neighbours = [tuple(j for j in (i-1, i+1) if 0 <= j < n)
                  for i in range(n)]

    def is_super_dominating(S):
        outside = tuple(i for i in range(n) if not ((S >> i) & 1))
        for v in outside:
            found = False
            for u in neighbours[v]:
                if (S >> u) & 1:
                    if sum(1 for t in neighbours[u]
                           if not ((S >> t) & 1)) == 1:
                        found = True
                        break
            if not found:
                return False
        return True

    result = 0
    for mask in range(1 << n):
        if not is_super_dominating(mask):
            continue
        if all(not is_super_dominating(mask & ~(1 << i))
               for i in range(n) if ((mask >> i) & 1)):
            result += 1
    return result


def run():
    v = {(ABSENT,) * 8: 1}
    vectors = [v]
    values = [close_and_count(v)]
    for n in range(1, 19):
        v = append(v, 0)
        # Separate the second branch, because both extensions must use
        # the same pre-step vector.
        prev = vectors[-1]
        branch = append(prev, 1)
        for st, count in branch.items():
            v[st] = v.get(st, 0) + count
        vectors.append(v)
        values.append(close_and_count(v))

    assert tuple(values[:12]) == INITIAL, values[:12]
    assert tuple(values[:18]) == (
        1, 1, 2, 3, 2, 6, 7, 10, 16, 21, 32, 47,
        67, 99, 142, 206, 302, 438)
    for n in range(12, 19):
        assert sum(Q[j] * values[n-j] for j in range(11)) == 0

    # The critical exact vector identity, not just a scalar recurrence.
    # For all 8-letter states s, sum_j Q[j] D_(18-j)(s) == 0.
    keys = set().union(*(set(vectors[18-j]) for j in range(11)))
    assert all(sum(Q[j] * vectors[18-j].get(s, 0)
                   for j in range(11)) == 0 for s in keys)
    assert len(vectors[18]) == 111
    assert all(ABSENT not in st for st in vectors[18])
    print('EXACT_INTEGER_VECTOR_RECURRENCE_PASS', len(keys), 'states', 18)
    # Because appending a binary bit is one fixed linear transformation,
    # this zero vector remains zero at every later n. Closing each path
    # with four ABSENT symbols is another fixed linear functional.

    for n in range(0, 16):
        independent = count_by_graph_definition(n)
        assert independent == values[n], (n, independent, values[n])
    print('INDEPENDENT_LITERAL_GRAPH_ENUMERATION_PASS', 'n=0..15')

    # Numerator is determined by Q(z)A(z) for degrees 0..11.
    assert all(sum(Q[j] * values[i-j] for j in range(min(i, 10)+1))
               == P[i] for i in range(12))
    print('RATIONAL_GENERATING_FUNCTION_COEFFICIENTS_PASS')

    # Extra exact independent iterative recurrence checks well beyond the
    # finite proof bound, not used as proof of the infinite assertion.
    for n in range(19, 75):
        last = vectors[-1]
        a = append(last, 0)
        b = append(last, 1)
        for s, num in b.items():
            a[s] = a.get(s, 0) + num
        vectors.append(a)
        new = close_and_count(a)
        assert new == -sum(Q[j]*values[n-j] for j in range(1, 11))
        values.append(new)
    print('EXTRA_RECURRENCE_CHECK_PASS', 'n=19..74')
    print('FIRST_VALUES', values[1:21])
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
