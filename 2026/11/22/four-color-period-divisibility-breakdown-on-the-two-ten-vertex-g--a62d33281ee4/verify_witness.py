#!/usr/bin/env python3
"""Direct finite-state witnesses for four-color cyclic and excitable dynamics."""
from itertools import product


def graph(k):
    g = [set() for _ in range(10)]
    for i in range(5):
        for a, b in [(i, (i+1)%5), (i, 5+i), (5+i, 5+(i+k)%5)]:
            g[a].add(b); g[b].add(a)
    assert all(len(t) == 3 for t in g)
    return g


def digits(s):
    return tuple((s >> (2*i)) & 3 for i in range(10))


def step(x, g, model):
    y = []
    for i, c in enumerate(x):
        if model == 'C':
            a = (c+1)%4
            y.append(a if any(x[j] == a for j in g[i]) else c)
        elif c:
            y.append((c+1)%4)
        else:
            y.append(int(any(x[j] == 1 for j in g[i])))
    return tuple(y)


def temporal(x, g, model):
    seen = {}; orbit = []
    while x not in seen:
        seen[x] = len(orbit)
        orbit.append(x)
        x = step(x, g, model)
    return seen[x], len(orbit)-seen[x], orbit

for k, seed in [(1, 2054), (2, 6)]:
    g=graph(k)
    a=temporal(digits(seed),g,'C')
    b=temporal(digits(seed),g,'H')
    assert (a[1], b[1]) == (1,5)
    assert a[2][-1] == tuple([2]*10)
    assert len(set(b[2][b[0]:])) == 5
    print('GP(5,%d) state %d CCA entry %d period %d GHM entry %d period %d' % (k,seed,a[0],a[1],b[0],b[1]))
print('DIRECT_WITNESS_OK')
