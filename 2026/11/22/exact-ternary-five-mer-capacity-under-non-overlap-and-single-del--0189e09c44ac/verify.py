#!/usr/bin/env python3
"""Exact standalone verifier for short non-overlapping one-deletion codes."""
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALPH = '012'


def words(n):
    for p in itertools.product(ALPH, repeat=n):
        w = ''.join(p)
        if all(w[:k] != w[-k:] for k in range(1, n)):
            yield w


def shadow(w):
    return {w[:j] + w[j+1:] for j in range(len(w))}


def overlap(a, b):
    return any(a[:k] == b[-k:] or b[:k] == a[-k:]
               for k in range(1, len(a)))


def compatible(a, b):
    return not overlap(a, b) and not (shadow(a) & shadow(b))


def maximum_cliques(ws, deletion=True):
    """Enumerate maximal cliques by the Bron-Kerbosch recursion with pivoting."""
    m = len(ws)
    adj = [0] * m
    for i in range(m):
        for j in range(i):
            if (compatible(ws[i], ws[j]) if deletion else not overlap(ws[i], ws[j])):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    best = 0
    maxima = []
    def ones(s):
        while s:
            b = s & -s
            yield b.bit_length() - 1
            s ^= b
    def bk(R, P, X):
        nonlocal best, maxima
        if not (P or X):
            if len(R) > best:
                best = len(R)
                maxima = []
            if len(R) == best:
                maxima.append(tuple(ws[i] for i in R))
            return
        u = max(ones(P | X), key=lambda i: (P & adj[i]).bit_count())
        Q = P & ~adj[u]
        for v in list(ones(Q)):
            bk(R + (v,), P & adj[v], X & adj[v])
            P &= ~(1 << v)
            X |= 1 << v
    bk((), (1 << m) - 1, 0)
    return best, {frozenset(a) for a in maxima}


def group_orbit(code):
    for p in itertools.permutations(ALPH):
        t = str.maketrans(ALPH, ''.join(p))
        for rev in (False, True):
            yield frozenset((w.translate(t)[::-1] if rev else w.translate(t)) for w in code)


def check_certificate():
    d = json.loads((HERE / 'clique_cover.json').read_text(encoding='utf-8'))
    assert (d['alphabet'], d['length'], d['denominator']) == ('012', 5, 16)
    W = [w for w in words(5) if w[0] in '02' and w[-1] == '1']
    assert len(W) == 48
    cover = {w: 0 for w in W}
    total = 0
    for group in d['cliques']:
        a = group['numerator']
        c = group['words']
        assert type(a) is int and a > 0 and c and len(set(c)) == len(c)
        assert all(w in cover for w in c)
        assert all(not compatible(u, v) for u,v in itertools.combinations(c,2))
        for w in c:
            cover[w] += a
        total += a
    assert len(d['cliques']) == 28
    assert total == 98 and min(cover.values()) >= 16
    # Every legal code is, up to relabeling and perhaps reversal, a
    # subset of W. Each conflict clique contains at most one codeword.
    # Summing weights gives |C| <= total / 16 = 49/8 < 7.
    return total, min(cover.values())


def main():
    cover_total, min_cover = check_certificate()
    expected = {2: (1, 6), 3: (2, 18), 4: (3, 60), 5: (6, 72)}
    result = {}
    for n in (2, 3, 4, 5):
        maximum, cs = maximum_cliques(list(words(n)))
        result[n] = (maximum, len(cs))
        assert result[n] == expected[n], (n, result[n])
    pure_size, _ = maximum_cliques(list(words(5)), deletion=False)
    assert pure_size == 17
    final = maximum_cliques(list(words(5)))[1]
    data = json.loads((HERE / 'optima.json').read_text(encoding='utf-8'))
    assert data['alphabet'] == '012' and data['length'] == 5
    orbits = []
    for row in data['orbits']:
        rep = row['representative']
        assert len(rep) == 6 and len(set(rep)) == 6
        assert all(w in set(words(5)) for w in rep)
        assert all(compatible(a,b) for a,b in itertools.combinations(rep,2))
        O = set(group_orbit(rep))
        assert len(O) == row['orbit_size']
        assert not (O & set().union(*orbits)) if orbits else True
        orbits.append(O)
    assert len(orbits) == 7
    assert sum(map(len,orbits)) == 72
    assert set().union(*orbits) == final
    print('VERIFY_OK')
    print('sizes_and_optimal_codebook_counts', result)
    print('cover_numerator', cover_total, 'denominator', 16, 'minimum_vertex_coverage', min_cover)
    print('symmetry_orbit_sizes', [len(x) for x in orbits])
    print('nonoverlap_only_capacity_length_five', pure_size)

if __name__ == '__main__':
    main()
