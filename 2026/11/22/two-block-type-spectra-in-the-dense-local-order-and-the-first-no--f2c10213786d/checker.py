"""Independent finite verifier for weighted two-block local-order extensions.

Usage: python3 checker.py
Requires only the Python 3 standard library.
"""
from collections import Counter
from itertools import combinations
from math import comb
import json


def gap_formula(n, r):
    assert n >= 1 and r >= 1
    a = list(range(1, n + 1)) + list(range(n - 1, -1, -1))
    result = [0] * (n * r + 1)
    for s in range(2 * n):
        # Unbounded knapsack: each of n+1 distinct gaps can receive any
        # nonnegative number of consecutively named new points.
        dp = [[0] * (n * r + 1) for _ in range(r)]
        dp[0][0] = 1
        for j in range(n + 1):
            w = a[(s + j) % (2 * n)]
            for c in range(1, r):
                for exponent in range(w, n * r + 1):
                    dp[c][exponent] += dp[c - 1][exponent - w]
        for exponent, value in enumerate(dp[r - 1]):
            if value and exponent + a[s] <= n * r:
                result[exponent + a[s]] += value
    return result


def direct_orientations(n, r):
    """Enumerate every cross-edge orientation, independent of gap formula."""
    N = n + r
    rows0 = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if i < n and j >= n:
                continue
            rows0[i] |= 1 << j
    edges = [(i, n + j) for i in range(n) for j in range(r)]
    ans = [0] * (n * r + 1)
    for mask in range(1 << (n * r)):
        out = rows0.copy()
        for bit, (i, j) in enumerate(edges):
            if mask & (1 << bit):
                out[i] |= 1 << j
            else:
                out[j] |= 1 << i
        bad = False
        # Forbidden local tournament configuration: a directed triangle
        # contained in the in- or out-neighborhood of a fourth vertex.
        for a, b, c in combinations(range(N), 3):
            cyclic = bool(out[a] & (1 << b)) and bool(out[b] & (1 << c)) and bool(out[c] & (1 << a))
            cyclic |= bool(out[a] & (1 << c)) and bool(out[c] & (1 << b)) and bool(out[b] & (1 << a))
            if not cyclic:
                continue
            for v in range(N):
                if v == a or v == b or v == c:
                    continue
                d = int(bool(out[v] & (1 << a))) + int(bool(out[v] & (1 << b))) + int(bool(out[v] & (1 << c)))
                if d in (0, 3):
                    bad = True
                    break
            if bad:
                break
        if not bad:
            ans[mask.bit_count()] += 1
    return ans


def is_unimodal(seq):
    state = 0
    for a, b in zip(seq, seq[1:]):
        if b < a:
            state = 1
        elif b > a and state:
            return False
    return True


def verify():
    table = {}
    exceptions = []
    comparisons = 0
    for total in range(2, 9):
        for n in range(1, total):
            r = total - n
            poly = gap_formula(n, r)
            brute = direct_orientations(n, r)
            assert poly == brute, (n, r, poly, brute)
            assert poly == poly[::-1], (n, r, 'palindromicity')
            assert sum(poly) == 2 * n * comb(n + r - 1, n), (n, r, 'total')
            nonunimodal = not is_unimodal(poly)
            if nonunimodal:
                exceptions.append((n, r))
            table[f'{n},{r}'] = {
                'n': n, 'r': r, 'coefficients': poly,
                'total': sum(poly), 'unimodal': not nonunimodal,
            }
            comparisons += 1
    assert exceptions == [(3, 5), (4, 4), (5, 3)], exceptions
    assert table['3,5']['coefficients'] == [1, 2, 5, 10, 15, 22, 26, 24, 24, 26, 22, 15, 10, 5, 2, 1]
    assert table['4,4']['coefficients'] == [1, 2, 5, 10, 20, 24, 33, 28, 34, 28, 33, 24, 20, 10, 5, 2, 1]
    print('VERIFY_OK')
    print('ordered_pairs_tested=', comparisons)
    print('exhaustive_all_cross_orientations_for_each_pair=YES')
    print('first_nonunimodal_pairs=', exceptions)
    print('spectrum_3_5=', table['3,5']['coefficients'])
    print('spectrum_4_4=', table['4,4']['coefficients'])
    return table


if __name__ == '__main__':
    TABLE = verify()
    with open('small_spectra.json', 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'description': 'Exact cross-edge spectra for all ordered positive (n,r) with n+r<=8, independently checked by exhaustive orientation enumeration.', 'spectra': TABLE}, f, indent=2, ensure_ascii=False)
        f.write('\n')
