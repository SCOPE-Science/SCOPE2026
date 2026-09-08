#!/usr/bin/env python3
"""Exhaustive antichain / monotone Boolean function census for B4, scalable to B5.
Stdlib only. Deterministic.
"""
import itertools, json, hashlib, time, sys

def subsets_of_n(n):
    return list(range(1 << n))

def comparable(a, b):
    return (a & b) == a or (a & b) == b  # a<=b or b<=a as bitmasks

def is_antichain(fam):
    L = list(fam)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if comparable(L[i], L[j]):
                return False
    return True

def brute_force_antichains(n):
    """Brute force over all subsets of powerset (only feasible n<=4)."""
    N = 1 << n
    elems = list(range(N))
    out = []
    for mask in range(1 << N):
        fam = tuple(e for e in elems if (mask >> e) & 1)
        if is_antichain(fam):
            out.append(fam)
    return out

def independent_set_antichains(n):
    """Branch-and-bound enumeration of all independent sets of comparability graph.
    Works for n=5 (32 vertices) easily. Deterministic order."""
    N = 1 << n
    # neighbor sets (strict comparability, excluding self)
    nbr = []
    for i in range(N):
        s = set()
        for j in range(N):
            if i != j and comparable(i, j):
                s.add(j)
        nbr.append(s)
    out = []
    # order vertices 0..N-1; recursive with candidate list
    sys.setrecursionlimit(10000)
    def rec(cand, chosen):
        if not cand:
            out.append(tuple(sorted(chosen)))
            return
        v = cand[0]
        rest = cand[1:]
        # branch exclude v
        rec(rest, chosen)
        # branch include v: remove v and its neighbors from candidates
        forbid = nbr[v]
        rest2 = [u for u in rest if u not in forbid]
        rec(rest2, chosen + [v])
    rec(list(range(N)), [])
    return out

def antichain_to_truth(fam, n):
    N = 1 << n
    s = set(fam)
    t = 0
    for x in range(N):
        v = 0
        for a in s:
            if (a & x) == a:
                v = 1
                break
        if v:
            t |= (1 << x)
    return t

def truth_to_minimal(truth, n):
    N = 1 << n
    ones = [x for x in range(N) if (truth >> x) & 1]
    mins = []
    for x in ones:
        if not any((y != x and (y & x) == y) for y in ones):
            mins.append(x)
    return tuple(sorted(mins))

def dual_truth(truth, n):
    N = 1 << n
    ALL = N - 1
    d = 0
    for x in range(N):
        fx = (truth >> x) & 1
        # f^d(x) = not f(not x); not x = ALL ^ x
        v = 1 - ((truth >> (ALL ^ x)) & 1)
        if v:
            d |= (1 << x)
    return d

def popcount(x):
    return bin(x).count("1")

if __name__ == "__main__":
    t0 = time.time()
    ac4 = brute_force_antichains(4)
    t1 = time.time()
    print("B4 brute force count:", len(ac4), "time %.2fs" % (t1-t0))
    ac4b = independent_set_antichains(4)
    print("B4 branch count:", len(ac4b))
    assert len(ac4b) == len(ac4)
    assert set(ac4b) == set(ac4)
    # Dedekind recursion cross-check: pairs (f0,f1) of MBF(n-1) with f0<=f1
    # MBF(3): enumerate first
    ac3 = brute_force_antichains(3)
    print("B3 count:", len(ac3))  # expect 20
    assert len(ac3) == 20
    truths3 = [antichain_to_truth(a, 3) for a in ac3]
    # f0<=f1 means truth(f0)|truth(f1)==truth(f1)
    cnt = sum(1 for a in truths3 for b in truths3 if (a | b) == b)
    print("Dedekind recursion D4 from D3 pairs:", cnt)
    assert cnt == 168
    # truths for n=4
    truths4 = sorted(antichain_to_truth(a, 4) for a in ac4)
    assert len(set(truths4)) == 168
    # spot check roundtrip
    for a in ac4:
        assert truth_to_minimal(antichain_to_truth(a, 4), 4) == tuple(sorted(a))
    print("roundtrip OK")
    # self-dual count
    sd = [t for t in truths4 if dual_truth(t, 4) == t]
    print("self-dual count n=4:", len(sd))
    for t in sd[:5]:
        print("  sd truth", t, "min", truth_to_minimal(t, 4))
