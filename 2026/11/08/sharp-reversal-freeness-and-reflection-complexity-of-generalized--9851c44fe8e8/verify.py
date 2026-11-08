#!/usr/bin/env python3
"""Exact small-factor language and reversal checks for digital-sum residues.

The language enumerator is exhaustive for lengths at most four. It enumerates
all b-adic valuation signatures of up to three consecutive positive integers,
with valuation classes reduced modulo m/gcd(b-1,m). Every signature is
attainable, and every initial letter is attainable by shifting the starting
index by a sufficiently high base-b power multiplied by a suitable repunit.
"""
from math import gcd


def sumdigits(x, b):
    total = 0
    while x:
        total += x % b
        x //= b
    return total


def signatures(b, m, increments):
    q = m // gcd(b - 1, m)
    if increments == 1:
        return {(v,) for v in range(q)}
    if increments == 2:
        s = {(0, 0)} if b >= 3 else set()
        for v in range(1, q + 1):
            s.update(((0, v), (v, 0)))
        return s
    if increments == 3:
        s = {(0, 0, 0)} if b >= 4 else set()
        if b >= 3:
            for v in range(1, q + 1):
                for j in range(3):
                    x = [0, 0, 0]
                    x[j] = v
                    s.add(tuple(x))
        else:
            for v in range(1, q + 1):
                s.add((0, v, 0))
            for v in range(2, q + 2):
                s.update(((v, 0, 1), (1, 0, v)))
        return s
    raise ValueError("Lengths 2, 3, 4 only")


def factors(b, m, n):
    if n == 1:
        return {(a,) for a in range(m)}
    result = set()
    for vals in signatures(b, m, n - 1):
        for a in range(m):
            word = [a]
            for v in vals:
                word.append((word[-1] + 1 - (b-1)*v) % m)
            result.add(tuple(word))
    return result


def witness_start(b, m, vals, first_letter):
    # Construct a small base-b starting index whose following increments have
    # the requested valuations, then adjust the initial letter by high digits.
    if len(vals) == 1:
        N = b ** vals[0] if vals[0] else 1
    elif len(vals) == 2:
        if vals == (0, 0):
            N = 1
        else:
            j = next(j for j,v in enumerate(vals) if v)
            N = b ** vals[j] - j
    elif len(vals) == 3:
        if vals == (0, 0, 0):
            N = 1
        elif b >= 3 or vals[1] != 0:
            j = next(j for j,v in enumerate(vals) if v)
            N = b ** vals[j] - j
        elif vals[0] >= 2:
            N = b ** vals[0]
        else:
            N = b ** vals[2] - 2
    else:
        raise ValueError
    n = N - 1
    assert n >= 0
    H = max(3, len(vals) + 2, max(vals) + 3)
    assert n + len(vals) + 2 < b**H
    target = (first_letter - sumdigits(n, b)) % m
    repunit = sum(b**j for j in range(target))
    start = n + repunit * b**H
    assert sumdigits(start, b) % m == first_letter
    return start


def verify_symbolic():
    settings = 0
    for b in range(2, 40):
        for m in range(3, 40):
            settings += 1
            g = gcd(b - 1, m)
            l2, l3, l4 = (factors(b,m,n) for n in (2,3,4))
            assert len(l2) == m*m//g
            r2 = len({min(w, w[::-1]) for w in l2})
            expected = m*m//g if g > 2 else m*(m+1)//2 if g == 1 else m*m//4
            assert r2 == expected, (b,m,'r2',r2,expected)
            pal3 = [w for w in l3 if w == w[::-1]]
            assert len(pal3) == (2*m if g in (1,2) else 0)
            assert all(w[::-1] not in l3 or w == w[::-1] for w in l3)
            assert all(w[::-1] not in l4 for w in l4)
    print('PASS: exact symbolic L2/L3/L4 and reversal formulas for',settings,'base/modulus pairs')


def verify_witnesses():
    total = 0
    for b in range(2, 12):
        for m in range(3, 12):
            for length in (2,3,4):
                for vals in signatures(b,m,length-1):
                    for a in range(m):
                        n = witness_start(b,m,vals,a)
                        word = tuple(sumdigits(n+j,b)%m for j in range(length))
                        expected=[a]
                        for v in vals:
                            expected.append((expected[-1]+1-(b-1)*v)%m)
                        assert word == tuple(expected),(b,m,length,vals,a,word,expected)
                        total += 1
    print('PASS: constructive high-digit realization of',total,'factors')


def verify_prefixes():
    configs = 0
    for b in range(2,7):
        for m in range(3,7):
            samples=[sumdigits(n,b)%m for n in range(100000)]
            for length in (2,3,4):
                actual={tuple(samples[j:j+length]) for j in range(100000-length+1)}
                assert actual == factors(b,m,length),(b,m,length,len(actual),len(factors(b,m,length)))
            configs+=1
    print('PASS: full direct 100000-symbol language equality at lengths 2/3/4 for',configs,'parameter pairs')

if __name__ == '__main__':
    verify_symbolic()
    verify_witnesses()
    verify_prefixes()
    print('VERIFICATION_OK')
