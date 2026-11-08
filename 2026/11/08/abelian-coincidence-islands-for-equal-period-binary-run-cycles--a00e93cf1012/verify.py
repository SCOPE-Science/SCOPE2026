#!/usr/bin/env python3
"""Independent finite verification of the two-run Abelian coincidence spectrum.
Requires Python 3.8+ standard library.  All comparisons use explicit factors."""
from itertools import product


def actual(a, b, c, d, n):
    assert a + b == c + d and n >= 1
    length = a + b
    x = ('0' * a + '1' * b) * (1 + (n + length - 1) // length)
    y = ('0' * c + '1' * d) * (1 + (n + length - 1) // length)
    xs = {x[i:i+n].count('0') for i in range(length)}
    ys = {y[i:i+n].count('0') for i in range(length)}
    return len(xs & ys)


def predicted(a, b, c, d, n):
    assert a + b == c + d and n >= 1
    if a < c:
        a, b, c, d = c, d, a, b
    length = a + b
    t, r = divmod(n, length)
    if a == c:
        return min(a, r) - max(0, r-b) + 1
    return max(0, min(c, r) - max(0, r-b) - t * (a-c) + 1)


def intervals(a, b, c, d):
    if a < c:
        a, b, c, d = c, d, a, b
    delta = a-c
    assert delta >= 1
    bound = min(c, b) // delta
    return [(t*(a+d), (t+1)*(b+c)) for t in range(bound+1)]


def run():
    cases = 0
    lengths = 0
    gaps = 0
    for period in range(2, 22):
        for a in range(1, period):
            for c in range(1, period):
                b, d = period-a, period-c
                if a == c:
                    top = 3 * period
                    for n in range(1, top+1):
                        assert actual(a, b, c, d, n) == predicted(a, b, c, d, n), (a,b,c,d,n)
                        lengths += 1
                else:
                    blocks = intervals(a, b, c, d)
                    assert all(lo <= hi for lo, hi in blocks)
                    assert all(blocks[j][1] < blocks[j+1][0] for j in range(len(blocks)-1))
                    top = blocks[-1][1] + period + 2
                    for n in range(1, top+1):
                        k = actual(a, b, c, d, n)
                        p = predicted(a, b, c, d, n)
                        assert k == p, (a,b,c,d,n,k,p)
                        exists = any(lo <= n <= hi for lo,hi in blocks)
                        assert (k>0) == exists, (a,b,c,d,n,k,blocks)
                        lengths += 1
                        if not exists and n < blocks[-1][1]:
                            gaps += 1
                cases += 1
    print('VERIFY_OK', 'parameter_pairs='+str(cases),
          'length_and_class_checks='+str(lengths), 'internal_gap_checks='+str(gaps))


if __name__ == '__main__':
    run()
