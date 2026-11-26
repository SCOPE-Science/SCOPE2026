"""Exact finite check, using the polynomial kernels on either side of the diagonal."""
from collections import defaultdict
from fractions import Fraction
from math import comb


def piece(m, n, x_less_y):
    # The common nonzero scale (m-1)!(n-1)! is omitted; it does not affect rank.
    p = defaultdict(Fraction)
    for a in range(m):
        for b in range(n):
            i, j, k = m-1-a, n-1-b, a+b+1
            c = Fraction(comb(m-1, a)*comb(n-1, b), k)
            # First integral from 0 to min(x,y).
            lo = (i+k, j) if x_less_y else (i, j+k)
            p[lo] += (-1)**(a+b)*c
            # Subtract integral from max(x,y) to 1; powers of x,y are swapped.
            c *= (-1)**(i+j)
            p[j, i] -= c
            hi = (j, i+k) if x_less_y else (j+k, i)
            p[hi] += c
    return {ij: c for ij, c in p.items() if c}


def rank(p, size):
    pivots = {}
    for i in range(size):
        row = [p.get((i, j), Fraction(0)) for j in range(size)]
        for j in range(size):
            if row[j]:
                if j not in pivots:
                    pivots[j] = [c/row[j] for c in row]
                    break
                row = [c-row[j]*b for c, b in zip(row, pivots[j])]
    return len(pivots)


if __name__ == '__main__':
    count = 0
    for m in range(1, 6):
        for n in range(1, 6):
            if m == n:
                continue
            left = piece(m, n, True)
            assert left == piece(m, n, False)
            assert rank(left, m+n) == 2*min(m, n)
            count += 1
    print(f'PASS: {count} ordered unequal pairs')
