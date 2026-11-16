"""Exact arithmetic verification of digit-tower Fourier moments.
Only finite cases are checked. The all-level theorem is proved separately.
"""
from math import comb
from collections import defaultdict


def binomial(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def moments_via_carries(b, r, n):
    # At r <= b, reachable carries lie in {-1,0,1}.
    weights = {0: 1}
    for _ in range(n):
        next_weights = defaultdict(int)
        for u, val in weights.items():
            for v in (-1, 0, 1):
                c = binomial(2*r, r+b*v-u)
                if c:
                    next_weights[v] += val*c
        weights = next_weights
    return weights.get(0, 0)


def moments_direct(b, r, n):
    support = [sum(((mask >> j) & 1)*b**j for j in range(n))
               for mask in range(1 << n)]
    poly = {0: 1}
    for _ in range(r):
        new = defaultdict(int)
        for s, coeff in poly.items():
            for t in support:
                new[s+t] += coeff
        poly = new
    return sum(v*v for v in poly.values())


def main():
    checks = 0
    for b in range(2, 9):
        for r in range(1, b+1):
            for n in range(1, 5):
                direct = moments_direct(b, r, n)
                carries = moments_via_carries(b, r, n)
                assert direct == carries, (b, r, n, direct, carries)
                checks += 1
                if r < b:
                    assert direct == comb(2*r, r)**n, (b, r, n)
                    checks += 1
                if r == b:
                    C, K, a = comb(2*b, b), comb(2*b, b-1), 2*b
                    q0, q1 = 1, C
                    for _ in range(n-1):
                        q0, q1 = q1, (C+a)*q1 - (a*C-2*K)*q0
                    assert direct == q1, (b, n, direct, q1)
                    checks += 1
    assert [moments_direct(4,4,n) for n in range(1,5)] == [70,5012,359576,25801552]
    checks += 1
    print(f'PASS: {checks} exact independent checks; b=2..8, n=1..4, r=1..b; base four moments [70, 5012, 359576, 25801552]')


if __name__ == '__main__':
    main()
