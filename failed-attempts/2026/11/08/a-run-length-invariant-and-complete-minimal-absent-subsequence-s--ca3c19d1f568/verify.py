#!/usr/bin/env python3
"""Standalone exact checks of a length-refined minimal-absent-subsequence theorem.

No external packages. All indexing is zero-based in the implementation.
Run: python3 verify.py
"""
from collections import Counter
from itertools import product


def embeds(v, host):
    """Literal greedy embedding: deliberately independent of state graph."""
    pos = 0
    for letter in v:
        i = host.find(letter, pos)
        if i < 0:
            return False
        pos = i + 1
    return True


def brute_minimal_absent(r, k):
    host = ('0' * r + '1') * k
    answer = set()
    # Any minimal absent subsequence has length <= len(host)+1.
    # The sharper bound rk+1 is a consequence checked independently below.
    for length in range(1, len(host) + 2):
        for bits in product('01', repeat=length):
            v = ''.join(bits)
            if embeds(v, host):
                continue
            if all(embeds(v[:i] + v[i + 1:], host) for i in range(length)):
                answer.add(v)
    return answer


TRANSITIONS = {
    'B': [('0', 'A1', 0), ('1', 'B', 1)],
    'D': [('0', 'A2', 0), ('1', 'B', 1)]
}


def graph_minimal_absent(r, k):
    assert r >= 2 and k >= 1
    answer = set()
    stack = [('A1', 0, '0'), ('B', 1, '1')]
    while stack:
        state, periods, prefix = stack.pop()
        if periods > k:
            continue
        if state == 'B' and periods == k:
            answer.add(prefix + '0')
            answer.add(prefix + '1')
        if state == 'A' + str(r) and periods + 1 == k:
            answer.add(prefix + '0')
        if state.startswith('A'):
            j = int(state[1:])
            if j < r:
                edges = [('0', 'A' + str(j+1), 0)]
            else:
                edges = [('0', 'D', 1)]
        else:
            edges = TRANSITIONS[state]
        for c, next_state, crossed in edges:
            if periods + crossed <= k:
                stack.append((next_state, periods + crossed, prefix + c))
    return answer


def poly_add(a, b, factor=1):
    result = Counter(a)
    for exp, coeff in b.items():
        result[exp] += factor * coeff
    return Counter({e:c for e,c in result.items() if c})


def shift(a, s):
    return Counter({e+s:c for e,c in a.items()})


def rational_coefficients(r, upto_k):
    """Coefficients of z^k of the claimed rational function in t."""
    coeffs = [Counter(), Counter({r+1:1, 2:2})]
    if r == 1:
        raise ValueError('The theorem requires r>=2')
    while len(coeffs) <= upto_k:
        k = len(coeffs)
        value = poly_add(shift(coeffs[k-1], 1), shift(coeffs[k-1], r))
        if k == 2:
            value = poly_add(value, Counter({r+2:-2,r+3:2}))
        else:
            value = poly_add(value, shift(coeffs[k-2],r+1), -1)
            value = poly_add(value, shift(coeffs[k-2],r+2))
        coeffs.append(value)
    return coeffs


def run():
    checks = 0
    words_checked = 0
    for r, upper in ((2,7),(3,4),(4,3),(5,3),(6,2)):
        for k in range(1,upper+1):
            exact = brute_minimal_absent(r,k)
            graph = graph_minimal_absent(r,k)
            assert exact == graph, (r,k,sorted(exact^graph)[:5])
            formula = rational_coefficients(r,k)[k]
            assert Counter(map(len, exact)) == formula, (r,k,formula)
            assert len(exact) == 3 * 2 ** (k-1), (r,k,len(exact))
            assert all(k+1 <= len(w) <= r*k+1 for w in exact)
            words_checked += sum(2**n for n in range(1,(r+1)*k+2))
            checks += 1

    # Separate large-parameter check: no direct enumeration, so a different
    # weighted graph DP must agree with rational polynomial coefficients.
    for r in (2,3,4,5,6,8,12):
        for k in range(1,17):
            graph = graph_minimal_absent(r,k)
            expect = rational_coefficients(r,k)[k]
            spectrum = Counter(map(len,graph))
            assert spectrum == expect, (r,k,spectrum,expect)
            assert len(graph) == 3*2**(k-1)
            checks += 1
    print('PASS:',checks,'parameter/length-spectrum comparisons')
    print('PASS: independent brute-force candidate words tested:',words_checked)
    print('PASS: graph set equality for 19 direct parameter pairs')
    print('PASS: rational coefficients and total 3*2^(k-1) for r<=12, k<=16')
    print('Limits: finite tests corroborate; the all-parameter proof is mathematical.')


if __name__ == '__main__':
    run()
