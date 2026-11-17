#!/usr/bin/env python3
"""Independent constructive census of synchronous majority two-cycles on theta graphs.
Reproducible plain Python 3 script; no external packages.
"""
from itertools import combinations, product


def graph(lengths):
    adj = [set(), set()]
    paths = []
    for length in lengths:
        path = [0]
        for _ in range(length - 1):
            nxt = len(adj)
            adj.append(set())
            adj[path[-1]].add(nxt)
            adj[nxt].add(path[-1])
            path.append(nxt)
        adj[path[-1]].add(1)
        adj[1].add(path[-1])
        path.append(1)
        paths.append(path)
    return adj, paths


def majority(adj, state):
    out = 0
    for i, nbs in enumerate(adj):
        votes = sum((state >> k) & 1 for k in nbs)
        if 2 * votes > len(nbs) or (2 * votes == len(nbs) and ((state >> i) & 1)):
            out |= 1 << i
    return out


def fixed_words(length, parity):
    m = length - 1
    if m == 1:
        return [(0,), (1,)] if parity else []
    # Directly test no singleton runs, including endpoints.
    return [w for w in product((0, 1), repeat=m)
            if all(w[j] == w[j - 1] or w[j] == w[j + 1]
                   for j in range(1, m - 1))
            and w[0] == w[1] and w[-1] == w[-2]]


def exact_pred(lengths):
    # Run compositions by parity; differs from the direct enumeration above.
    cache = {}
    def EO(L, p):
        if (L, p) in cache: return cache[L, p]
        if L == 2:
            ans = (1, 0) if p else (0, 0)
        else:
            m = L - 1
            even, odd = [0] * (m + 1), [0] * (m + 1)
            even[0] = 1
            for i in range(2, m + 1):
                even[i] = sum(odd[i-j] for j in range(2, i+1))
                odd[i] = sum(even[i-j] for j in range(2, i+1))
            ans = odd[m], even[m]
        cache[L, p] = ans
        return ans
    total = 0
    for count in (1, 2, 3):
        for active in combinations(range(3), count):
            if len({lengths[j] % 2 for j in active}) != 1: continue
            parity = lengths[active[0]] % 2
            inactive = [j for j in range(3) if j not in active]
            if count == 3: total += 1
            elif count == 2:
                e, o = EO(lengths[inactive[0]], parity)
                total += 2 * (e + o)
            else:
                e, o = EO(lengths[inactive[0]], parity)
                f, g = EO(lengths[inactive[1]], parity)
                total += 2 * (e*f + o*g)
    return total


def construct(lengths):
    adj, paths = graph(lengths)
    possible = set()
    by_active = [0] * 4
    for count in (1, 2, 3):
        for active in combinations(range(3), count):
            if len({lengths[j] % 2 for j in active}) != 1: continue
            parity = lengths[active[0]] % 2
            inactive = [j for j in range(3) if j not in active]
            options = [fixed_words(lengths[j], parity) for j in inactive]
            for fixed_choices in product(*options):
                for start in (0, 1):
                    bits = [None] * len(adj)
                    bits[0], bits[1] = start, start ^ parity
                    for j in active:
                        path = paths[j]
                        for k in range(1, len(path)-1):
                            bits[path[k]] = start ^ (k % 2)
                    for j, word in zip(inactive, fixed_choices):
                        path = paths[j]
                        for k, val in enumerate(word, 1): bits[path[k]] = val
                    if None in bits: raise AssertionError('undefined vertex')
                    state = sum(bit << i for i, bit in enumerate(bits))
                    successor = majority(adj, state)
                    if successor == state or majority(adj, successor) != state: continue
                    flip_paths = [j for j in range(3) if all(((state ^ successor) >> k) & 1 for k in paths[j][1:-1])]
                    if set(flip_paths) != set(active): raise AssertionError('support mismatch')
                    if state in possible: raise AssertionError('duplicate')
                    possible.add(state)
                    by_active[count] += 1
    if len(possible) % 2: raise AssertionError('odd state count')
    return len(possible)//2, [k//2 for k in by_active]


def main():
    tests = 0
    total_orbits = 0
    for a in range(2, 10):
        for b in range(a, 10):
            for c in range(b, 10):
                if a + b + c > 23: continue
                actual, strata = construct((a,b,c))
                predicted = exact_pred((a,b,c))
                if actual != predicted: raise AssertionError((a,b,c,actual,predicted,strata))
                tests += 1
                total_orbits += actual
    print(f'PASS: {tests} triples; {total_orbits} independently constructed primitive orbits.')
    for p in ((2,2,2),(2,2,3),(3,3,3),(3,4,5),(4,4,5),(5,5,5),(5,7,9),(9,9,9)):
        actual, strata = construct(p)
        assert actual == exact_pred(p)
        print(f'{p}: {actual} orbits; by 1,2,3 active paths {strata[1:]}')

if __name__ == '__main__': main()
