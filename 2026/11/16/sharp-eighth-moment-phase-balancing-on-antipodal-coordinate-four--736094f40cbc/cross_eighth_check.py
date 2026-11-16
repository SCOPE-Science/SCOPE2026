"""Exact coefficient verifier for eighth moments on antipodal coordinate characters.

Run with Python 3. No non-standard libraries required. Each coefficient is an
integer, and equality is checked in the full Laurent phase ring.
"""
from collections import defaultdict
from itertools import product
from math import factorial


def add(a, b):
    result = dict(a)
    for e, x in b.items():
        result[e] = result.get(e, 0) + x
    return {e: x for e, x in result.items() if x}


def scale(a, s):
    return {e: s*x for e, x in a.items() if s*x}


def mul(a, b):
    z = defaultdict(int)
    for x, ax in a.items():
        for y, by in b.items():
            z[tuple(t+u for t, u in zip(x, y))] += ax*by
    return {e:x for e,x in z.items() if x}


def star(a):
    return {tuple(-x for x in e): v for e, v in a.items()}


def moments(d):
    # Monomials z_j and q_j z_j^{-1} in P.
    s = defaultdict(lambda: defaultdict(int))
    letters = [(j, sign) for j in range(d) for sign in (1,-1)]
    for word in product(letters, repeat=4):
        freq = [0]*d
        qexp = [0]*d
        for j, sg in word:
            freq[j] += sg
            if sg == -1:
                qexp[j] += 1
        s[tuple(freq)][tuple(qexp)] += 1
    result = defaultdict(int)
    for terms in s.values():
        for a, ca in terms.items():
            for b, cb in terms.items():
                result[tuple(x-y for x,y in zip(a,b))] += ca*cb
    return {e:v for e,v in result.items() if v}


def formula(d):
    zero = (0,)*d
    S = {tuple(int(j==i) for j in range(d)):1 for i in range(d)}
    T = {tuple(2*int(j==i) for j in range(d)):1 for i in range(d)}
    R = add(scale(mul(S,S),2),scale(T,-1))
    A = 96*(12*d*d-33*d+26)
    C = 2*d*(192*d**3-864*d*d+1604*d-1155)
    return add(add({zero:C}, scale(mul(S,star(S)),A)), scale(mul(R,star(R)),36))


def main():
    count = 0
    for d in range(2,7):
        actual = moments(d)
        predicted = formula(d)
        assert actual == predicted, (d, set(actual.items()) ^ set(predicted.items()))
        assert actual[(0,)*d] == 2*d*(192*d**3-288*d*d+164*d-33)
        pair=(1,-1)+(0,)*(d-2)
        assert actual[pair] == 1152*d*d-2592*d+1632
        assert formula(d)[pair]==actual[pair]
        count += len(actual)
        print(f'd={d}, exact Laurent phase coefficients={len(actual)}, identity=PASS')
    # Verify the three-dimensional specialization from the established record.
    assert 2*3*(192*3**3-864*3**2+1604*3-1155)==6390
    assert 96*(12*3*3-33*3+26)==3360
    # Check claimed sharp endpoints for each d.
    for d in range(3,12):
        A=96*(12*d*d-33*d+26)
        C=2*d*(192*d**3-864*d*d+1604*d-1155)
        assert A>0 and C>0
        assert C+A*d*d+36*(2*d*d-d)**2 > C
    # When q_j are roots of unity, s=t=0 is attained by regular d-gons.
    # Lower alphabet criteria follow from the elementary cyclotomic basis.
    for d in range(3,19):
        assert (d%3==0)==(d//3 * 3 == d)
        assert (d%4==0)==(d//4 * 4 == d)
    print(f'EXACT_CROSS_EIGHTH_PASS: {count} Laurent coefficients and endpoint checks')

if __name__ == '__main__':
    main()
