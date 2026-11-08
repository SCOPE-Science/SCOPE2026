"""Independent exact distance check for crown matching switches on nine positions.
Run: python3 verify_crown_switch_independent.py
Uses recursive matching generation and direct breadth-first exploration of tuple states.
"""
from collections import Counter, deque

N = 9

def generate_states():
    p = [-1] * N
    def rec(i, used):
        if i == N:
            yield tuple(p)
            return
        for j in range(N):
            if j != i and not (used & (1 << j)):
                p[i] = j
                yield from rec(i + 1, used | (1 << j))
    yield from rec(0, 0)

def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(N):
        if i in seen:
            continue
        j, size = i, 0
        while j not in seen:
            seen.add(j)
            j = p[j]
            size += 1
        lengths.append(size)
    return tuple(sorted(lengths))

def neighbours(p):
    # Swapping the values at a,b cannot introduce a fixed point elsewhere.
    for a in range(N):
        for b in range(a + 1, N):
            if p[b] != a and p[a] != b:
                v = list(p)
                v[a], v[b] = v[b], v[a]
                yield tuple(v)

def distances(start):
    d = {start: 0}
    q = deque((start,))
    while q:
        p = q.popleft()
        v = d[p] + 1
        for t in neighbours(p):
            if t not in d:
                d[t] = v
                q.append(t)
    return d

states = set(generate_states())
assert len(states) == 133496
by_type = Counter(map(cycle_type, states))
expected = {
    (2,2,2,3):(2520,9),
    (2,2,5):(9072,8),
    (2,3,4):(15120,9),
    (2,7):(25920,8),
    (3,3,3):(2240,10),
    (3,6):(20160,9),
    (4,5):(18144,8),
    (9,):(40320,8),
}
assert set(by_type) == set(expected)
representatives = {}
for p in states:
    typ = cycle_type(p)
    if typ not in representatives:
        representatives[typ] = p
for typ in sorted(expected):
    seed = representatives[typ]
    d = distances(seed)
    assert len(d) == 133496
    assert set(d) == states
    size, ecc = expected[typ]
    assert by_type[typ] == size
    assert max(d.values()) == ecc
    far = [p for p, value in d.items() if value == 10]
    if typ == (3,3,3):
        assert len(far) == 1
        inv = [None]*N
        for i,j in enumerate(seed):
            inv[j] = i
        assert far[0] == tuple(inv)
    else:
        assert not far
    print('type=', typ, 'size=', size, 'ecc=', ecc, 'shells=', sorted(Counter(d.values()).items()))
print('independent_checks_passed states=133496 diameter=10 diametral_pairs=1120')
