#!/usr/bin/env python3
"""Independent finite checks for rank-refined centralizers of path maps.

Run with Python 3 standard library: python verify_path_rank_centralizers.py
"""
from itertools import product
from collections import Counter, defaultdict
from math import comb


def maps(N):
    for bits in product((0, 1), repeat=N):
        h = sum(bits)
        for start in range(N - h + 1):
            f = [start]
            for bit in bits:
                f.append(f[-1] + bit)
            yield tuple(f)


def clamp(N, a, b):
    return tuple(max(a, min(i, b)) for i in range(N + 1))


def commute(f, g):
    return all(f[g[i]] == g[f[i]] for i in range(len(f)))


def predicted(N, a, b):
    k = b-a
    A, B = a, N-b
    ans = Counter()
    for h in range(k+1):
        for s in range(k-h+1):
            for i in range(A+1 if s == 0 else 1):
                for j in range(B+1 if s+h == k else 1):
                    weight = comb(k, h)
                    if s == 0:
                        weight *= comb(A, i)
                    if s+h == k:
                        weight *= comb(B, j)
                    ans[h+i+j] += weight
    return ans


def pair_rank_via_rational(N):
    # Coefficient of x^N in
    # 1 / ((1-x)^2 (1-ux) (1-(1+u)x)^2).
    out = Counter()
    for k in range(N+1):
        for j in range(N-k+1):
            i = N-k-j
            for h in range(k+1):
                out[j+h] += (i+1)*(k+1)*comb(k,h)
    return out


def assertions():
    all_cases = 0
    for N in range(0, 11):
        fs = list(maps(N))
        found_agg = Counter()
        for a in range(N+1):
            for b in range(a,N+1):
                e = clamp(N,a,b)
                observed = Counter(sum(f[i+1]-f[i] for i in range(N))
                                   for f in fs if commute(f,e))
                expected = predicted(N,a,b)
                assert observed == expected, (N,a,b,observed,expected)
                assert expected[0] == b-a+1
                if b>a:
                    k = b-a
                    c2 = expected[2]
                    S = N-k
                    ab = comb(S,2) + comb(k,2)*(k-1) + k*S - c2
                    assert ab == a*(N-b), (N,a,b,ab)
                else:
                    assert expected == Counter({i:comb(N,i) for i in range(N+1)})
                found_agg.update(observed)
                all_cases += 1
        assert found_agg == pair_rank_via_rational(N), N
        if N >= 1:
            n = N+1
            A_n = (4*n-12)*2**n + (n*n+9*n)//2 + 12
            assert sum(found_agg.values()) == A_n, (N,A_n,found_agg)
        print('N=%02d maps=%5d commuting_pairs=%6d' % (N,len(fs),sum(found_agg.values())))
    # Test all gap pairs and ensure the polynomial distinguishes nonconstant
    # intervals modulo reversal, not merely the finite examples above.
    for N in range(1, 35):
        signatures=defaultdict(set)
        for a in range(N+1):
            for b in range(a+1,N+1):
                p=predicted(N,a,b)
                signatures[tuple(p.get(i,0) for i in range(N+1))].add((b-a,tuple(sorted((a,N-b)))))
        assert all(len(v)==1 for v in signatures.values()), N
    print('RANK_REFINED_PATH_CENTRALIZERS_VERIFIED; cases=%d' % all_cases)


if __name__ == '__main__':
    assertions()
