"""Reproducible finite checks for sparse binary composition reconstruction.

This tests both an independently computed substring-composition multiset
and the gap-polynomial identities used in the unrestricted-length proof.
Requires only the Python standard library.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def spectrum(s):
    hist = Counter()
    n = len(s)
    for i in range(n):
        ones = 0
        for j in range(i, n):
            ones += (s[j] == '1')
            hist[(j - i + 1, ones)] += 1
    return tuple(sorted(hist.items()))


def word(positions, n):
    p = set(positions)
    return ''.join('1' if i in p else '0' for i in range(n))


def poly_mul(p, q):
    out = Counter()
    for i, v in p.items():
        for j, w in q.items():
            out[i + j] += v * w
    return +out


def geom(t):
    return {i: 1 for i in range(t + 1)}


def shift(p, r):
    return {i + r: v for i, v in p.items()}


def marginal(s, k):
    return Counter({ell: c for (ell, j), c in spectrum(s) if j == k})


def test_polynomials():
    checked = 0
    for total in range(13):
        for a in range(total + 1):
            for b in range(total - a + 1):
                for c in range(total - a - b + 1):
                    d = total - a - b - c
                    s = '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
                    predicted3 = Counter(shift(poly_mul(geom(a), geom(d)), b+c+3))
                    predicted2 = Counter(shift(poly_mul(geom(a), geom(c)), b+2))
                    predicted2.update(shift(poly_mul(geom(b), geom(d)), c+2))
                    predicted0 = Counter()
                    for g in (a,b,c,d):
                        for length in range(1, g+1):
                            predicted0[length] += g-length+1
                    assert marginal(s, 3) == predicted3, (s, 'Q3')
                    assert marginal(s, 2) == predicted2, (s, 'Q2')
                    assert marginal(s, 0) == predicted0, (s, 'Q0')
                    checked += 1
    return checked


def test_complete_reconstruction():
    checked = 0
    for n in range(3, 27):
        profiles = defaultdict(list)
        for pos in combinations(range(n), 3):
            s = word(pos, n)
            profiles[spectrum(s)].append(s)
            checked += 1
        assert len(profiles) == (comb(n, 3) + ((n-1)//2 if n%2 else 0)) // 2, n
        for fiber in profiles.values():
            assert len(fiber) <= 2
            for s in fiber:
                assert all(t == s or t == s[::-1] for t in fiber)
    return checked


def test_difference_identity():
    checked = 0
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    s = '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d
                    t = '0'*a+'1'+'0'*c+'1'+'0'*b+'1'+'0'*d
                    is_equal = marginal(s,2)==marginal(t,2)
                    assert is_equal == (a==d or b==c), (a,b,c,d)
                    checked+=1
    return checked


def test_threshold():
    x, y = '10110010','10010110'
    assert len(x)==len(y)==8 and x.count('1')==y.count('1')==4
    assert x != y and x != y[::-1]
    assert spectrum(x)==spectrum(y)
    return (x,y)


if __name__ == '__main__':
    polynomials = test_polynomials()
    words = test_complete_reconstruction()
    differences = test_difference_identity()
    examples = test_threshold()
    print(f'VERIFY_OK polynomials={polynomials} words={words} differences={differences} threshold={examples}')
