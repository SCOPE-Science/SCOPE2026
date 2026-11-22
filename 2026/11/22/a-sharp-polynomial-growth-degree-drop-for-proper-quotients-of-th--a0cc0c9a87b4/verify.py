"""Finite consistency tests for the Munn-interval growth degree result.

Finite checks do not establish the universal quotient theorem; that proof is symbolic.
"""
from collections import deque

ONE = (0, 0, 0)
X = (0, 1, 1)
Y = (1, 0, -1)


def mul(u, v):
    a, b, k = u
    c, d, l = v
    return (max(a, c - k), max(b, d + k), k + l)


def inv(u):
    a, b, k = u
    return (a + k, b - k, -k)


def length(u):
    a, b, k = u
    return 2 * (a + b) - abs(k)


def ball(n):
    seen = {ONE: 0}
    queue = deque([ONE])
    while queue:
        u = queue.popleft()
        if seen[u] >= n:
            continue
        for g in (X, Y):
            v = mul(u, g)
            if v not in seen:
                seen[v] = seen[u] + 1
                queue.append(v)
    return seen


def right_bicyclic(u):
    a, b, k = u
    return (a, a + k)


def bi_mul(s, t):
    i, j = s
    h, l = t
    r = min(j, h)
    return (i + h - r, j + l - r)


for n in range(11):
    seen = ball(n)
    expected = {
        (a, b, k)
        for a in range(n + 1)
        for b in range(n + 1)
        for k in range(-a, b + 1)
        if length((a, b, k)) <= n
    }
    assert set(seen) == expected, (n, len(seen), len(expected))
    assert all(length(u) == cost for u, cost in seen.items())
    assert len(set(map(right_bicyclic, seen))) == (n + 1) * (n + 2) // 2
    for u in seen:
        assert mul(mul(u, inv(u)), u) == u
        assert mul(mul(inv(u), u), inv(u)) == inv(u)
        assert mul(u, ONE) == u == mul(ONE, u)

for u in ball(4):
    for v in ball(4):
        assert right_bicyclic(mul(u, v)) == bi_mul(right_bicyclic(u), right_bicyclic(v))
        assert mul(mul(u, v), ONE) == mul(u, v)
        assert mul(inv(u), inv(v)) == inv(mul(v, u))

# Test the essential eventual-periodicity implication for a noncomparable
# pair of idempotents, including all small right boundaries and endpoints.
a, b, c, d = 1, 3, 3, 1
B = max(b, d)
for t in range(B, B + 6):
    eleft = (a + t, 0, 0)
    eright = (c + t, 0, 0)
    assert mul(mul(Y, Y), ONE) == (2, 0, -2)
    for j in range(8):
        assert mul(eleft, (0, j, 0)) == (a + t, j, 0)
        assert mul(eright, (0, j, 0)) == (c + t, j, 0)
        for k in range(-a-t, j + 1):
            assert mul((a + t, j, 0), (max(0, -k), max(0, k), k)) == (a + t, j, k)

print('MONOGENIC_INVERSE_QUOTIENT_GROWTH_CHECKS_OK')
