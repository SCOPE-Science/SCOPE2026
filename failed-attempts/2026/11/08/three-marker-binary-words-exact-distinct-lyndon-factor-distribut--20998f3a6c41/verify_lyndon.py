#!/usr/bin/env python3
"""Independent exact checks for distinct Lyndon factors of three-one binary words.

No nonstandard libraries are needed. The coefficient expansion implements
geometric-series products separately from the factor enumeration.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def lyndon(q):
    return all(q < q[i:] for i in range(1, len(q)))


def direct_count(w):
    factors = {w[i:j] for i in range(len(w)) for j in range(i+1, len(w)+1)}
    return sum(map(lyndon, factors))


def gap_count(a, b, c, d):
    if a == b == c == d == 0:
        return 1
    return (max(a, b, c) + 2 + max(a-b, 0) + max(b-c, 0)
            + max(a-max(b, c), 0) + int(c < b <= a))


def series_term(nmax, zshift, ushift, factors):
    """Expand z^zshift u^ushift * product (1-z^p u^q)^(-1)."""
    out = Counter({(zshift, ushift): 1})
    for p, q in factors:
        new = Counter()
        for (k, v), coef in out.items():
            for j in range((nmax-k)//p+1):
                new[(k+j*p, v+j*q)] += coef
        out = new
    return out


def gf_coefficients(nmax):
    # G(z,u)=u-u^2+(1-z)^(-1)(1-z^3u)^(-1) times the bracket.
    terms = [
        (0, 2, [(1, 3)]),
        (2, 5, [(2, 2), (1, 3)]),
        (2, 4, [(2, 2), (1, 3)]),
        (1, 4, [(2, 2), (1, 2)]),
        (2, 3, [(2, 1), (1, 2)]),
        (1, 3, [(2, 2), (1, 1)]),
        (3, 4, [(2, 1), (1, 1)]),
    ]
    ans = Counter({(0,1):1,(0,2):-1})
    for p, q, factors in terms:
        ans.update(series_term(nmax,p,q,[(1,0),(3,1)]+factors))
    return +ans


def check_direct(max_n=21):
    checked = 0
    for n in range(3, max_n+1):
        dist = Counter()
        for positions in combinations(range(n), 3):
            w = ''.join('1' if j in positions else '0' for j in range(n))
            a=positions[0]
            b=positions[1]-positions[0]-1
            c=positions[2]-positions[1]-1
            d=n-1-positions[2]
            brute=direct_count(w)
            pred=gap_count(a,b,c,d)
            assert brute == pred, (w, brute, pred)
            dist[pred]+=1
            checked+=1
        assert sum(dist.values()) == comb(n,3)
        gf = Counter({v:c for (k,v),c in gf_coefficients(n-3).items() if k==n-3})
        assert gf == dist, (n, gf,dist)
    return checked


def check_extended(max_n=70):
    gf=gf_coefficients(max_n-3)
    for n in range(3,max_n+1):
        counts=Counter()
        for a in range(n-2):
            for b in range(n-2-a):
                for c in range(n-2-a-b):
                    d=n-3-a-b-c
                    counts[gap_count(a,b,c,d)] += 1
        assert counts==Counter({v:k for (j,v),k in gf.items() if j==n-3})
    return max_n


def check_moments():
    # In each of six order chambers, transformed lengths have Dirichlet(1,1,1,1).
    cs=[(Fraction(1,3),1,3),(Fraction(1,3),1,3),
        (Fraction(1,3),1,2),(Fraction(1,3),Fraction(1,2),2),
        (Fraction(1,3),1,1),(Fraction(1,3),Fraction(1,2),1)]
    means=[];seconds=[]
    for coef in cs:
        coef=[Fraction(v) for v in coef]
        means.append(sum(coef)/4)
        seconds.append((sum(v*v for v in coef)+sum(coef)**2)/20)
    mu=sum(means)/6
    sec=sum(seconds)/6
    variance=sec-mu*mu
    assert mu == Fraction(19,24)
    assert variance == Fraction(563,2880)
    return mu, variance


if __name__=='__main__':
    print('WORDS_CHECKED',check_direct())
    print('GF_CHECKED_TO_LENGTH',check_extended())
    print('LIMIT_MOMENTS',*(str(q) for q in check_moments()))
    print('VERIFY_OK')
