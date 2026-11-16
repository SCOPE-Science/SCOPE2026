"""Exact integer tests for cycle independent-set Walsh convolution."""
from itertools import product
from collections import Counter

IDENTITY = (1, 0, 0, 1)

def matmul(a, b):
    x, y, z, t = a
    u, v, w, h = b
    return (x*u + y*w, x*v + y*h, z*u + t*w, z*v + t*h)

def transfer(signs):
    p = IDENTITY
    for s in signs:
        p = matmul(p, (1, 1, s, 0))
    return p

def walsh_transfer(signs):
    a, b, c, d = transfer(signs)
    return a + d

def walsh_dp(signs):
    # Two independently accumulated possibilities for whether site zero is occupied.
    a, b, c, d = 1, 0, 0, signs[0]
    for s in signs[1:]:
        a, b, c, d = a+b, s*a, c+d, s*c
    return a+b+c

def walsh_bruteforce(signs):
    n = len(signs)
    total = 0
    for mask in range(1 << n):
        if any((mask & (1 << i)) and (mask & (1 << ((i+1) % n))) for i in range(n)):
            continue
        p = 1
        for i in range(n):
            if mask & (1 << i):
                p *= signs[i]
        total += p
    return total

def word(s):
    return tuple(1 if t == '+' else -1 for t in s)

SCALAR_WORDS = ['+--+--', '-+--+-', '--+--+', '------']
TRACENULL_WORDS = ['--+', '-+-', '+--']
for w in SCALAR_WORDS:
    assert transfer(word(w)) == IDENTITY, w
for w in TRACENULL_WORDS:
    assert walsh_transfer(word(w)) == 0, w
assert walsh_transfer(word('--+---')) == 0

counts = {}
for n in range(3, 17):
    hist = Counter()
    for bits in range(1 << n):
        s = tuple(1 - 2 * ((bits >> i) & 1) for i in range(n))
        a = walsh_dp(s)
        assert a == walsh_transfer(s), (n, bits)
        if n <= 9:
            assert a == walsh_bruteforce(s), (n, bits)
        hist[a] += 1
    expected_min = 1 if n % 3 else 2
    assert min(abs(v) for v in hist if v) == expected_min, n
    assert (hist[0] == 0) == (n % 3 != 0), n
    assert (0 in hist) == (n % 3 == 0), n
    assert hist[walsh_transfer((1,) * n)] >= 1
    counts[n] = hist[0]
print('EXACT_COUNTS', counts)
for n in range(3, 102):
    if n % 3 == 0:
        suffix = '--+' if n % 6 == 3 else '--+---'
        suffix += '------' * ((n - len(suffix)) // 6)
        assert len(suffix) == n
        assert walsh_transfer(word(suffix)) == 0
        assert walsh_transfer(word('-' * n)) in (-2, 2)
    else:
        assert walsh_transfer(word('-' * n)) in (-1, 1)
print('CHECKS_PASS')
