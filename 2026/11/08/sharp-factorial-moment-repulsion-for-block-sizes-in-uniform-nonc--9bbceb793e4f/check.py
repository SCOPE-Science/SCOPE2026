#!/usr/bin/env python3
"""Exact finite checks for uniform noncrossing-partition block-count factorial bounds."""
from math import comb, factorial, prod
from fractions import Fraction
from collections import Counter
from itertools import combinations_with_replacement


def noncrossing_rgs(n):
    def rec(a, maximum):
        if len(a) == n:
            blocks = {}
            for x, v in enumerate(a):
                blocks.setdefault(v, []).append(x)
            for x, y in combinations_with_replacement(list(blocks), 2):
                if x == y:
                    continue
                A, B = blocks[x], blocks[y]
                for a in A:
                    for c in A:
                        if a >= c:
                            continue
                        for b in B:
                            for d in B:
                                if a < b < c < d or b < a < d < c:
                                    return
            yield Counter(map(len, blocks.values()))
            return
        for v in range(maximum + 2):
            yield from rec(a + [v], max(maximum, v))
    if n == 0:
        yield Counter()
    else:
        yield from rec([0], 0)


def F(n, lengths):
    m, s = len(lengths), sum(lengths)
    if m == 0:
        return Fraction(1)
    if s > n:
        return Fraction(0)
    cat = comb(2*n, n) // (n+1)
    return Fraction(prod(range(n-m+2, n+1)) * comb(2*n-m-s,n-s), cat)


def brute(n,lengths, allcounts):
    cat = len(allcounts)
    counts = Counter(lengths)
    total = 0
    for cc in allcounts:
        term = 1
        for k, r in counts.items():
            val = cc[k]
            if val < r:
                term = 0
                break
            term *= prod(range(val-r+1,val+1))
        total += term
    return Fraction(total,cat)


def main():
    checks=0
    for n in range(3,9):
        allcounts=list(noncrossing_rgs(n))
        assert len(allcounts) == comb(2*n,n)//(n+1)
        checks += 1
        kappa=Fraction((2*n-1)*(n-1),(n+1)*(2*n-3))
        assert 0 < kappa < 1
        checks += 1
        for m in range(1,min(4,n)+1):
            for lens in combinations_with_replacement(range(1,n+1),m):
                if sum(lens)>n:
                    continue
                actual=brute(n,lens,allcounts)
                exact=F(n,lens)
                assert actual==exact,(n,lens,actual,exact)
                checks += 1
                if m >= 2:
                    rhs=kappa**(m-1)*prod(F(n,(x,)) for x in lens)
                    assert exact <= rhs, (n,lens,exact,rhs)
                    checks += 1
                if m == 2:
                    pair=exact/(F(n,(lens[0],))*F(n,(lens[1],)))
                    if tuple(lens) in ((1,1),(1,2)):
                        assert pair==kappa
                    else:
                        assert pair<kappa
                    checks += 1
    for n in range(3,100):
        kappa=Fraction((2*n-1)*(n-1),(n+1)*(2*n-3))
        for a in range(1,n+1):
            for b in range(1,n+1):
                lhs=F(n,(a,b))
                rhs=kappa*F(n,(a,))*F(n,(b,))
                assert lhs<=rhs,(n,a,b,lhs,rhs)
                checks+=1
    print(f'VERIFY_OK {checks} exact assertions')

if __name__ == '__main__':
    main()
