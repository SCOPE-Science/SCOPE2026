#!/usr/bin/env python3
"""Independent finite verification of a deletion-shadow theorem for involutions."""
from collections import defaultdict
from fractions import Fraction


def involutions(n):
    p = [-1] * n
    def recur():
        i = next((i for i, x in enumerate(p) if x < 0), None)
        if i is None:
            yield tuple(x + 1 for x in p)
            return
        p[i] = i
        yield from recur()
        p[i] = -1
        for j in range(i + 1, n):
            if p[j] < 0:
                p[i], p[j] = j, i
                yield from recur()
                p[i], p[j] = -1, -1
    yield from recur()


def deletion_shadow(p):
    n = len(p)
    return {tuple(1 + sum(y < x for y in a) for x in a)
            for k in range(n) for a in [p[:k] + p[k+1:]]}


def motifs(p):
    n = len(p)
    a = sum(p[i] == i + 1 and p[i+1] == i + 2 for i in range(n-1))
    b = sum(p[i] == i + 2 and p[i+1] == i + 1 for i in range(n-1))
    c_plus = sum(p[i] == j+1 and p[i+1] == j+2
                 for i in range(n-1) for j in range(i+2, n-1))
    c_minus = sum(p[i] == j+2 and p[i+1] == j+1
                  for i in range(n-1) for j in range(i+2, n-1))
    e = sum(p[i] == i + 3 and p[i+1] == i+2 and p[i+2] == i+1
            for i in range(n-2))
    return a, b, c_plus, c_minus, e


def exact_mean(n, f):
    if n == 1:
        return Fraction(0)
    m = n-f
    return (Fraction(f*(f-1), n) + Fraction(m, n)
            + 2*Fraction(m*(n-2), n*(n-1)))


def main():
    for n in range(1, 12):
        groups = defaultdict(lambda: [0, 0])
        for p in involutions(n):
            f = sum(v == i+1 for i, v in enumerate(p))
            observed = n - len(deletion_shadow(p)) if n else 0
            a,b,c_plus,c_minus,e = motifs(p)
            assert observed == a+b+2*(c_plus+c_minus+e), (n,p,observed,a,b,c_plus,c_minus,e)
            groups[f][0] += observed
            groups[f][1] += 1
        for f,(total,count) in sorted(groups.items()):
            assert Fraction(total,count) == exact_mean(n, f), (n,f,total,count,exact_mean(n,f))
        print('n',n,'checked',sum(x[1] for x in groups.values()),
              'strata',len(groups),'all exact',flush=True)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
