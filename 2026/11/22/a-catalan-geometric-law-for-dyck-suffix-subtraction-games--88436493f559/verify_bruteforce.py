"""Direct finite exhaustive check for the Dyck-suffix word game. Python 3 stdlib."""
from functools import lru_cache
from itertools import product
from collections import Counter
from math import comb

@lru_cache(None)
def is_dyck(s):
    if not s: return False
    h = 0
    for a in s:
        h += 1 if a == 'a' else -1
        if h < 0: return False
    return h == 0

@lru_cache(None)
def value(w):
    opts = {value(w[:j]) for j in range(len(w)) if is_dyck(w[j:])}
    mex = 0
    while mex in opts: mex += 1
    return mex

def canonical(w):
    # Longest suffix belonging to the Dyck language.
    ix = next((j for j in range(len(w)) if is_dyck(w[j:])), len(w))
    suffix = w[ix:]
    h = 0
    k = 0
    for a in suffix:
        h += 1 if a == 'a' else -1
        if h == 0: k += 1
    return w[:ix], k

def strict_low(w):
    h = 0
    low = 0
    for a in w[:-1]:
        h += 1 if a == 'a' else -1
        low = min(low,h)
    last = h + (1 if w and w[-1] == 'a' else -1)
    return bool(w and w[-1]=='b' and last < low)

checked = 0
for n in range(13):
    hist = Counter()
    extremizers = []
    for x in product('ab', repeat=n):
        w = ''.join(x)
        g = value(w)
        u, k = canonical(w)
        assert g == k, (w, g, k)
        assert (g == 0) == (not w or w[-1]=='a' or strict_low(w)), w
        if not w or n <= 1:
            pass
        if n > 0 and g == n//2: extremizers.append(w)
        hist[g] += 1
        checked += 1
    assert sum(hist.values()) == 2**n
    if n == 0: expected_zero = 1
    else: expected_zero = 2**(n-1) + comb(n-1, (n-1)//2)
    assert hist[0] == expected_zero, (n,hist[0],expected_zero)
    assert max(hist) == n//2
    if n >= 2:
        expected_ext = ['ab'*(n//2)] if n%2==0 else [c+'ab'*(n//2) for c in 'ab']
        assert sorted(extremizers) == sorted(expected_ext)
    print(f'n={n}: '+','.join(f'{k}:{hist[k]}' for k in sorted(hist)))
print('PASS checked_words=',checked,'cached_positions=',value.cache_info().currsize)
