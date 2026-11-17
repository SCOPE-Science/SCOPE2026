"""Exact rational verification for the cyclic three-point mean--median blend.

Run with Python 3: python checker.py
The symbolic proof of the unrestricted statement is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import permutations


def median3(a, b, c):
    return sorted((a, b, c))[1]


def output(x, w):
    n = len(x)
    return [(1-w)*median3(x[(i-1)%n], x[i], x[(i+1)%n])
            + w*(x[(i-1)%n]+x[i]+x[(i+1)%n])/3 for i in range(n)]


def variation(x):
    return sum(abs(x[(i+1)%len(x)]-x[i]) for i in range(len(x)))


def sharp_data(n):
    assert n >= 6
    if n == 6:
        x = [0, 2, 1, 5, 3, 4]
    else:
        x = [None]*n
        for i, v in {0:0, 1:2, 2:1, 3:5, n-3:6, n-2:3, n-1:4}.items():
            x[i] = v
        for i in range(n):
            if x[i] is None:
                x[i] = 10+i
    h = [int(2 <= i <= n-2) for i in range(n)]
    return [Q(v) for v in x], [Q(v) for v in h]


for n in range(6, 24):
    x, h = sharp_data(n)
    e = Q(1, 4)
    y = [u + e*v for u, v in zip(x, h)]
    assert variation([a-b for a, b in zip(y,x)]) == 2*e
    for w in [Q(0), Q(1,5), Q(1,2), Q(3,4), Q(9,10), Q(1)]:
        fx, fy = output(x, w), output(y, w)
        ratio = variation([a-b for a,b in zip(fy,fx)])/(2*e)
        assert ratio == max(Q(1), Q(3)-Q(8,3)*w), (n,w,ratio)
print('EXACT_SHARP_WITNESSES_N6_TO23_PASS')

# Full rank-order chamber enumeration for short cycles, with all input-edge
# columns, including direct checking of the local difference factorization.
for n in [6, 7, 8]:
    checks = 0
    for x in permutations(range(n)):
        selector = []
        for i in range(n):
            ix = ((i-1)%n, i, (i+1)%n)
            selector.append(sorted(ix, key=lambda j: x[j])[1])
        d = [x[(j+1)%n]-x[j] for j in range(n)]
        actual = [x[selector[(i+1)%n]]-x[selector[i]] for i in range(n)]
        computed = [0]*n
        for j in range(n):
            a = int(selector[j] == (j+1)%n)
            c = int(selector[(j+1)%n] == j)
            vals = (a, 1-a-c, c)
            for k in range(3):
                computed[(j-1+k)%n] += vals[k]*d[j]
            for m in [0, 1, 2, 4, 6, 7, 8]:
                num = [3*(8-m)*a+m,
                       3*(8-m)*(1-a-c)+m,
                       3*(8-m)*c+m]
                assert sum(abs(z) for z in num) <= max(24, 72-8*m)
                checks += 1
        assert computed == actual, (n, x, computed, actual)
    print('ALL_RANK_CHAMBERS_FACTOR_AND_COLUMNS_PASS', n, checks)
print('ALL_MEAN_MEDIAN_VARIATION_CHECKS_PASS')
