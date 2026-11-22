#!/usr/bin/env python3
"""Finite exact checks supporting the local proof of golden-mean ECA injectivity."""
from itertools import product

NEIGHBORHOODS = (0, 1, 2, 4, 5)  # 000,001,010,100,101
GOOD_BASE = {4, 6, 7, 12, 13}
GOOD = GOOD_BASE | {31 - mask for mask in GOOD_BASE}

def local(rule, a, b, c):
    return (rule >> (4 * a + 2 * b + c)) & 1

def mask(rule):
    return sum(((rule >> p) & 1) << j for j, p in enumerate(NEIGHBORHOODS))

def bits(m):
    return tuple((m >> j) & 1 for j in range(5))

def criterion(m):
    a, b, c, d, e = bits(m)
    return c != e and not (b == c == d) and not (a == c and b == d)

def cyclic_good(w):
    n = len(w)
    return all(w[i] * w[(i + 1) % n] == 0 for i in range(n))

def image(rule, w):
    n = len(w)
    return tuple(local(rule, w[(i - 1) % n], w[i], w[(i + 1) % n]) for i in range(n))

def inverse_center(m, yl, yc, yr):
    complement = m not in GOOD_BASE
    if complement:
        yl, yc, yr = 1 - yl, 1 - yc, 1 - yr
        m = 31 - m
    if m == 4:
        return yc
    if m in (6, 7):
        return yc * (1 - yr)
    if m in (12, 13):
        return yc * (1 - yl)
    raise AssertionError("unlisted mask")

def first_pair(m):
    a, b, c, d, e = bits(m)
    if c == e:
        return (0, 1), (1, 0)
    if b == c == d:
        return (0, 0, 1), (0, 1, 0)
    if a == c and b == d:
        return (1, 0, 0, 0), (0, 0, 1, 0)
    raise AssertionError("expected noninjective mask")

assert len(GOOD) == 10
assert [m for m in range(32) if criterion(m)] == sorted(GOOD)
assert all(len([r for r in range(256) if mask(r) == m]) == 8 for m in range(32))

# Every possible five-site source window is covered, including boundary windows
# of every bi-infinite or periodic admissible source.
valid_five = [w for w in product((0, 1), repeat=5)
              if all(w[i] * w[i+1] == 0 for i in range(4))]
assert len(valid_five) == 13
for m in GOOD:
    rule = next(r for r in range(256) if mask(r) == m)
    for w in valid_five:
        y = [local(rule, w[i], w[i+1], w[i+2]) for i in range(3)]
        assert inverse_center(m, *y) == w[2], (m, w, y)

# All other local truth tables have explicit period <= 4 collisions.
for m in range(32):
    rule = next(r for r in range(256) if mask(r) == m)
    if m in GOOD:
        continue
    w, v = first_pair(m)
    assert cyclic_good(w) and cyclic_good(v) and w != v
    assert image(rule, w) == image(rule, v), (m, w, v)

# Exhaustive independent periodic map comparison for moderate ring lengths.
for n in range(1, 13):
    words = [w for w in product((0,1), repeat=n) if cyclic_good(w)]
    for m in range(32):
        rule = next(r for r in range(256) if mask(r) == m)
        yy = [image(rule, w) for w in words]
        injective = len(yy) == len(set(yy))
        if m in GOOD:
            assert injective, (n, m)
        if n >= 4 and m not in GOOD and n % len(first_pair(m)[0]) == 0:
            assert not injective, (n, m)

# The four-site bound is sharp; short cycles cannot refute either witness.
for m in (5, 26):
    rule = next(r for r in range(256) if mask(r) == m)
    for n in (1, 2, 3):
        words = [w for w in product((0,1), repeat=n) if cyclic_good(w)]
        assert len({image(rule, w) for w in words}) == len(words)
    p, q = first_pair(m)
    assert len(p) == 4 and image(rule, p) == image(rule, q)

# No radius-zero inverse works in any of the other eight good mask classes.
for m in GOOD:
    rule = next(r for r in range(256) if mask(r) == m)
    relation = {(local(rule, w[0], w[1], w[2]), w[1])
                for w in product((0,1), repeat=3)
                if w[0]*w[1] == 0 and w[1]*w[2] == 0}
    zero_radius = all(len({x for y,x in relation if y == z}) == 1
                      for z in (0,1))
    assert zero_radius == (m in (4, 27)), m

print("PASS: 32 effective rules, 10 injective masks, 80 of 256 ECA;")
print("PASS: 13-window universal radius-one inverses; 22 explicit <=4-period collisions;")
print("PASS: sharp period-four examples 5/26; radius-zero exactly 16 rules;")
print("PASS: independently enumerated indexed periodic rings n=1..12.")
