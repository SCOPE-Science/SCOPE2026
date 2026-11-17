"""Independent mathematical macrostep and conserved-reflector tests.

Only standard Python is required: python3 column_invariant.py.
The macrostep is implemented directly from turn-flip-move operations; the
predicted projected reflector walk is independently checked for every state.
"""
from collections import Counter

def step(n, colors, p, d):
    x, y = p % n, p // n
    black = (colors >> p) & 1
    d = (d + (3 if black else 1)) % 4
    colors ^= 1 << p
    if d == 0 or d == 2:
        y ^= 1
    elif d == 1:
        x = (x + 1) % n
    else:
        x = (x - 1) % n
    return colors, y * n + x, d

def invariant(n, colors, p):
    x = p % n
    return sum((((colors >> k) ^ (colors >> (k + n)) ^ (k == x)) & 1) << k
               for k in range(n))

def projected_return(n, b, x, h):
    start = (x, h)
    t = 0
    while True:
        x = (x + h) % n
        h *= 1 if ((b >> x) & 1) else -1
        t += 1
        if (x, h) == start:
            return t
        assert t <= 2 * n

for n in range(2, 8):
    trials = 0
    for colors in range(1 << (2 * n)):
        for p in range(2 * n):
            for d in (0, 2):
                b = invariant(n, colors, p)
                c1, p1, d1 = step(n, colors, p, d)
                assert d1 in (1, 3)
                c2, p2, d2 = step(n, c1, p1, d1)
                assert d2 in (0, 2)
                assert invariant(n, c2, p2) == b
                h = 1 if d1 == 1 else -1
                x1 = (p2 % n)
                assert x1 == (p % n + h) % n
                c3, p3, d3 = step(n, c2, p2, d2)
                hnext = 1 if d3 == 1 else -1
                h_predict = h * (1 if (b >> x1) & 1 else -1)
                assert hnext == h_predict
                if (colors % (n + 1) == 0):
                    j = projected_return(n, b, p % n, h)
                    assert (j % 2 == 0) if b != ((1 << n) - 1) else (j == n)
                    assert j <= 2 * n
                trials += 1
    print(f'n={n} macrostep_states_checked={trials} invariant_and_reflector=PASS')
