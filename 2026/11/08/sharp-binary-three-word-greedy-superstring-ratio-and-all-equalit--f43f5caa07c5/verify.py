#!/usr/bin/env python3
"""Exact worst-case greedy shortest-common-superstring census on binary three-words.

No external packages or files are needed. Each dynamic program enumerates finite
states exhaustively, and independent algorithms check its final output.
"""
from functools import lru_cache
from itertools import permutations
from fractions import Fraction
from collections import defaultdict

K = 3
WORDS = tuple(format(i, '03b') for i in range(8))


def overlap(a, b):
    """Greatest suffix/prefix match, with a zero-length match allowed."""
    for ell in range(min(len(a), len(b)), 0, -1):
        if a[-ell:] == b[:ell]:
            return ell
    return 0


def selected(mask):
    return tuple(WORDS[j] for j in range(8) if (mask >> j) & 1)


@lru_cache(None)
def direct_greedy(state):
    """Direct string-merger recursion exploring all maximum-overlap ties."""
    if len(state) == 1:
        return len(state[0])
    pairs = [(i, j, overlap(state[i], state[j]))
             for i in range(len(state)) for j in range(len(state)) if i != j]
    best = max(z for _, _, z in pairs)
    answers = []
    for i, j, z in pairs:
        if z != best:
            continue
        merged = state[i] + state[j][z:]
        nxt = tuple(sorted([state[t] for t in range(len(state))
                            if t not in (i, j)] + [merged]))
        answers.append(direct_greedy(nxt))
    return max(answers)


@lru_cache(None)
def endpoint_greedy(paths):
    """Independent recursion on ordered paths of *original* three-words.

    The classical endpoint-overlap lemma for equal-length, substring-free
    inputs states that each available merger overlap equals the overlap of
    the rightmost word of the left path and the leftmost of the right path.
    We minimize the cumulative overlap to obtain the worst greedy length.
    """
    if len(paths) == 1:
        return 0
    pairs = [(i, j, overlap(WORDS[paths[i][-1]], WORDS[paths[j][0]]))
             for i in range(len(paths)) for j in range(len(paths)) if i != j]
    best = max(z for _, _, z in pairs)
    return min(z + endpoint_greedy(tuple(sorted(
        [paths[t] for t in range(len(paths)) if t not in (i, j)]
        + [paths[i] + paths[j]])))
        for i, j, z in pairs if z == best)


def held_karp_opt(mask):
    """Maximum-overlap Hamilton path DP, exact for equal-length inputs."""
    ids = [j for j in range(8) if (mask >> j) & 1]
    n = len(ids)
    best = {(1 << i, i): 0 for i in range(n)}
    for subset in range(1, 1 << n):
        for last in range(n):
            score = best.get((subset, last))
            if score is None:
                continue
            for nxt in range(n):
                if subset & (1 << nxt):
                    continue
                key = (subset | (1 << nxt), nxt)
                score2 = score + overlap(WORDS[ids[last]], WORDS[ids[nxt]])
                if score2 > best.get(key, -1):
                    best[key] = score2
    savings = max(best[((1 << n) - 1, i)] for i in range(n))
    return K * n - savings


def brute_opt(mask):
    """Completely separate permutation evaluator for optimal length."""
    ws = selected(mask)
    return min(len(ws)*K - sum(overlap(a,b) for a,b in zip(p,p[1:]))
               for p in permutations(ws))


def transform_mask(mask, reverse=False, complement=False):
    f = lambda w: (w[::-1] if reverse else w)
    def g(w):
        w = f(w)
        return ''.join('1' if ch == '0' else '0' for ch in w) if complement else w
    return sum(1 << int(g(w), 2) for w in selected(mask))


def verify():
    table = []
    by_size = defaultdict(list)
    for mask in range(1, 256):
        ws = selected(mask)
        direct = direct_greedy(ws)
        paths = tuple((i,) for i in range(8) if mask & (1 << i))
        endpoint = K*len(ws) - endpoint_greedy(paths)
        assert direct == endpoint, (mask, direct, endpoint)
        optimum = held_karp_opt(mask)
        assert optimum == brute_opt(mask), mask
        assert optimum <= direct <= K*len(ws)
        row = (mask,len(ws),optimum,direct)
        table.append(row)
        by_size[len(ws)].append(row)
    ratio = max(Fraction(g, o) for _, _, o, g in table)
    assert ratio == Fraction(10, 7), ratio
    max_masks = sorted(mask for mask, n, o, g in table if Fraction(g, o) == ratio)
    assert max_masks == [31, 87, 234, 248], max_masks
    assert all(x[1] == 5 and x[2:] == (7,10) for x in table if x[0] in max_masks)
    orbit = {transform_mask(31, reverse=r, complement=c) for r in (False,True) for c in (False,True)}
    assert orbit == set(max_masks), orbit
    # Verify an explicit greedy worst-case execution: all chosen overlaps are globally maximal.
    blocks = ['000','001','010','011','100']
    steps = [('001','010'), ('100','0010'), ('10010','011'), ('000','1001011')]
    for a,b in steps:
        z = overlap(a,b)
        assert z == max(overlap(x,y) for x in blocks for y in blocks if x != y)
        assert a in blocks and b in blocks and a != b
        blocks.remove(a); blocks.remove(b); blocks.append(a+b[z:])
    assert blocks == ['0001001011']
    optimum_string = '0100011'
    assert len(optimum_string)==7
    assert all(w in optimum_string for w in selected(31))
    assert held_karp_opt(31)==7
    print('BINARY_3MER_GREEDY_VERIFY_OK masks=255 ratio=10/7 maximizers=4')
    for k in sorted(by_size):
        frac = max(Fraction(g,o) for _,_,o,g in by_size[k])
        achievers=sum(Fraction(g,o)==frac for _,_,o,g in by_size[k])
        print(f'k={k} subsets={len(by_size[k])} peak={frac} attaining={achievers}')
    return table


if __name__ == '__main__':
    table = verify()
    print('mask,cardinality,optimal_length,worst_greedy_length')
    for x in table:
        print(','.join(map(str, x)))
