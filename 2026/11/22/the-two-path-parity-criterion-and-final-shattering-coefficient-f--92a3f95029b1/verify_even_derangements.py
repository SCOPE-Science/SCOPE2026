#!/usr/bin/env python3
"""Independent finite checks for even-derangement edge-query shattering.
Python 3 standard library only; no network, randomization, or external packages.
"""
from itertools import permutations, combinations
from collections import Counter
from math import comb, factorial


def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 == 0


def even_derangements(n):
    return [p for p in permutations(range(n)) if all(p[i] != i for i in range(n)) and even(p)]


def partial_rooks(n, k):
    for rows in combinations(range(n), k):
        for cols in combinations(range(n), k):
            for values in permutations(cols):
                if all(i != v for i, v in zip(rows, values)):
                    yield tuple(zip(rows, values))


def topology(n, support):
    out = dict(support)
    inverse = {j: i for i, j in support}
    starts = [i for i in range(n) if i not in inverse]
    seen = set()
    lengths = []
    for v in starts:
        length = 0
        while True:
            assert v not in seen
            seen.add(v)
            length += 1
            if v not in out:
                break
            v = out[v]
        lengths.append(length)
    cycles = 0
    for v in range(n):
        if v not in seen:
            cycles += 1
            w = v
            while w not in seen:
                seen.add(w)
                w = out[w]
    assert len(seen) == n and len(lengths) == n - len(support)
    return sorted(lengths), cycles


def structural_shattered(n, support):
    k = len(support)
    if k > n - 2:
        return False
    if k <= n - 4:
        return True
    lengths, cycles = topology(n, support)
    if k == n - 3:
        return not (lengths == [1, 1, 1] and (n - cycles) % 2 == 0)
    assert k == n - 2 and len(lengths) == 2
    a, b = lengths
    return (a, b) != (1, 1) and (a >= 3 or (n - cycles) % 2 == 1)


def brute_shattered(support, concepts):
    k = len(support)
    full = (1 << (1 << k)) - 1
    seen = 0
    for p in concepts:
        trace = 0
        for j, (i, v) in enumerate(support):
            if p[i] == v:
                trace |= 1 << j
        seen |= 1 << trace
        if seen == full:
            return True
    return False


def signed_robustness_small():
    # With full forbidden diagonal and <=2 other disjoint forbidden cells,
    # both signs occur for each of the r=4 residual configurations.
    r = 4
    allp = list(permutations(range(r)))
    count = 0
    for t in range(3):
        for rows in combinations(range(r), t):
            for cols in combinations(range(r), t):
                for v in permutations(cols):
                    f = set(zip(rows, v))
                    if any(i == j for i, j in f):
                        continue
                    ok = [False, False]
                    for p in allp:
                        if all(p[i] != i and (i, p[i]) not in f for i in range(r)):
                            ok[0 if even(p) else 1] = True
                    assert all(ok), (r, f)
                    count += 1
    # For r=5 extend both forbidden matchings to perfect matchings;
    # after diagonal normalization only the second permutation varies.
    r = 5
    allp = list(permutations(range(r)))
    for sigma in allp:
        ok = [False, False]
        for p in allp:
            if all(p[i] != i and p[i] != sigma[i] for i in range(r)):
                ok[0 if even(p) else 1] = True
        assert all(ok), sigma
    return count, len(allp)


def refined_derangements(maxn):
    # D[m,c] = permutations of m labels with c cycles, all cycle lengths >=2.
    D = [[0] * (maxn + 1) for _ in range(maxn + 1)]
    D[0][0] = 1
    for m in range(1, maxn + 1):
        for ell in range(2, m + 1):
            for c in range(1, m + 1):
                D[m][c] += comb(m - 1, ell - 1) * factorial(ell - 1) * D[m - ell][c - 1]
    return D


def rook_number(n, k):
    return sum((-1)**j * comb(n, j) * comb(n-j, k-j)**2 * factorial(k-j) for j in range(k+1))


def top_count(n, D):
    total_twice = 0
    for a in range(1, n):
        for b in range(1, n - a + 1):
            m = n - a - b
            for c in range(m + 1):
                if a == b == 1:
                    continue
                if a >= 3 and b >= 3 or (n - c) % 2:
                    weight = factorial(n) * D[m][c]
                    assert weight % factorial(m) == 0
                    total_twice += weight // factorial(m)
    assert total_twice % 2 == 0
    return total_twice // 2


def coefficients(n, D):
    vals = [rook_number(n, k) for k in range(n - 1)]
    m = n - 3
    odd = sum(D[m][c] for c in range(m+1) if (m-c) % 2)
    vals[n-3] -= comb(n, 3)*odd
    vals[n-2] = top_count(n, D)
    return vals


def explicit_top_support(n):
    if n % 2:
        # Odd n: two missing arcs of a single n-cycle.
        p = [(i+1) % n for i in range(n)]
        missing = {0, n//2}
    else:
        # Even n: a 3-cycle and an odd-length (n-3)-cycle,
        # omitting two consecutive arcs from the 3-cycle.
        p = [None] * n
        p[0:3] = [1, 2, 0]
        for i in range(3, n-1):
            p[i] = i+1
        p[n-1] = 3
        missing = {0,1}
    return tuple((i,p[i]) for i in range(n) if i not in missing)


def local_witness(n, support, negative=None):
    positive = dict(e for e in support if e != negative)
    rows = [i for i in range(n) if i not in positive]
    cols = [j for j in range(n) if j not in positive.values()]
    assert len(rows) <= 3
    for v in permutations(cols):
        p = [None] * n
        for i,j in positive.items():p[i] = j
        for i,j in zip(rows,v):p[i] = j
        if all(p[i] != i for i in range(n)) and (negative is None or p[negative[0]] != negative[1]) and even(p):
            return p
    return None


def main():
    small = signed_robustness_small()
    print('SMALL_PARITY_ROBUSTNESS_PASS', small, flush=True)
    D = refined_derangements(14)
    expected = {4:[1,12,0],5:[1,20,120,240],6:[1,30,315,1420,1140]}
    for n in range(4, 15):
        coeff = coefficients(n, D)
        if n in expected:
            assert coeff == expected[n], (n,coeff)
        print('POLYNOMIAL',n,coeff[-3:], flush=True)
    total_supports = 0
    for n in range(4,8):
        concepts = even_derangements(n)
        predicted = [0] * (n-1)
        for k in range(n-1):
            for s in partial_rooks(n,k):
                a = structural_shattered(n,s)
                b = brute_shattered(s,concepts)
                assert a == b, (n,s,a,b)
                predicted[k] += int(a)
                total_supports += 1
        assert predicted == coefficients(n,D), (n,predicted,coefficients(n,D))
        print('EXHAUSTIVE_PASS',n,'supports',total_supports,'coefficients',predicted,flush=True)
    for n in range(5,15):
        s = explicit_top_support(n)
        assert structural_shattered(n,s), n
        assert local_witness(n,s) is not None, (n,'all+')
        for e in s:
            assert local_witness(n,s,e) is not None, (n,e)
    print('EXPLICIT_LOWER_BOUND_WITNESSES_PASS 5..14',flush=True)
    print('EVEN_DERANGEMENT_ALL_CHECKS_PASS',total_supports,flush=True)

if __name__=='__main__':
    main()
