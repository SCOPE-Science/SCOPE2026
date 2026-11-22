#!/usr/bin/env python3
"""Independent exact finite-extension enumeration for ordered antichain posets."""
from itertools import combinations


def predicted_by_gaps(l, m, r):
    first = (1 << l) + (1 << (m + r)) - 1
    second = (1 << (l + m)) + (1 << r) - 1
    inc = first * second - (1 << (l + r)) * (4**m - 3**m)
    comp = (1 << (l + r)) * 4**m + (3**l + 3**r - (1 << l) - (1 << r)) * (1 << m)
    return comp, inc


def direct_by_gaps(l, m, r):
    n = l + m + r
    positions = list(range(l)) + ['x'] + list(range(l, l + m)) + ['y'] + list(range(l + m, n))
    k = len(positions)
    possible = [(i, j) for i in range(k) for j in range(i + 1, k)
                if positions[i] in ('x', 'y') or positions[j] in ('x', 'y')]
    x_pos, y_pos = positions.index('x'), positions.index('y')
    comparable = incomparable = 0
    for mask in range(1 << len(possible)):
        out = [0] * k
        for bit, (i, j) in enumerate(possible):
            if mask & (1 << bit):
                out[i] |= 1 << j
        # The full relation must be closed under all length-two paths.
        valid = True
        for i in range(k):
            if not valid:
                break
            for j in range(i + 1, k):
                if not (out[i] >> j & 1):
                    continue
                if out[j] & ~out[i]:
                    valid = False
                    break
        if valid:
            if out[x_pos] >> y_pos & 1:
                comparable += 1
            else:
                incomparable += 1
    return comparable, incomparable


def closed_counts(n):
    C = 8 * 4**n + 18 * 3**n - (10*n+22) * 2**n - 2
    I_num = 32*4**n + 54*3**n - (24*n+120)*2**n + 3*n*n+21*n+40
    assert I_num % 3 == 0
    I = I_num // 3
    T_num = 56*4**n + 108*3**n - (54*n+186)*2**n + 3*n*n+21*n+34
    assert T_num % 3 == 0
    T = T_num // 3
    assert T == C + I
    return C, I, T


def sum_gaps(n, brute=False):
    cc = ii = 0
    for l in range(n+1):
        for m in range(n-l+1):
            r = n-l-m
            pred = predicted_by_gaps(l, m, r)
            if brute:
                direct = direct_by_gaps(l, m, r)
                assert direct == pred, (n,l,m,r,pred,direct)
            cc += pred[0]
            ii += pred[1]
    return 2*cc, 2*ii, 2*(cc+ii)


def one_type_count(n):
    # An extension in a fixed linear-order gap is either above a nonempty
    # subset to its left, below a nonempty subset to its right, or free.
    return sum((1 << i) + (1 << (n-i)) - 1 for i in range(n+1))


def main():
    for n in range(6):
        a = sum_gaps(n,brute=True)
        b = closed_counts(n)
        assert a == b, (n,a,b)
        assert one_type_count(n) == 2**(n+2)-n-3
        print('BRUTE_OK', n, 'comparable',a[0], 'incomparable',a[1], 'total',a[2])
    for n in range(6, 41):
        assert sum_gaps(n) == closed_counts(n)
        assert one_type_count(n) == 2**(n+2)-n-3
    print('GAP_SUMS_AND_CLOSED_FORMS_OK n=0..40')
    for n in [10,20,40]:
        c,i,t=closed_counts(n)
        print('EXACT', n, 'comparable',c,'incomparable',i,'total',t)
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
