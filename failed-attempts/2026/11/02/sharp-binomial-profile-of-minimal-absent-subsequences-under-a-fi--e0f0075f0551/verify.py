#!/usr/bin/env python3
"""Elementary independent checks for fixed-content minimal absent subsequences.

Usage: python verify.py
Requires only Python 3 and its standard library.
Finite enumeration is a consistency check, not a proof of the infinite theorem.
"""
from itertools import combinations, product
from math import comb


def embeds(u, w):
    i = 0
    for c in w:
        if i < len(u) and c == u[i]:
            i += 1
    return i == len(u)


def brute_minimal_absents(w):
    # Generate every subsequence, then all one-letter minimal extensions.
    present = {""}
    for ch in w:
        present |= {s + ch for s in tuple(present)}
    candidates = set()
    for s in present:
        for i in range(len(s) + 1):
            for ch in "01":
                u = s[:i] + ch + s[i:]
                if u not in present:
                    candidates.add(u)
    return {
        u for u in candidates
        if all(u[:j] + u[j+1:] in present for j in range(len(u)))
    }


def greedy_one_indices(u, w):
    # Indices among source ones, not absolute positions.
    q, ones, chosen = 0, 0, []
    for ch in u:
        while q < len(w) and w[q] != ch:
            if w[q] == "1":
                ones += 1
            q += 1
        if q == len(w):
            raise ValueError("input is not a subsequence")
        if ch == "1":
            ones += 1
            chosen.append(ones)
        q += 1
    return tuple(chosen)


def reconstruct_from_one_indices(w, indices, terminal):
    a = [len(z) for z in w.split("1")]
    k = len(a)-1
    z, prev = [], 0
    for j in indices:
        if prev == 0:
            z.append(0 if j == 1 else sum(a[:j-1]) + 1)
        else:
            z.append(0 if j == prev + 1 else sum(a[prev:j-1]) + 1)
        prev = j
    if terminal == "0":
        z.append(sum(a[prev:]))
    else:
        z.append(0 if prev == k else sum(a[prev:k]) + 1)
    return "".join("0"*z[j] + "1" for j in range(len(indices))) + "0"*z[-1] + terminal


def extremal_candidate(k, indices, terminal):
    # Direct formula for source (010)^k. This does not enumerate MAS.
    z, prev = [], 0
    for j in indices:
        if prev == 0:
            z.append(2*(j-1))
        else:
            z.append(0 if j == prev+1 else 2*(j-prev)-1)
        prev = j
    if terminal == "0":
        z.append(2*k if prev == 0 else 2*(k-prev)+1)
    else:
        z.append(0 if prev == k else (2*(k-prev)+1 if prev else 2*k))
    return "".join("0"*z[j] + "1" for j in range(len(indices))) + "0"*z[-1] + terminal


def main():
    trials = 0
    for n in range(1, 12):
        for bits in product("01", repeat=n):
            w = "".join(bits)
            k = w.count("1")
            mas = brute_minimal_absents(w)
            for r in range(k+2):
                assert sum(u.count("1") == r for u in mas) <= comb(k+1, r), (w,r)
            codewords = set()
            for v in mas:
                assert not embeds(v,w)
                assert all(embeds(v[:j]+v[j+1:],w) for j in range(len(v)))
                I = greedy_one_indices(v[:-1],w)
                assert v == reconstruct_from_one_indices(w,I,v[-1]), (w,v,I)
                assert (I,v[-1]) not in codewords
                codewords.add((I,v[-1]))
            trials += 1
    for k in range(1, 10):
        w = "010"*k
        found = set()
        counts = [0]*(k+2)
        for s in range(k+1):
            for I in combinations(range(1,k+1),s):
                for terminal in "01":
                    v = extremal_candidate(k,I,terminal)
                    assert v not in found, (k,I,terminal,v)
                    assert not embeds(v,w), (k,I,terminal,v)
                    assert all(embeds(v[:j]+v[j+1:],w) for j in range(len(v))), (k,I,terminal,v)
                    assert greedy_one_indices(v[:-1],w) == I, (k,I,terminal,v)
                    found.add(v)
                    counts[v.count("1")] += 1
        assert counts == [comb(k+1,r) for r in range(k+2)], (k,counts)
        assert len(found) == 2**(k+1)
        if k <= 3:
            assert found == brute_minimal_absents(w)
    print("VERIFY_OK binary_words=4094 witness_k=1..9 canonical_injection=checked")


if __name__ == "__main__":
    main()
