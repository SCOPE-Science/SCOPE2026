#!/usr/bin/env python3
"""Independent exact-enumeration checks of crossing/simple-chord joint law.
This script verifies finite cases only; the all-size statements follow from
combinatorial deletion and published crossing-limit results in RESULT.md.
"""
from fractions import Fraction
from collections import Counter
from math import comb, factorial


def pairings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for j in range(1, len(vertices)):
        second = vertices[j]
        for tail in pairings(vertices[1:j] + vertices[j+1:]):
            yield ((first, second),) + tail


def stats(matching, n):
    if n == 0:
        return 0, 0
    s = sum((b-a == 1 or (a == 0 and b == 2*n-1)) for a,b in matching)
    x = sum(a<c<b<d or c<a<d<b
            for i,(a,b) in enumerate(matching)
            for c,d in matching[i+1:])
    return s,x


def count_matchings(n):
    return factorial(2*n)//(2**n*factorial(n))


def cycle_matching_count(n,k):
    return (2*n*comb(2*n-k,k))//(2*n-k)


def factorial_moment(n,k):
    v = Fraction(1)
    for j in range(k):
        v *= Fraction(2*n-2*j,2*n-j-1)
    return v


def main():
    checks = 0
    cross_laws = {}
    for n in range(0,8):
        cross_laws[n] = Counter()
        counts = Counter()
        M = 0
        for mat in pairings(tuple(range(2*n))):
            s,x = stats(mat,n)
            counts[s,x] += 1
            cross_laws[n][x] += 1
            M += 1
        assert M == count_matchings(n)
        checks += 1
        if n < 2:
            continue
        # Exact conditional-deletion factorial generating-function identity,
        # one crossing coefficient at a time, for all 0 <= k <= n.
        for k in range(n+1):
            mk = cycle_matching_count(n,k)
            denom = 1
            for j in range(k):
                denom *= (2*n-2*j-1)
            c = Fraction(mk,denom)
            assert factorial_moment(n,k) == factorial(k)*c
            checks += 1
            xvals = set(cross_laws[n]) | set(cross_laws[n-k])
            for x in xvals:
                lhs = Fraction(sum(comb(s,k)*v for (s,y),v in counts.items() if y == x), M)
                rhs = c*Fraction(cross_laws[n-k][x],count_matchings(n-k))
                assert lhs == rhs, (n,k,x,lhs,rhs)
                checks += 1
        E_S = sum(Fraction(s*v,M) for (s,x),v in counts.items())
        E_X = sum(Fraction(x*v,M) for (s,x),v in counts.items())
        VarS = sum(Fraction((s*s)*v,M) for (s,x),v in counts.items())-E_S**2
        VarX = sum(Fraction((x*x)*v,M) for (s,x),v in counts.items())-E_X**2
        Cov = sum(Fraction((s*x)*v,M) for (s,x),v in counts.items())-E_S*E_X
        assert E_S == Fraction(2*n,2*n-1)
        assert E_X == Fraction(n*(n-1),6)
        assert VarS == Fraction(4*n*(n-1),(2*n-1)**2)
        assert VarX == Fraction(n*(n-1)*(n+3),45)
        assert Cov == Fraction(-2*n*(n-1),3*(2*n-1))
        assert Cov*Cov == Fraction(5,n+3)*VarX*VarS
        assert Cov < 0
        checks += 7
        print('n',n,'matchings',M,'meanX',E_X,'cov',Cov)
    print('VERIFY_OK',checks,'exact assertions; n=2..7 complete matchings')

if __name__=='__main__':
    main()
