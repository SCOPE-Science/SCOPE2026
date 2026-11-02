"""Exact finite checks of the gcd–lcm pencil on complete divisor lattices.
Run: python verify_gcd_lcm_sum.py
The finite checks corroborate, but do not replace, the proof for arbitrary n.
"""
from itertools import product
from math import gcd, lcm, prod
from sympy import Matrix, Symbol, divisors, factorint, totient, expand


def predicted_pencil(n, t):
    prime_powers = list(factorint(n).items())
    r = len(prime_powers)
    ans = prod(int(totient(d)) for d in divisors(n))
    for mask in range(1, 1 << r):
        selected = [i for i in range(r) if (mask >> i) & 1]
        m = prod(prime_powers[i][0] ** prime_powers[i][1] for i in selected)
        mult = (2 ** (len(selected) - 1)) * prod(
            prime_powers[i][1] - 1 for i in range(r) if i not in selected
        )
        ans *= (1 - m * t * t) ** mult
    empty_mult = prod(a - 1 for _, a in prime_powers)
    return ans * (1 + (-1) ** r * t) ** empty_mult


def direct_pencil(n, t):
    divs = list(map(int, divisors(n)))
    return Matrix([
        [gcd(d, e) + t * lcm(d, e) for e in divs] for d in divs
    ]).det(method='domain-ge')


def main():
    fixed = 0
    for n in range(1, 241):
        if len(divisors(n)) > 12:
            continue
        expect = predicted_pencil(n, 1)
        got = direct_pencil(n, 1)
        assert expect == got, (n, expect, got)
        fixed += 1
    for n in (256, 343, 625, 900, 1200, 3600, 2700, 81 * 25,
              2 * 3 * 5 * 7, 4 * 9 * 25):
        if len(divisors(n)) <= 36:
            assert predicted_pencil(n, 1) == direct_pencil(n, 1), n
            fixed += 1
    other = 0
    for n in range(1, 71):
        if len(divisors(n)) > 9:
            continue
        for t in (-2, -1, 0, 2):
            expect = predicted_pencil(n, t)
            got = direct_pencil(n, t)
            assert expect == got, (n, t, expect, got)
            other += 1
    t = Symbol('t')
    symbolic = 0
    for n in (1, 2, 4, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36):
        diff = expand(predicted_pencil(n, t) - direct_pencil(n, t))
        assert diff == 0, (n, diff)
        symbolic += 1
    print(f'VERIFY_OK: {fixed} independent exact t=1 determinants; '
          f'{other} additional integer pencil determinants; '
          f'{symbolic} exact symbolic characteristic polynomials')

if __name__ == '__main__':
    main()
