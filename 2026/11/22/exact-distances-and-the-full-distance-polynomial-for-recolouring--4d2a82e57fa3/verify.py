"""Independent finite checks for the metric and distance polynomial of star-colouring reconfiguration.

Run with Python 3, no third-party dependencies. All colorings use named colors.
"""
from collections import Counter, deque
from itertools import product
from math import comb


def predicted_distance(s, t):
    x, y = s[0], t[0]
    disagreements = sum(a != b for a, b in zip(s[1:], t[1:]))
    swapped = any(a == y and b == x for a, b in zip(s[1:], t[1:]))
    return disagreements + (1 + int(swapped) if x != y else 0)


def expected_coefficients(n, k):
    def mul(p, q):
        c = [0] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                c[i + j] += a * b
        return c

    def power(p, exponent):
        result = [1]
        for _ in range(exponent):
            result = mul(result, p)
        return result

    def extend_shift(c, p, shift, factor):
        for j, a in enumerate(p):
            c[j + shift] += factor * a

    T = k * k - 3 * k + 3
    a = power([(k - 1), (k - 1) * (k - 2)], n)
    b = power([k - 2, T], n)
    c = power([k - 2, T - 1], n)
    out = [0] * (n + 3)
    extend_shift(out, a, 0, k)
    extend_shift(out, b, 2, k * (k - 1))
    extend_shift(out, c, 1, k * (k - 1))
    extend_shift(out, c, 2, -k * (k - 1))
    return out


def partition_type(s):
    return tuple(sorted(Counter(s[1:]).values(), reverse=True))


def verify(n, k):
    states = [(x,) + a for x in range(k) for a in product((v for v in range(k) if v != x), repeat=n)]
    states_idx = {s: i for i, s in enumerate(states)}
    orbit_counts = Counter(partition_type(s) for s in states)
    representative = {}
    for i, s in enumerate(states):
        representative.setdefault(partition_type(s), i)
    distance_counts = [0] * (n + 3)
    for p, origin in representative.items():
        start = states[origin]
        dist = [-1] * len(states)
        dist[origin] = 0
        todo = deque([origin])
        while todo:
            idx = todo.popleft()
            s = states[idx]
            for j in range(n + 1):
                for c in range(k):
                    if c == s[j]:
                        continue
                    if j == 0 and c in s[1:]:
                        continue
                    if j > 0 and c == s[0]:
                        continue
                    t = s[:j] + (c,) + s[j+1:]
                    u = states_idx[t]
                    if dist[u] == -1:
                        dist[u] = dist[idx] + 1
                        todo.append(u)
        assert all(d >= 0 for d in dist)
        for t, distance in zip(states, dist):
            assert distance == predicted_distance(start, t), (n, start, t, distance)
            distance_counts[distance] += orbit_counts[p]
    theory = expected_coefficients(n, k)
    assert theory == distance_counts, (n, theory, distance_counts)
    assert sum(theory) == len(states) ** 2
    assert max(i for i, a in enumerate(theory) if a) == n + 2
    assert theory[n + 2] == k*(k-1)*((k*k-3*k+3)**n-(k*k-3*k+2)**n)
    print(f'n={n} k={k} states={len(states)} orbit_representatives={len(representative)} PASS',flush=True)



# Boundary witness: with only n named colours the proposed n+2 law is false.
def verify_sharpness(n):
    k = n
    if n < 3:
        return
    x, y = 0, 1
    s = (x,) + (y,) * n
    t = (y, x, x) + tuple(range(2, n))
    assert len(s) == len(t) == n + 1
    todo = deque([(s, 0)])
    seen = {s}
    while todo:
        a, steps = todo.popleft()
        if a == t:
            assert steps == n + 3, (n, steps)
            print(f'SHARP n={n} k={k} distance={steps} predicted={n+2} PASS', flush=True)
            return
        for j in range(n + 1):
            for c in range(k):
                if c == a[j] or (j == 0 and c in a[1:]) or (j > 0 and c == a[0]):
                    continue
                b = a[:j] + (c,) + a[j+1:]
                if b not in seen:
                    seen.add(b)
                    todo.append((b, steps + 1))
    raise AssertionError('Boundary witness unreachable')

if __name__ == '__main__':
    for n in range(2, 6):
        for k in (n+1, n+2):
            verify(n, k)
    for n in range(3, 7):
        verify_sharpness(n)
    print('VERIFY_OK')
