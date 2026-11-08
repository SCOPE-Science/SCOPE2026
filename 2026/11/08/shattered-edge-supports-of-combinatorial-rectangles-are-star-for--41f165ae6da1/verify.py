"""Finite cross-checks for Cartesian rectangle shattering and online depth.
Python 3, standard library only.  Run: python verify.py
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb


def hypotheses(p, q):
    h = {0}
    for a in range(1, 1 << p):
        for b in range(1, 1 << q):
            h.add(sum(1 << (i * q + j) for i in range(p) for j in range(q)
                      if a & (1 << i) and b & (1 << j)))
    return sorted(h)


def star_forest(s, p, q):
    dr = [0] * p
    dc = [0] * q
    for i in range(p):
        for j in range(q):
            if (s >> (i*q+j)) & 1:
                dr[i] += 1
                dc[j] += 1
    return all(dr[i] == 1 or dc[j] == 1 for i in range(p)
               for j in range(q) if s & (1 << (i*q+j)))


def direct_shatters(s, h):
    return len({x & s for x in h}) == (1 << s.bit_count())


def online_depth(p, q):
    h = hypotheses(p,q)
    full = (1 << len(h)) - 1
    queries = [sum(1 << idx for idx, x in enumerate(h) if x & (1 << k))
               for k in range(p*q)]

    @lru_cache(None)
    def recur(mask):
        if mask.bit_count() <= 1:
            return 0
        return max([1 + min(recur(mask & t), recur(mask & (full ^ t)))
                    for t in queries if mask & t and mask & (full ^ t)] or [0])
    return recur(full)


@lru_cache(None)
def species_recurrence(p, q):
    # Labelled-set exponential-formula coefficient recurrence,
    # conditioned on the component containing the first left vertex.
    if p == 0:
        return (1,)
    out = Counter({k: v for k, v in enumerate(species_recurrence(p - 1, q))})
    for j in range(1, q + 1):
        for k, coeff in enumerate(species_recurrence(p - 1, q - j)):
            out[k + j] += comb(q, j) * coeff
    for t in range(2, p + 1):
        for k, coeff in enumerate(species_recurrence(p - t, q - 1)):
            out[k + t] += q * comb(p - 1, t - 1) * coeff
    while out and out[max(out)] == 0:
        del out[max(out)]
    return tuple(out[k] for k in range(max(out) + 1))


def run():
    tests = 0
    hist = {}
    for p, q in product(range(1,5), repeat=2):
        # exhaustively check even the full 4x4 edge set
        h = hypotheses(p,q)
        counts = Counter()
        for s in range(1 << (p*q)):
            sf = star_forest(s,p,q)
            yes = direct_shatters(s,h)
            assert sf == yes, (p,q,s,sf,yes)
            if sf: counts[s.bit_count()] += 1
            tests += 1
        hist[p,q] = counts
        assert tuple(counts[k] for k in range(max(counts)+1)) == species_recurrence(p,q), (p,q)
        assert max(counts) == (max(p,q) if min(p,q)==1 else p+q-2)
        if p == 2:
            assert all(counts[k] == comb(q,k)*(2**k) + (q if k==2 else 0)
                       for k in range(q+1)), (p,q,counts)
        print('SHATTER',p,q,tuple(counts[k] for k in range(max(counts)+1)))
    rank_checks=0
    for p,q in [(1,i) for i in range(1,6)] + [(2,i) for i in range(2,5)] + [(3,3),(3,4)]:
        assert online_depth(p,q) == p+q-1,(p,q)
        rank_checks += 1
    print('CARTESIAN_RECTANGLES_PASS',tests,'supports',rank_checks,'online_ranks')

if __name__=='__main__': run()
