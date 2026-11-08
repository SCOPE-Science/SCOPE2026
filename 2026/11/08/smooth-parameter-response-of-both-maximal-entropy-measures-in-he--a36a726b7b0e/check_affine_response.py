#!/usr/bin/env python3
"""Exact finite-word checks for affine coordinate codings of heterochaos baker maps.

These checks support, but do not prove, the infinite-word uniform derivative estimates.
Only Python's standard library is required.
"""
from fractions import Fraction as Q
from itertools import product


def branch_data(symbol, k, M, t, axis):
    assert 1 <= k <= M and 0 < t < Q(1, M)
    if axis == 'u':
        if symbol == 'A':
            return (t, (k-1)*t, Q(1), Q(k-1))
        return (1-M*t, M*t, Q(-M), Q(M))
    if axis == 's':
        if symbol == 'A':
            return (1-M*t, Q(0), Q(-M), Q(0))
        return (t, 1 + (k-M-1)*t, Q(1), Q(k-M-1))
    raise ValueError(axis)


def composition_and_derivative(word, M, t, axis):
    value = deriv = Q(0)
    for symbol, k in reversed(word):
        A, B, dA, dB = branch_data(symbol, k, M, t, axis)
        deriv = dB + dA*value + A*deriv
        value = B + A*value
    return value, deriv


def independent_series(word, M, t, axis):
    total = dtotal = Q(0)
    prefix = Q(1)
    dprefix = Q(0)
    for symbol, k in word:
        A, B, dA, dB = branch_data(symbol, k, M, t, axis)
        total += prefix*B
        dtotal += dprefix*B + prefix*dB
        dprefix, prefix = dprefix*A + prefix*dA, prefix*A
    return total, dtotal


def tests():
    count = 0
    for M in (2, 3, 4):
        for t in (Q(1, 2*M+1), Q(1, M+2)):
            alphabet = tuple((s, k) for s in ('A','B') for k in range(1, M+1))
            r = max(t, 1-M*t)
            for axis in ('u', 's'):
                for sym in alphabet:
                    A, B, dA, dB = branch_data(*sym, M, t, axis)
                    assert 0 <= B <= B+A <= 1
                    assert A <= r
                    assert dA in (Q(1),Q(-M))
                    count += 4
                for n in range(0, 5):
                    for word in product(alphabet, repeat=n):
                        v, dv = composition_and_derivative(word, M, t, axis)
                        w, dw = independent_series(word, M, t, axis)
                        assert (v, dv)==(w, dw)
                        assert 0 <= v <= 1
                        count += 2
                        # Uniform derivative bound for the next truncation increment.
                        # The newly added affine map contributes P_n * B_n.
                        if n <= 3:
                            for extra in alphabet:
                                e, de = composition_and_derivative(word+(extra,), M, t, axis)
                                assert 0 <= e-v <= r**n
                                if n:
                                    assert abs(de-dv) <= n*M*r**(n-1)+M*r**n
                                else:
                                    assert abs(de-dv) <= M
                                count += 2
    return count


if __name__ == '__main__':
    total = tests()
    print('PASS: %d exact rational algebra/bound checks; finite words, M=2,3,4.' % total)
