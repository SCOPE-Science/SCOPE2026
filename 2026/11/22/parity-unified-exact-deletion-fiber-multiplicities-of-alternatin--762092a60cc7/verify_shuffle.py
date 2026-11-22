"""Independent dynamic shuffle-count regression for alternating-prefix deletion fibers.

Run: python3 verify_shuffle.py
Uses only Python's standard library.
"""
from functools import lru_cache
from itertools import product
from math import comb
import random


def alt(n):
    return ''.join('01'[i % 2] for i in range(n))


def shuffle_count(source, removed, retained):
    # Counts disjoint interleavings of two specified words matching the source.
    @lru_cache(None)
    def dp(i, j):
        q = i + j
        if q == len(source):
            return int(i == len(removed) and j == len(retained))
        ans = 0
        if i < len(removed) and removed[i] == source[q]:
            ans += dp(i + 1, j)
        if j < len(retained) and retained[j] == source[q]:
            ans += dp(i, j + 1)
        return ans
    return dp(0, 0)


def predicted(n, d, bits):
    r = n-d
    ell = r//2
    p = d%2
    assert len(bits) == ell
    v = ''.join('10' if c else '01' for c in bits) + (str(p) if r%2 else '')
    chain = (0,) + tuple(bits) + (p,)
    switches = sum(chain[j] != chain[j+1] for j in range(ell+1))
    mult = comb(ell + (d-switches)//2, ell) if switches <= d else 0
    return v, switches, mult


def main():
    cases = 0
    counted = 0
    histogram_bins = 0
    for n in range(23):
        w = alt(n)
        for d in range(n+1):
            u = alt(d)
            ell = (n-d)//2
            hist = {}
            for bits in product((0,1),repeat=ell):
                v,t,expect = predicted(n,d,bits)
                got = shuffle_count(w,u,v)
                assert got == expect, (n,d,bits,t,got,expect)
                if got:
                    hist[t] = hist.get(t,0) + 1
                counted += got
                cases += 1
            p=d%2
            for t in range(p,min(d,ell+1)+1,2):
                assert hist.get(t,0) == comb(ell+1,t), (n,d,t,hist)
                histogram_bins += 1
    rng = random.Random(271828)
    sampled = 0
    for _ in range(500):
        n = rng.randint(24,100)
        d = rng.randint(0,n)
        ell=(n-d)//2
        bits=tuple(rng.randrange(2) for _ in range(ell))
        v,t,expect=predicted(n,d,bits)
        got=shuffle_count(alt(n),alt(d),v)
        assert got == expect,(n,d,t,got,expect)
        sampled+=1
    print('VERIFY_SHUFFLE_OK n=0..22 cases=%d histogram_bins=%d total_count=%d extra_samples=%d' % (cases,histogram_bins,counted,sampled))


if __name__=='__main__':
    main()
