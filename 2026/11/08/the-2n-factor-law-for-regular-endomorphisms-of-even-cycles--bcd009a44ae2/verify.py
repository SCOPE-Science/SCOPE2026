#!/usr/bin/env python3
"""Independent finite-step-word and transfer-matrix checks for even-cycle regular maps."""
from itertools import combinations
from math import comb

def path_transfer(n, h):
    a = [0] * (h + 1)
    a[0] = 1
    for _ in range(n - h):
        b = [0] * (h + 1)
        for j, count in enumerate(a):
            if j > 0:
                b[j - 1] += count
            if j < h:
                b[j + 1] += count
        a = b
    return a[h]

def brute(n):
    runs = 0
    regular = 0
    double = 0
    for ups in combinations(range(n), n // 2):
        steps = [-1] * n
        for j in ups:
            steps[j] = 1
        heights = [0]
        for x in steps:
            heights.append(heights[-1] + x)
        assert heights[-1] == 0
        h = max(heights) - min(heights)
        assert 1 <= h <= n // 2
        m = 0
        for i in range(n):
            for sign in (-1, 1):
                if all(steps[(i + j) % n] == sign for j in range(h)):
                    m += 1
        runs += m
        regular += int(m > 0)
        double += m * (m - 1) // 2
    return regular, runs, double

def direct_semigroup(n):
    """Directly test f*g*f=f and f*f=f using actual vertex maps, n<=8."""
    maps = []
    for initial in range(n):
        for signs in ((1,) * n, (-1,) * n):
            v = [initial]
            for step in signs[:-1]:
                v.append((v[-1] + step) % n)
            maps.append(tuple(v))
        for ups in combinations(range(n), n // 2):
            steps = [-1] * n
            for i in ups:
                steps[i] = 1
            v = [initial]
            for step in steps[:-1]:
                v.append((v[-1] + step) % n)
            maps.append(tuple(v))
    assert len(maps) == n * (2 + comb(n, n//2))
    idem = sum(all(f[f[x]] == f[x] for x in range(n)) for f in maps)
    reg = 0
    for f in maps:
        image = set(f)
        if any(all(f[g[y]] == y for y in image) for g in maps):
            reg += 1
    return idem, reg

def main():
    for n in range(4, 20, 2):
        ws = [path_transfer(n, h) for h in range(1, n // 2 + 1)]
        s = sum(ws)
        regwords, marks, doubles = brute(n)
        assert marks == 2 * n * s, (n, marks, 2*n*s)
        assert regwords <= marks and marks-regwords <= doubles
        # For each balanced word, all n cyclic output shifts are distinct maps.
        regular_maps = n * (regwords + 2)
        idempotents = 1 + n * s
        assert 0 <= 2*n*idempotents-regular_maps <= n*doubles
        assert n * (comb(n, n//2) + 2) >= regular_maps
        if n <= 8:
            assert direct_semigroup(n) == (idempotents, regular_maps)
        print('n=%d bridge_regular_words=%d marked=%d pairs=%d I=%d R=%d'
              % (n, regwords, marks, doubles, idempotents, regular_maps))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
