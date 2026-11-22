#!/usr/bin/env python3
"""Independent integer and modular checks for adjacent quadratic valuation pairs."""
from collections import Counter
from fractions import Fraction


def nu2(n):
    if n == 0:
        return None
    n = abs(n)
    return (n & -n).bit_length() - 1


def parameter(a, b, c):
    r = a*a - b*b + 4*a*c
    return None if r == 0 else nu2(r) - 1


def expected(i, j, d):
    if min(i, j) == 1 and max(i, j) >= 2:
        return Fraction(1, 1 << (max(i, j)+1))
    if i == j and (d is None or i < d):
        return Fraction(1, 1 << (i+1))
    if d is not None and min(i, j) == d and max(i, j) > d:
        return Fraction(1, 1 << (max(i, j)+1))
    return Fraction(0)


def values(a, b, c, n):
    return (nu2(a*n*n+b*n+c),
            nu2(a*(n+1)*(n+1)+b*(n+1)+c))


def test(a, b, c, n=8192):
    d = parameter(a,b,c)
    observed = Counter(values(a,b,c,x) for x in range(n))
    for i in range(1, 10):
        for j in range(1, 10):
            got = Fraction(observed[(i,j)], n)
            want = expected(i,j,d)
            if max(i,j) <= 9 and got != want:
                raise AssertionError((a,b,c,i,j,got,want,d))
    # Each nonempty cell has precisely one residue mod 2^(max(i,j)+1).
    for i in range(1, 8):
        for j in range(1, 8):
            m = 1 << (max(i,j)+1)
            hits = sum(values(a,b,c,x) == (i,j) for x in range(m))
            want = int(expected(i,j,d) * m)
            if hits != want or want not in (0,1):
                raise AssertionError(('class',a,b,c,i,j,hits,want))
    return d


def main():
    triples = [(1,1,2),(1,1,4),(1,3,2),(3,1,2),(3,3,2),
               (5,7,2),(3,5,6),(1,5,6),(7,9,16),(3,7,28),
               (1,7,12),(3,9,6)]
    for a in (1,3,5,7,9):
        for b in (1,3,5,7,9):
            for c in (2,4,6,8,10):
                if (a,b,c) not in triples:
                    triples.append((a,b,c))
    for a,b,c in triples:
        test(a,b,c)
    print('PASS:',len(triples),'coefficient triples; 2^13-index blocks; exact joint counts for 81 cells and one-residue checks for 49 cells per triple')
    print('Degenerate R=0 example (1,3,2):',parameter(1,3,2),'(None means infinite)')
    print('Covariance (1,1,2):',Fraction(1,2)-Fraction(3,1<<2))
    print('Covariance (1,1,4):',Fraction(1,2)-Fraction(3,1<<3))


if __name__ == '__main__':
    main()
