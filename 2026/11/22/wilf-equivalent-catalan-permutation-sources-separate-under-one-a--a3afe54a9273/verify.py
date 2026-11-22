#!/usr/bin/env python3
"""Exact finite certificates for one adjacent-transposition correction in Catalan permutation sources.

Run: python3 verify.py (requires certificates.json alongside this program).
Only Python's standard library is used.
"""
from itertools import permutations
from fractions import Fraction
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def word_set(n, forbidden):
    forbidden = tuple(int(d)-1 for d in forbidden)
    ans = []
    for p in permutations(range(n)):
        if not any(tuple(sorted((p[i], p[j], p[k])).index(x) for x in (p[i],p[j],p[k])) == forbidden
                   for i in range(n) for j in range(i+1,n) for k in range(j+1,n)):
            ans.append(''.join(str(x+1) for x in p))
    return ans


def received(w):
    out = {w}
    for i in range(len(w)-1):
        a = list(w)
        a[i], a[i+1] = a[i+1], a[i]
        out.add(''.join(a))
    return out


def kendall_distance(u, v):
    pos = {a:i for i,a in enumerate(v)}
    a = [pos[x] for x in u]
    return sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1,len(a)))


def compatibility(words):
    balls = [received(w) for w in words]
    edges = [0]*len(words)
    for i in range(len(words)):
        for j in range(i):
            disjoint = balls[i].isdisjoint(balls[j])
            assert disjoint == (kendall_distance(words[i],words[j]) >= 3)
            if disjoint:
                edges[i] |= 1 << j
                edges[j] |= 1 << i
    return edges, balls


def maximal_cliques(adj):
    n = len(adj)
    results = Counter()
    best = ()
    def go(R, P, X):
        nonlocal best
        if not (P | X):
            results[len(R)] += 1
            if len(R) > len(best) or (len(R) == len(best) and R < best):
                best = R
            return
        union = P | X
        # Pivot minimizes the number of non-neighbors in P.
        pivot = max((i for i in range(n) if union >> i & 1),
                    key=lambda i: (P & adj[i]).bit_count())
        todo = P & ~adj[pivot]
        while todo:
            low = todo & -todo
            v = low.bit_length()-1
            todo ^= low
            go(R+(v,), P & adj[v], X & adj[v])
            P &= ~low
            X |= low
    go((), (1 << n)-1, 0)
    return len(best), results[len(best)], best


def fixed_size_count(adj, k):
    # An independent k-clique enumeration by increasing vertex index.
    n = len(adj)
    def rec(candidates, need):
        if need == 0:
            return 1
        if candidates.bit_count() < need:
            return 0
        total = 0
        while candidates.bit_count() >= need:
            low = candidates & -candidates
            v = low.bit_length()-1
            candidates ^= low
            total += rec(candidates & adj[v], need-1)
        return total
    return rec((1 << n)-1, k)


def cert_check(cert, words, balls):
    outputs = sorted({z for b in balls for z in b})
    out_index = {w:i for i,w in enumerate(outputs)}
    def expand(entries, size):
        z = [Fraction(0)]*size
        for i,a,b in entries:
            assert 0 <= i < size and b > 0 and a > 0 and z[i] == 0
            z[i] = Fraction(a,b)
        return z
    x = expand(cert['primal'],len(words))
    y = expand(cert['dual'],len(outputs))
    for out in outputs:
        assert sum(x[i] for i,b in enumerate(balls) if out in b) <= 1
    for b in balls:
        assert sum(y[out_index[z]] for z in b) >= 1
    val = Fraction(*cert['value'])
    assert sum(x) == val == sum(y)
    return val


def run():
    expected = {
        '123': [(1,1,1),(1,2,1),(2,2,2),(5,2,5),(12,40,12)],
        '132': [(1,1,1),(1,2,1),(2,2,2),(4,17,Fraction(23,5)),(11,96,Fraction(227,18))],
    }
    symmetry = {'123':'123','321':'123','132':'132','231':'132','312':'132','213':'132'}
    certificates = {(a['forbidden_pattern'],a['n']):a for a in json.loads((ROOT/'certificates.json').read_text(encoding='utf-8'))}
    for pattern, canonical in symmetry.items():
        for n in range(1,6):
            W = word_set(n,pattern)
            adj, balls = compatibility(W)
            capacity, count, indices = maximal_cliques(adj)
            em, en, ep = expected[canonical][n-1]
            assert capacity == em and count == en, (pattern,n,capacity,count,em,en)
            if pattern in ('123','132'):
                # The second count does not rely on maximality or pivot selection.
                assert fixed_size_count(adj,capacity) == count
                assert fixed_size_count(adj,capacity+1) == 0
                if n >= 3:
                    p = cert_check(certificates[(pattern,n)],W,balls)
                    assert p == ep
                if n == 5:
                    print('EXPLICIT_CODE',pattern,','.join(W[i] for i in sorted(indices)))
            print('CHECK', pattern,n,len(W),capacity,count)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
