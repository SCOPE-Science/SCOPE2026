#!/usr/bin/env python3
"""Exhaustive four-state Greenberg-Hastings check on KG(5,2).

Requires only Python 3 standard library. Each of the 4**10 labelled states is
visited; integers encode states as two bits per lexicographically ordered pair.
"""
from array import array
from collections import Counter
from itertools import combinations, permutations

PAIRS = list(combinations(range(5), 2))
ADJ = [[j for j, p in enumerate(PAIRS) if not set(p).intersection(pair)]
       for pair in PAIRS]
assert len(PAIRS) == 10 and all(len(a) == 3 for a in ADJ)
N = 1 << 20


def build(threshold):
    f = array('I', [0]) * N
    for state in range(N):
        out = 0
        for v in range(10):
            c = (state >> (2*v)) & 3
            if c:
                new = (c+1) & 3
            else:
                excited = sum(((state >> (2*u)) & 3) == 1 for u in ADJ[v])
                new = int(excited >= threshold)
            out |= new << (2*v)
        f[state] = out
    return f


def check_threshold_one():
    f = build(1)
    recurring = bytearray(N)
    for start in range(N):
        y = start
        for _ in range(11):
            y = f[y]
        z = y
        for _ in range(20):
            z = f[z]
        assert y == z, (start, y, z)
        recurring[y] = 1
    periods = bytearray(N)
    cycle_set = set()
    for y in (i for i in range(N) if recurring[i]):
        if periods[y]:
            continue
        orbit = []
        z = y
        while not periods[z]:
            periods[z] = 255
            orbit.append(z)
            z = f[z]
        assert z == y
        assert len(orbit) in (1, 4, 5)
        for x in orbit:
            periods[x] = len(orbit)
        cycle_set.add(tuple(sorted(orbit)))
    assert sum(recurring) == 511
    count = Counter()
    most_delayed = []
    for s in range(N):
        t, y = 0, s
        while not recurring[y]:
            y = f[y]
            t += 1
            assert t <= 11
        p = periods[y]
        count[t, p] += 1
        if t == 11:
            most_delayed.append(s)
    cycles = Counter(len(c) for c in cycle_set)
    assert cycles == {1: 1, 4: 90, 5: 30}, cycles
    assert count[11, 4] == 1920 and sum(v for (t, p), v in count.items() if t == 11) == 1920
    assert sum(count.values()) == N

    maps = []
    for permutation in permutations(range(5)):
        maps.append(tuple(PAIRS.index(tuple(sorted(permutation[v] for v in pair)))
                          for pair in PAIRS))
    assert len(maps) == 120 and len(set(maps)) == 120

    def act(s, perm):
        x = 0
        for i, j in enumerate(perm):
            x |= ((s >> (2*i)) & 3) << (2*j)
        return x

    classes = Counter()
    reps = []
    while cycle_set:
        seed = min(cycle_set)
        orbit = {tuple(sorted(act(s, perm) for s in seed)) for perm in maps}
        assert orbit.issubset(cycle_set)
        cycle_set.difference_update(orbit)
        classes[len(seed), len(orbit)] += 1
        reps.append((len(seed), len(orbit), seed[0],
                     tuple((seed[0] >> (2*i)) & 3 for i in range(10))))
    assert classes == {(1, 1): 1, (4, 30): 1, (4, 60): 1, (5, 30): 1}, classes

    delayed = set(most_delayed)
    extremal = Counter()
    while delayed:
        seed = min(delayed)
        orb = {act(seed, perm) for perm in maps}
        assert orb.issubset(delayed)
        delayed.difference_update(orb)
        extremal[len(orb), 4] += 1
    assert extremal == {(120, 4): 16}, extremal
    print('threshold 1: F^31 = F^11 over all', N, 'states')
    print('primitive cycles:', dict(sorted(cycles.items())))
    print('cycle spatial symmetry classes:', dict(sorted(classes.items())))
    print('sample representatives:', sorted(reps))
    print('maximal first-entry time 11, states 1920; group classes:', dict(extremal))
    print('maximal-delay representative:', min(most_delayed), tuple((min(most_delayed) >> (2*i)) & 3 for i in range(10)))
    print('threshold 1 complete (time,period,count) table:')
    for (t,p),n in sorted(count.items()):
        print(t,p,n)
    return count


def check_threshold_two():
    f = build(2)
    counts = Counter()
    witness = None
    for start in range(N):
        x = start
        t = 0
        while x:
            x = f[x]
            t += 1
            assert t <= 5
        counts[t] += 1
        if t == 5 and witness is None:
            witness = start
    assert sum(counts.values()) == N
    assert [counts[i] for i in range(6)] == [1, 1023, 58025, 669622, 316165, 3740]
    print('threshold 2: F^5 is zero on all', N, 'states')
    print('time-to-zero counts:', [counts[i] for i in range(6)])
    print('threshold-2 five-update witness:', witness, tuple((witness >> (2*i)) & 3 for i in range(10)))


if __name__ == '__main__':
    check_threshold_one()
    check_threshold_two()
    print('ALL ASSERTIONS PASSED')
