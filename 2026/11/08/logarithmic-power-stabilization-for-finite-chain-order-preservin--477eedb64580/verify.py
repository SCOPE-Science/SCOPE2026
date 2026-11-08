"""Finite checks for fixed-interval coding and stabilization depth.

Run with Python 3 and the standard library: python verify.py
These are finite checks, not a substitute for the asymptotic proof.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, log2
from random import Random


def weak_maps(n):
    for steps in product((0, 1), repeat=n-1):
        for start in range(1, n-sum(steps)+1):
            f = [start]
            for step in steps:
                f.append(f[-1]+step)
            yield tuple(f)


def power_depth(f):
    n = len(f)
    g = tuple(range(1, n+1))
    for t in range(n+1):
        h = tuple(f[i-1] for i in g)
        if h == g:
            return t
        g = h
    raise AssertionError('No stabilization')


def fixed_interval(f):
    fixed = [i+1 for i, v in enumerate(f) if i+1 == v]
    assert fixed and fixed == list(range(fixed[0], fixed[-1]+1))
    return fixed[0], fixed[-1]


def depth_from_tail(f):
    a, b = fixed_interval(f)
    n = len(f)
    def left_depth():
        L = a-1
        S = [0] * (L+1)
        # For h>=2, f(a-h) differs from f(a-h+1) by 0 or 1.
        for h in range(2, L+1):
            S[h-1] = S[h-2] + f[a-h] - f[a-h-1]
        h, steps = L, 0
        while h:
            h = S[h-1]
            steps += 1
        return steps
    def right_depth():
        R = n-b
        S = [0] * (R+1)
        for h in range(2, R+1):
            S[h-1] = S[h-2] + f[b+h-1] - f[b+h-2]
        h, steps = R, 0
        while h:
            h = S[h-1]
            steps += 1
        return steps
    return max(left_depth(), right_depth())


def maps_with_fixed_interval(n, a, b):
    L, R = a-1, n-b
    for lb in product((0,1), repeat=max(0,L-1)):
        for rb in product((0,1), repeat=max(0,R-1)):
            f = [None] * n
            for i in range(a,b+1): f[i-1] = i
            if L:
                f[a-2] = a
                for j, step in enumerate(lb):
                    idx = a-3-j
                    f[idx] = f[idx+1] - step
            if R:
                f[b] = b
                for j, step in enumerate(rb):
                    idx = b+1+j
                    f[idx] = f[idx-1] + step
            yield tuple(f)


def known_joint_count(n, k, rank):
    if k == n:
        return int(rank == n)
    m, j = n-k-1, rank-k
    return (n-rank+1)*comb(m,j) if 0 <= j <= m else 0

for n in range(1, 11):
    maps = list(weak_maps(n))
    distribution = Counter()
    by_interval = defaultdict(set)
    for f in maps:
        assert len(f) == n and all(1 <= y <= n for y in f)
        assert all(f[i+1]-f[i] in (0,1) for i in range(n-1))
        a,b = fixed_interval(f)
        by_interval[a,b].add(f)
        assert depth_from_tail(f) == power_depth(f), (n, f)
        distribution[b-a+1, len(set(f))] += 1
    target_total = 1 if n == 1 else (n+1)*2**(n-2)
    assert len(maps) == target_total, (n,len(maps))
    for k in range(1,n+1):
        for r in range(k,n+1):
            assert distribution[k,r] == known_joint_count(n,k,r), (n,k,r)
    if n <= 8:
        for a in range(1,n+1):
            for b in range(a,n+1):
                coded = set(maps_with_fixed_interval(n,a,b))
                assert coded == by_interval[a,b], (n,a,b)
                assert len(coded) == 2**(max(0,a-2)+max(0,n-b-1))
    print('EXHAUSTIVE_OK',n,'maps',len(maps), 'depths',dict(Counter(power_depth(f) for f in maps)))

# The next check is a numerical diagnostic, not a proof of convergence.
rng = Random(107)
for t in (100, 1000, 10000):
    observed=[]
    for _ in range(100):
        L=t//2; R=t-L
        depths=[]
        for s in (L,R):
            pref=[0]
            for j in range(s-1):
                pref.append(pref[-1]+rng.randrange(2))
            h=s; depth=0
            while h:
                h=pref[h-1]
                depth += 1
            depths.append(depth)
        observed.append(max(depths))
    print('DIAGNOSTIC',t,'mean ratio',round(sum(observed)/len(observed)/log2(t),6))
print('VERIFY_OK')
