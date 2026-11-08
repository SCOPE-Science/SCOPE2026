#!/usr/bin/env python3
"""Exact checks of the three-alternative simultaneous-elimination Baldwin rule.

Run: python3 verify.py
Pure Python 3 standard library. No third-party dependencies or saved data.
"""
from itertools import permutations
from collections import Counter
from math import comb

BALLOTS = tuple(permutations(range(3)))
B = tuple(tuple(2 - ballot.index(j) for j in range(3)) for ballot in BALLOTS)
V = tuple(tuple(tuple(int(ballot.index(i) < ballot.index(j)) for j in range(3)) for i in range(3)) for ballot in BALLOTS)

def profiles(total, k=6):
    if k == 1:
        yield (total,)
        return
    for n in range(total + 1):
        for rest in profiles(total - n, k - 1):
            yield (n,) + rest

def scores(c):
    return tuple(sum(c[b] * B[b][j] for b in range(6)) for j in range(3))

def margin(c, i, j):
    return sum(c[b] * (2*V[b][i][j] - 1) for b in range(6))

def winner(c):
    ss = scores(c)
    losers = [i for i in range(3) if ss[i] == min(ss)]
    if len(losers) == 3:
        return None
    if len(losers) == 2:
        return next(i for i in range(3) if i not in losers)
    remaining = [i for i in range(3) if i != losers[0]]
    m = margin(c, *remaining)
    return remaining[0] if m > 0 else remaining[1] if m < 0 else None

def predicted(c, ballot):
    a,b,d = BALLOTS[ballot]
    sa,sb,sd = (scores(c)[i] for i in (a,b,d))
    t1 = sb == sa+1 and sd >= sa+3 and margin(c,b,d) > 0
    t2 = sb == sd and sb < sa and margin(c,b,a) >= 2
    return int(t1) + 2*int(t2)

def outcome(c, ballot):
    before = winner(c)
    new = list(c)
    new[ballot] += 1
    after = winner(new)
    if before is None or after is None:
        return False
    rank = BALLOTS[ballot]
    return rank.index(before) < rank.index(after)

checks = 0
counts = Counter()
unique = {}
for n in range(0, 18):
    events=[]
    for c in profiles(n):
        for t in range(6):
            truth = outcome(c,t)
            classification = predicted(c,t)
            assert truth == bool(classification), (n,c,BALLOTS[t],truth,classification)
            checks += 1
            if truth:
                events.append((c,t,classification))
    counts[n] = len(events)
    if n in (11,12):
        unique[n] = events
assert all(counts[n] == 0 for n in range(11))
assert counts[11] == 6 and {e[2] for e in unique[11]} == {1}
assert counts[12] == 6 and {e[2] for e in unique[12]} == {2}

# Canonical 11-voter witness and its full symmetric orbit.
base = (2,0,0,4,5,0)
assert BALLOTS[0] == (0,1,2)
assert winner(base) == 1 and scores(base) == (9,10,14)
with_vote = (3,0,0,4,5,0)
assert winner(with_vote) == 2 and scores(with_vote) == (11,11,14)
orb = set()
for sigma in permutations(range(3)):
    moved = [0]*6
    for t, r in enumerate(BALLOTS):
        rr = tuple(sigma[j] for j in r)
        moved[BALLOTS.index(rr)] = base[t]
    new_ballot = BALLOTS.index(tuple(sigma[j] for j in BALLOTS[0]))
    orb.add((tuple(moved),new_ballot))
assert len(orb) == 6
assert orb == {(c,t) for c,t,_ in unique[11]}
print('EXACT CHECKS:', checks)
print('COUNTS (initial voters 0..17):', dict(counts))
print('UNIQUE 11-VOTER EVENTS:', len(unique[11]), 'one orbit')
print('FIRST SECOND-TYPE 12-VOTER EVENT:', unique[12][0])
print('CANONICAL 11-VOTER SCORES:', scores(base), 'AFTER:', scores(with_vote))
print('VERIFIED: all classification comparisons, 12-voter sharpness and one orbit')
