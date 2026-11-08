#!/usr/bin/env python3
"""Exact finite-state and direct checks for cyclic antisquare-good words.

Run: python3 VERIFY.py
Uses only the Python standard library. It independently constructs the
five-bit forbidden-factor transfer matrix and checks its characteristic
polynomial using the Newton identities.
"""

from itertools import product
from fractions import Fraction
from math import comb

FORBIDDEN = (
    '0011', '1100', '0110', '1001',
    '010101', '101010', '001011', '110100',
)
CODE_FORBIDDEN = ('010', '101', '11111', '01110')


def is_allowed_periodic(word):
    doubled = word * 6
    return all(f not in doubled for f in FORBIDDEN)


def direct_antisquare_good(word):
    """Sufficient direct test for short periodic words, used as diagnostics."""
    n = len(word)
    expanded = word * (5 * n + 2)
    for half in range(2, 2 * n + 1):
        for i in range(n):
            left = expanded[i:i + half]
            right = expanded[i + half:i + 2 * half]
            if all(a != b for a, b in zip(left, right)):
                return False
    return True


def expected_counts(last):
    # -z f'(z)/f(z) with f(z)=1-z-z^4-z^6, multiplied by 2.
    p = [0] * (last + 1)
    for n in range(1, last + 1):
        p[n] = sum(p[n - d] for d in (1, 4, 6) if n > d)
        p[n] += {1: 2, 4: 8, 6: 12}.get(n, 0)
    return p


def exact_run_pair_count(n):
    total = Fraction(2)
    for m in range(1, n // 4 + 1):
        ways = sum(
            comb(m, j) * comb(n - 3*m - 2*j - 1, m - 1)
            for j in range(0, min(m, (n - 4*m) // 2) + 1)
        )
        total += Fraction(2*n*ways, m)
    assert total.denominator == 1
    return int(total)


def mobius(n):
    primes = 0
    d = 2
    while d*d <= n:
        if n % d == 0:
            n //= d
            primes += 1
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        primes += 1
    return -1 if primes % 2 else 1


def transfer_graph():
    nodes = [''.join(x) for x in product('01', repeat=5)]
    index = {s: i for i, s in enumerate(nodes)}
    graph = [[] for _ in nodes]
    for i, s in enumerate(nodes):
        for b in '01':
            six = s + b
            if all(not six.endswith(f) for f in FORBIDDEN):
                graph[i].append(index[s[1:] + b])
    return graph


def traces(graph, last):
    out = [0] * (last + 1)
    # Every n-step closed walk is a marked n-periodic word avoiding the
    # eight forbidden factors; this works for n shorter than five as well.
    for start in range(len(graph)):
        current = [0] * len(graph)
        current[start] = 1
        for n in range(1, last + 1):
            nxt = [0] * len(graph)
            for i, ways in enumerate(current):
                if ways:
                    for j in graph[i]:
                        nxt[j] += ways
            current = nxt
            out[n] += current[start]
    return out


def determinant_from_traces(trace, order):
    # det(I-z A) = sum e[k] z^k,
    # k e[k] = -sum_{i=1}^k e[k-i] trace(A^i).
    e = [Fraction(1)]
    for k in range(1, order + 1):
        numerator = sum(e[k - i] * trace[i] for i in range(1, k + 1))
        value = -numerator / k
        if value.denominator != 1:
            raise AssertionError('nonintegral determinant coefficient')
        e.append(value)
    return [int(x) for x in e]


def poly_mul(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x * y
    return ans


def run():
    graph = transfer_graph()
    assert sum(len(x) for x in graph) == 44
    last = 40
    trace = traces(graph, last)
    expected = expected_counts(last)
    assert trace == expected, (trace, expected)
    for n in range(1, last + 1):
        assert exact_run_pair_count(n) == expected[n]
        primitive_points = sum(
            mobius(d) * expected[n//d] for d in range(1, n+1) if n % d == 0
        )
        assert primitive_points >= 0 and primitive_points % n == 0
        assert sum(
            d * (sum(mobius(e)*expected[d//e]
                     for e in range(1,d+1) if d % e == 0)//d)
            for d in range(1,n+1) if n % d == 0
        ) == expected[n]
    f = [1, -1, 0, 0, -1, 0, -1]
    determinant = poly_mul(f, f)
    determinant += [0] * (len(graph) + 1 - len(determinant))
    assert determinant_from_traces(trace, len(graph)) == determinant

    direct_total = 0
    for n in range(1, 17):
        count = 0
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            if is_allowed_periodic(word):
                count += 1
        assert count == expected[n], (n, count, expected[n])
        direct_total += 2 ** n

    antisquare_cases = 0
    for n in range(1, 11):
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            assert is_allowed_periodic(word) == direct_antisquare_good(word)
            antisquare_cases += 1

    code_cases = 0
    for n in range(1, 12):
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            code = ''.join('1' if word[i] != word[i+1] else '0'
                           for i in range(n-1))
            a = all(f not in word for f in FORBIDDEN)
            b = all(f not in code for f in CODE_FORBIDDEN)
            assert a == b
            code_cases += 1
    print('VERIFY_OK transfer_states=32 transfer_edges=44',
          'matrix_trace_n=1..40 characteristic_polynomial_degree=32',
          'run_pair_formula_n=1..40 mobius_orbits_n=1..40',
          'brute_periodic_words=' + str(direct_total),
          'direct_antisquare_cases=' + str(antisquare_cases),
          'finite_pansiot_cases=' + str(code_cases))


if __name__ == '__main__':
    run()
