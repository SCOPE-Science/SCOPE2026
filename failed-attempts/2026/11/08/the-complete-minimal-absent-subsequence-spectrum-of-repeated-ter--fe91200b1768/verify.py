#!/usr/bin/env python3
"""Exact polynomial-certificate and direct-subsequence checks for ternary MAS."""
import json
import itertools
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'certificate.json').read_text(encoding='utf-8'))

def poly(terms):
    return {(e_y, e_z): c for e_y, e_z, c in terms if c}

def plus(p, q, scale=1):
    r = dict(p)
    for a, v in q.items():
        r[a] = r.get(a, 0) + scale * v
        if not r[a]: del r[a]
    return r

def times(p, q):
    r = defaultdict(int)
    for (ay, az), a in p.items():
        for (by, bz), b in q.items():
            r[(ay + by, az + bz)] += a * b
    return {k: v for k, v in r.items() if v}

def indicator(x):
    return int(bool(x))

def transition(a, b, c):
    return indicator(b <= a) + indicator(c <= b) - indicator(c <= a) == 1

def algebraic_certificate():
    states = list(itertools.product(range(3), repeat=2))
    assert DATA['states'] == [list(x) for x in states]
    H = [poly(v) for v in DATA['state_vector']]
    D, N = poly(DATA['denominator']), poly(DATA['numerator'])
    assert D.get((0, 0)) == 1
    for i, (a, b) in enumerate(states):
        rhs = D if b <= a else {}
        lhs = dict(H[i])
        for c in range(3):
            if transition(a, b, c):
                edge = {(1, indicator(c <= b)): 1}
                lhs = plus(lhs, times(edge, H[states.index((b, c))]), -1)
        assert lhs == rhs, ('certificate state', (a, b))
    start = {}
    for i, (a, b) in enumerate(states):
        if b <= a:
            start = plus(start, times({(2, 1): 1}, H[i]))
    assert start == N, 'certificate numerator'
    return N, D

def embedded(v, host):
    j = 0
    for letter in host:
        if j < len(v) and letter == v[j]:
            j += 1
    return j == len(v)

def structural(v, k):
    return (len(v) >= 2 and
            sum(v[i] <= v[i - 1] for i in range(1, len(v))) == k and
            v[1] <= v[0] and v[-1] <= v[-2] and
            all(transition(v[i - 1], v[i], v[i + 1])
                for i in range(1, len(v) - 1)))

def brute(q, k, length_cutoff):
    host = tuple(range(q)) * k
    counts = Counter()
    tested = 0
    for length in range(1, length_cutoff + 1):
        for v in itertools.product(range(q), repeat=length):
            predicted = structural(v, k)
            direct = (not embedded(v, host) and
                      all(embedded(v[:i] + v[i + 1:], host)
                          for i in range(length)))
            assert direct == predicted, (q, k, v, direct, predicted)
            tested += 1
            if direct:
                counts[length] += 1
    return counts, tested

def series(N, D, max_k):
    # Formal division in z with coefficients in the finite y-polynomial ring.
    result = {}
    d0 = D[(0, 0)]
    assert d0 == 1 and all(z > 0 for (y, z) in D if (y, z) != (0, 0))
    for k in range(max_k + 1):
        for length in range(2 * max_k + 3):
            value = N.get((length, k), 0)
            for (dy, dz), coeff in D.items():
                if dz == 0: continue
                value -= coeff * result.get((length - dy, k - dz), 0)
            result[(length, k)] = value
    return result

def transfer(max_k):
    # Independent direct dynamic programming, without the rational certificate.
    counts = Counter()
    curr = Counter()
    for a, b in itertools.product(range(3), repeat=2):
        if b <= a:
            curr[(a, b, 1, 2)] += 1
    for length in range(2, 2 * max_k + 1):
        nxt = Counter()
        for (a, b, k, m), number in curr.items():
            if b <= a and k <= max_k:
                counts[(m, k)] += number
            if k >= max_k: continue
            for c in range(3):
                if transition(a, b, c):
                    nk = k + indicator(c <= b)
                    if nk <= max_k:
                        nxt[(b, c, nk, m + 1)] += number
        curr = nxt
    return counts

def main():
    N, D = algebraic_certificate()
    series_coeff = series(N, D, 12)
    counts = transfer(12)
    for k in range(1, 13):
        for length in range(k + 1, 2 * k + 1):
            assert series_coeff[(length, k)] == counts[(length, k)], ('series', length, k)
    observed = 0
    for q, k, cutoff in ([(2, k, 2 * k + 2) for k in range(1, 5)] +
                          [(3, k, 2 * k + 2) for k in range(1, 5)] +
                          [(4, k, 2 * k + 1) for k in range(1, 3)]):
        exact, tested = brute(q, k, cutoff)
        observed += tested
        if q == 3:
            for length, n in exact.items():
                assert series_coeff[(length, k)] == n, ('direct', k, length)
            print('ternary k=', k, 'spectrum=', dict(sorted(exact.items())), 'total=', sum(exact.values()))
    for k, expected in enumerate([6, 16, 46, 127, 349, 960, 2640, 7264, 19989, 54999], 1):
        assert sum(series_coeff[(length, k)] for length in range(k + 1, 2 * k + 1)) == expected
    print('PASS: exact 9-state polynomial identities, 12 transfer coefficient rows,',
          observed, 'direct subsequence/deletion pairs, ten total counts')

if __name__ == '__main__':
    main()
