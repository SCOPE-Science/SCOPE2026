#!/usr/bin/env python3
"""Exact top Schubert intersection checks for three-plane Grassmannians.

No external packages.  Pieri multiplication and Vandermonde coefficient
extraction are independent evaluations of the same integral.
"""
import json
import math
import sys
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from pathlib import Path

@lru_cache(None)
def vertical(part, width, height):
    ans = []
    for inds in combinations(range(3), height):
        other = list(part)
        for i in inds:
            other[i] += 1
        if other[0] <= width and other[0] >= other[1] >= other[2]:
            ans.append(tuple(other))
    return ans


def pieri_integral(width, b):
    a = 3 * width - 2 * b
    x = {(0, 0, 0): 1}
    for height, n in ((2, b), (1, a)):
        for _ in range(n):
            y = defaultdict(int)
            for part, count in x.items():
                for nxt in vertical(part, width, height):
                    y[nxt] += count
            x = y
    return x.get((width,) * 3, 0)


@lru_cache(None)
def factorial(n):
    return math.factorial(n)


def multinomial(n, triple):
    if min(triple) < 0 or sum(triple) != n:
        return 0
    return factorial(n) // math.prod(factorial(i) for i in triple)


def coeff_product(a, b, exp):
    """Coefficient of x^exp in (x+y+z)^a (xy+xz+yz)^b."""
    answer = 0
    for u in range(b + 1):
        for v in range(b - u + 1):
            w = b - u - v
            residual = (exp[0] - u - v,
                        exp[1] - u - w,
                        exp[2] - v - w)
            answer += multinomial(b, (u, v, w)) * multinomial(a, residual)
    return answer


def coefficient_integral(width, b):
    """Alternant extraction from the three-variable Chern-root formula."""
    a = 3 * width - 2 * b
    t = width
    signed_exps = [
        ((t, t, t), 1),
        ((t, t + 1, t - 1), -1),
        ((t + 1, t - 1, t), -1),
        ((t + 1, t + 1, t - 2), 1),
        ((t + 2, t - 1, t - 1), 1),
        ((t + 2, t, t - 2), -1),
    ]
    return sum(sgn * coeff_product(a, b, exps)
               for exps, sgn in signed_exps)


def calculate():
    rows = []
    for width in range(1, 17):
        vals = [pieri_integral(width, b)
                for b in range(3 * width // 2 + 1)]
        separate = [coefficient_integral(width, b)
                    for b in range(len(vals))]
        assert vals == separate, 'the two exact constructions disagree'
        assert all(v > 0 for v in vals)
        g = 0
        for val in vals:
            g = math.gcd(g, val)
        assert g == (3 if 13 <= width <= 15 else 1)
        rows.append({'width': width, 'gcd': g, 'integrals': vals})
    return {'basis': 'top Schubert point class',
            'class_monomials': 'e1^(3*width-2*b) e2^b',
            'b_range': '0 <= b <= floor(3*width/2)',
            'rows': rows}


def main():
    data = calculate()
    if len(sys.argv) == 2:
        saved = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        assert saved == data, 'certificate is not equal to recomputed values'
    for row in data['rows']:
        print('WIDTH', row['width'], 'GCD', row['gcd'],
              'PAIRS', len(row['integrals']))
    print('PIERI_AND_ALTERNANT_CHECKS_OK')
    print('FIRST_NONPRIMITIVE_WINDOW_EXACT')


if __name__ == '__main__':
    main()
