"""Exact rational check of the two-length duplication joint law.

Run: python verify_joint.py
No third-party modules required.
"""
from fractions import Fraction
from itertools import product
from math import comb, gcd


def multiply(f, h):
    output = {}
    for (i, j), a in f.items():
        for (s, t), b in h.items():
            key = (i+s, j+t)
            output[key] = output.get(key, 0) + a*b
    return output


def power(f, m):
    result = {(0, 0): Fraction(1)}
    for _ in range(m):
        result = multiply(result, f)
    return result


def predicted(n, k, ell, q):
    g = gcd(k, ell)
    a, b = k//g, ell//g
    c = max(0, n-k-ell+g)
    assert 1 <= k < ell <= n <= k+ell
    short = {(0, 0): Fraction(1), (1, 0): Fraction(1, q)}
    long = {(0, 0): Fraction(1), (0, 1): Fraction(1, q)}
    cycle = multiply(power(short, b), power(long, a))
    cycle[(b, a)] += Fraction(q-1, q**(a+b))
    return multiply(multiply(power(short, n-k-c*b),
                             power(long, n-ell-c*a)), power(cycle, c))


def observed(n, k, ell, q):
    totals = {}
    for word in product(range(q), repeat=n):
        y = sum(word[i] == word[i+k] for i in range(n-k))
        z = sum(word[i] == word[i+ell] for i in range(n-ell))
        for i in range(y+1):
            for j in range(z+1):
                totals[(i, j)] = totals.get((i, j), 0) + comb(y, i)*comb(z, j)
    return {pair: Fraction(count, q**n) for pair, count in totals.items()}


def run():
    cases = [(2, 1, 2), (3, 1, 2), (2, 1, 3), (3, 1, 3),
             (2, 2, 3), (2, 2, 4), (3, 2, 4), (2, 2, 5),
             (2, 3, 4), (2, 3, 6)]
    checked = 0
    for q, k, ell in cases:
        for n in range(ell, k+ell+1):
            if q**n > 9000:
                continue
            p = {key: value for key, value in predicted(n, k, ell, q).items() if value}
            o = observed(n, k, ell, q)
            assert p == o, (q, k, ell, n, p, o)
            checked += 1
    assert checked >= 20
    print('JOINT_PGF_VERIFY_OK', checked)


if __name__ == '__main__':
    run()
