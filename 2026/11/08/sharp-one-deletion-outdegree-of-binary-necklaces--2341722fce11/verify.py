"""Finite regression for a sharp cyclic one-deletion descendant theorem.

Run: python verify.py
This program checks finite samples; the mathematical proof establishes all n.
"""
from itertools import product


def necklace(s):
    if not s:
        return s
    return min(s[i:]+s[:i] for i in range(len(s)))


def descendants(s):
    return {necklace(s[:i]+s[i+1:]) for i in range(len(s))}


def cyclic_runs(s):
    if len(set(s)) <= 1:
        return 1
    return sum(s[i] != s[i-1] for i in range(len(s)))


def predicted(n):
    if n == 1:
        return 1
    if n in (2, 3):
        return 2
    return n - 2 - int(n >= 9 and n % 2 == 1)


def construction(n):
    assert n >= 4
    if n % 2 == 0:
        return '00' + '10' * (n // 2 - 2) + '11'
    if n >= 9:
        return '000' + '10' * ((n - 1) // 2 - 2) + '11'
    if n == 5:
        return '00101'
    if n == 7:
        return '0010101'
    raise ValueError(n)


checked = 0
for n in range(1, 16):
    counts = {}
    for t in product('01', repeat=n):
        s = ''.join(t)
        if necklace(s) != s:
            continue
        value = len(descendants(s))
        if n > 1:
            assert value <= cyclic_runs(s)
        counts[s] = value
        assert value <= predicted(n), (n, s, value, predicted(n))
        checked += 1
    actual = max(counts.values())
    assert actual == predicted(n), (n,actual,predicted(n))
    if n >= 4:
        witness = construction(n)
        assert len(witness) == n
        assert len(descendants(witness)) == predicted(n)

for n in range(4, 301):
    if n % 2 == 1 and n < 9:
        continue
    s = construction(n)
    assert len(descendants(s)) == predicted(n), (n, len(descendants(s)))

# Cross-check equivalence under deletion from all choices of source rotation.
for s in ('00110101', '00010101011', '00101010101', '000101011', '0011011011'):
    ground = descendants(s)
    for offset in range(len(s)):
        sr = s[offset:] + s[:offset]
        assert descendants(sr) == ground
print(f'VERIFY_OK necklace_classes={checked} exhaustive_n=1..15 witnesses_n=4..300')
