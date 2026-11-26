#!/usr/bin/env python3
"""Exact local-bound certificate and explicit orientable-cycle verification."""
from collections import Counter
from itertools import product

W = "0001231333032331222023231031212302232132212013301220113130302131002113020210230112101300201030010111320332"
Q = tuple(range(4))
assert len(W) == 106 and set(W) == set("0123")
windows = [tuple(int(W[(i+j) % len(W)]) for j in range(4)) for i in range(len(W))]
assert len(set(windows)) == 106
assert all(e != e[::-1] for e in windows)
assert set(windows).isdisjoint({e[::-1] for e in windows})
print("WITNESS length=106 unique_windows=106 reversed_collisions=0 palindromes=0")

def h(t):
    a, b, c = t
    return int(a == b and b != c) - int(a != b and b == c)

def lam(e):
    a, b, c, d = e
    if a != b and b != c and c != d:
        return 1
    if b == c and len({a, b, d}) == 3:
        return 3
    return 0

def uniform_charge(e):
    a, b, c, d = e
    return 2 if (a == b == c != d or a != b == c == d) else 0

table = Counter()
orbits = {}
for e in product(Q, repeat=4):
    if e == e[::-1]:
        continue
    a, b, c, d = e
    L = lam(e)
    U = uniform_charge(e)
    D = h((a,b,c)) - h((b,c,d))
    assert L + U + D >= 1, (e, L, U, D)
    table[L, U, D, L + U + D] += 1
    orbits[min(e,e[::-1])] = L
assert sum(table.values()) == 240
expected = Counter({(1,0,0,1):108,(0,0,1,1):72,(0,2,-1,1):24,(3,0,-2,1):24,(0,0,2,2):12})
assert table == expected, (table, expected)
assert Counter(orbits.values()) == Counter({0:54,1:54,3:12})
assert len(orbits) == 120
# Independently test the balanced degree at the four uniform triple vertices.
selected = set(windows)
for a in Q:
    outgoing = sum((a,a,a,b) in selected for b in Q if b != a)
    incoming = sum((b,a,a,a) in selected for b in Q if b != a)
    assert outgoing == incoming and outgoing <= 1
# Independently test the complete flow cancellation for the actual witness.
balance = Counter()
for e in windows:
    balance[e[:3]] += 1
    balance[e[1:]] -= 1
assert all(value == 0 for value in balance.values())
upper = sum(orbits.values()) + 2*(4*2)
assert upper == 106
print("LOCAL_CERTIFICATE nonpal_words=240 cases=5 reversal_orbits=120 weight_budget=90 uniform_budget=16")
print("UPPER_BOUND 106")
print("VERIFY_OK")
